-- Apply manually via psql: \i schema_pg.sql

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

CREATE TABLE IF NOT EXISTS subscriptions (
  id         BIGSERIAL PRIMARY KEY,
  user_id    BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  plan       TEXT NOT NULL,
  status     TEXT NOT NULL,
  started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  expires_at TIMESTAMPTZ NOT NULL,
  source     TEXT
);
CREATE INDEX IF NOT EXISTS ix_sub_user ON subscriptions(user_id);
CREATE INDEX IF NOT EXISTS ix_sub_active ON subscriptions(user_id,status,expires_at);

CREATE TABLE IF NOT EXISTS devices (
  id               BIGSERIAL PRIMARY KEY,
  user_id          BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  label            TEXT,
  platform         TEXT,
  type             TEXT,
  config_id        TEXT,
  public_key       TEXT,
  created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  revoked_at       TIMESTAMPTZ,
  status           TEXT NOT NULL DEFAULT 'active',
  last_handshake_at TIMESTAMPTZ,
  bytes_up         BIGINT NOT NULL DEFAULT 0,
  bytes_down       BIGINT NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS ix_dev_user ON devices(user_id);
CREATE INDEX IF NOT EXISTS ix_dev_active ON devices(user_id,status);

CREATE TABLE IF NOT EXISTS traffic_daily (
  id         BIGSERIAL PRIMARY KEY,
  user_id    BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  device_id  BIGINT REFERENCES devices(id) ON DELETE SET NULL,
  date       DATE NOT NULL,
  bytes_up   BIGINT NOT NULL DEFAULT 0,
  bytes_down BIGINT NOT NULL DEFAULT 0,
  UNIQUE(user_id, device_id, date)
);
CREATE INDEX IF NOT EXISTS ix_traffic_date ON traffic_daily(date);
