import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "vpn_bot.db"

def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn

def init_db() -> None:
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_user_id INTEGER UNIQUE,
            is_banned INTEGER DEFAULT 0
        );
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            plan TEXT,
            status TEXT,
            expires_at TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS traffic_daily (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT,
            bytes_up INTEGER,
            bytes_down INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
        """
    )
    conn.commit()
    conn.close()
