# db.py
import os
from psycopg.rows import dict_row
from psycopg_pool import AsyncConnectionPool

# Goal: migrate from sqlite3 to PostgreSQL 14 using psycopg v3 async pool.
# Tasks:
# 1) Add file db.py exactly as provided in the spec (psycopg_pool AsyncConnectionPool, helpers: init_pool, close_pool, fetchone, fetchall, execute, executemany, ping).
# 2) Read DSN from env var POSTGRES_DSN. Do NOT hardcode credentials.
# 3) At bot startup (bot.py/start.py), call await init_pool() before polling and await close_pool() in finally. Add a ping() assert.
# 4) Replace all SQLite usages with calls to db.py helpers and %s placeholders.
# 5) Add schema_pg.sql (from the spec) and a note to apply it with psql manually.
# 6) Ensure .env contains: POSTGRES_DSN=postgresql://postgres:admin@localhost:5432/vpnbot (plus existing tokens).
# 7) Acceptance: project runs without sqlite; all queries go via db.py; grep for 'sqlite3' returns nothing.

POSTGRES_DSN = os.getenv(
    "POSTGRES_DSN",
    "postgresql://postgres:admin@localhost:5432/vpnbot"
)

pool: AsyncConnectionPool | None = None


async def init_schema() -> None:
    """Ensure required tables and indexes exist."""
    if pool is None:
        raise RuntimeError("DB pool is not initialized. Call init_pool() first.")

    statements = [
        """
        CREATE TABLE IF NOT EXISTS users (
          id            BIGSERIAL PRIMARY KEY,
          tg_user_id    BIGINT UNIQUE NOT NULL,
          joined_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          last_seen_at  TIMESTAMPTZ,
          locale        TEXT DEFAULT 'ru',
          is_banned     BOOLEAN NOT NULL DEFAULT FALSE,
          ref_code      TEXT UNIQUE,
          referred_by   TEXT,
          device_limit  INT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS subscriptions (
          id         BIGSERIAL PRIMARY KEY,
          user_id    BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
          plan       TEXT NOT NULL,
          status     TEXT NOT NULL,
          started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          expires_at TIMESTAMPTZ NOT NULL,
          source     TEXT
        );
        """,
        "CREATE INDEX IF NOT EXISTS ix_sub_user ON subscriptions(user_id);",
        "CREATE INDEX IF NOT EXISTS ix_sub_active ON subscriptions(user_id,status,expires_at);",
        """
        CREATE TABLE IF NOT EXISTS devices (
          id                BIGSERIAL PRIMARY KEY,
          user_id           BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
          label             TEXT,
          platform          TEXT,
          type              TEXT,
          config_id         TEXT,
          public_key        TEXT,
          created_at        TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          revoked_at        TIMESTAMPTZ,
          status            TEXT NOT NULL DEFAULT 'active',
          last_handshake_at TIMESTAMPTZ,
          bytes_up          BIGINT NOT NULL DEFAULT 0,
          bytes_down        BIGINT NOT NULL DEFAULT 0
        );
        """,
        "CREATE INDEX IF NOT EXISTS ix_dev_user ON devices(user_id);",
        "CREATE INDEX IF NOT EXISTS ix_dev_active ON devices(user_id,status);",
        """
        CREATE TABLE IF NOT EXISTS traffic_daily (
          id         BIGSERIAL PRIMARY KEY,
          user_id    BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
          device_id  BIGINT REFERENCES devices(id) ON DELETE SET NULL,
          date       DATE NOT NULL,
          bytes_up   BIGINT NOT NULL DEFAULT 0,
          bytes_down BIGINT NOT NULL DEFAULT 0,
          UNIQUE(user_id, device_id, date)
        );
        """,
        "CREATE INDEX IF NOT EXISTS ix_traffic_date ON traffic_daily(date);",
    ]

    async with pool.connection() as ac:
        async with ac.cursor() as cur:
            for statement in statements:
                await cur.execute(statement)
        await ac.commit()

    print("✅ Schema initialized")


async def init_pool(min_size: int = 1, max_size: int = 10) -> None:
    """
    Инициализация пула соединений. Вызывать один раз при старте бота.
    """
    global pool
    if pool is not None:
        return
    pool = AsyncConnectionPool(
        POSTGRES_DSN,
        min_size=min_size,
        max_size=max_size,
        kwargs={
            "row_factory": dict_row,
            "autocommit": False,
            "prepare_threshold": 0,
        },
    )
    await pool.open()


async def close_pool() -> None:
    """
    Аккуратное закрытие пула. Вызывать при остановке бота.
    """
    global pool
    if pool is not None:
        await pool.close()
        pool = None


async def fetchone(sql: str, *params):
    """
    Вернёт одну строку как dict или None.
    """
    if pool is None:
        raise RuntimeError("DB pool is not initialized. Call init_pool() first.")
    async with pool.connection() as ac:
        async with ac.cursor() as cur:
            await cur.execute(sql, params)
            return await cur.fetchone()


async def fetchall(sql: str, *params):
    """
    Вернёт список dict-строк (может быть пустым).
    """
    if pool is None:
        raise RuntimeError("DB pool is not initialized. Call init_pool() first.")
    async with pool.connection() as ac:
        async with ac.cursor() as cur:
            await cur.execute(sql, params)
            return await cur.fetchall()


async def execute(sql: str, *params) -> int:
    """
    Выполнит запрос (INSERT/UPDATE/DELETE). Возвращает 1 при успехе.
    """
    if pool is None:
        raise RuntimeError("DB pool is not initialized. Call init_pool() first.")
    async with pool.connection() as ac:
        async with ac.cursor() as cur:
            await cur.execute(sql, params)
        await ac.commit()
    return 1


async def executemany(sql: str, seq_of_params) -> int:
    """
    Выполнит множественные вставки/обновления. Возвращает кол-во батчей (не строк).
    """
    if pool is None:
        raise RuntimeError("DB pool is not initialized. Call init_pool() first.")
    async with pool.connection() as ac:
        async with ac.cursor() as cur:
            await cur.executemany(sql, seq_of_params)
        await ac.commit()
    return 1


async def ping() -> bool:
    """
    Быстрая проверка соединения.
    """
    try:
        row = await fetchone("SELECT 1 AS ok")
        return bool(row and row["ok"] == 1)
    except Exception:
        return False
