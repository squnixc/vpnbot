"""Helpers for storing bot data in PostgreSQL."""

from __future__ import annotations

import datetime as dt
from typing import Any, Dict, List

from db import execute, fetchall, fetchone


async def _ensure_user_record(tg_user_id: int) -> int:
    """Return internal DB id for Telegram user, creating the record if needed."""

    row = await fetchone("SELECT id FROM users WHERE tg_user_id=%s", tg_user_id)
    if row:
        return row["id"]

    await execute(
        "INSERT INTO users (tg_user_id) VALUES (%s) ON CONFLICT (tg_user_id) DO NOTHING",
        tg_user_id,
    )

    row = await fetchone("SELECT id FROM users WHERE tg_user_id=%s", tg_user_id)
    if not row:
        raise RuntimeError("Failed to ensure users record")
    return row["id"]


async def touch_user(tg_user_id: int) -> None:
    """Update last seen timestamp for the user."""

    user_id = await _ensure_user_record(tg_user_id)
    await execute("UPDATE users SET last_seen_at=NOW() WHERE id=%s", user_id)


async def get_user(tg_user_id: int) -> Dict[str, Any]:
    """Fetch aggregated user info used across the bot."""

    user_id = await _ensure_user_record(tg_user_id)

    user_row = await fetchone("SELECT is_banned FROM users WHERE id=%s", user_id)

    devices_rows = await fetchall(
        """
        SELECT label, config_id
        FROM devices
        WHERE user_id=%s AND status='active'
        ORDER BY created_at
        """,
        user_id,
    )

    devices: Dict[str, Dict[str, str]] = {}
    for idx, row in enumerate(devices_rows, start=1):
        label = row.get("label") or f"Устройство {idx}"
        devices[label] = {"config": row.get("config_id") or ""}

    sub_row = await fetchone(
        """
        SELECT id, expires_at
        FROM subscriptions
        WHERE user_id=%s AND status='active'
        ORDER BY expires_at DESC
        LIMIT 1
        """,
        user_id,
    )

    expires_at = None
    if sub_row and sub_row.get("expires_at"):
        expires_at = sub_row["expires_at"]
        if expires_at.tzinfo is not None:
            expires_at = expires_at.astimezone(dt.timezone.utc).replace(tzinfo=None)

    return {
        "devices": devices,
        "expires_at": expires_at,
        "peers": len(devices_rows),
        "banned": bool(user_row and user_row.get("is_banned")),
    }


async def save_device_config(tg_user_id: int, label: str, config: str) -> None:
    """Store or update WireGuard config for the device."""

    user_id = await _ensure_user_record(tg_user_id)
    row = await fetchone(
        """
        SELECT id
        FROM devices
        WHERE user_id=%s AND label=%s AND status='active'
        ORDER BY created_at DESC
        LIMIT 1
        """,
        user_id,
        label,
    )

    if row:
        await execute("UPDATE devices SET config_id=%s WHERE id=%s", config, row["id"])
    else:
        await execute(
            "INSERT INTO devices (user_id, label, config_id, status) VALUES (%s,%s,%s,%s)",
            user_id,
            label,
            config,
            "active",
        )


async def peers_count(tg_user_id: int) -> int:
    """Return number of active devices linked to the user."""

    user_id = await _ensure_user_record(tg_user_id)
    row = await fetchone(
        "SELECT COUNT(*) AS cnt FROM devices WHERE user_id=%s AND status='active'",
        user_id,
    )
    return int(row["cnt"]) if row else 0


async def update_expiration(tg_user_id: int, minutes: int) -> None:
    """Extend or create a subscription record for the user."""

    user_id = await _ensure_user_record(tg_user_id)
    new_expires = dt.datetime.now(dt.timezone.utc) + dt.timedelta(minutes=minutes)

    sub_row = await fetchone(
        """
        SELECT id
        FROM subscriptions
        WHERE user_id=%s AND status='active'
        ORDER BY expires_at DESC
        LIMIT 1
        """,
        user_id,
    )

    if sub_row:
        await execute("UPDATE subscriptions SET expires_at=%s WHERE id=%s", new_expires, sub_row["id"])
    else:
        await execute(
            "INSERT INTO subscriptions (user_id, plan, status, expires_at) VALUES (%s,%s,%s,%s)",
            user_id,
            "trial",
            "active",
            new_expires,
        )


async def set_ban_status(tg_user_id: int, banned: bool) -> None:
    """Update ban flag for the user."""

    user_id = await _ensure_user_record(tg_user_id)
    await execute("UPDATE users SET is_banned=%s WHERE id=%s", banned, user_id)


async def is_banned(tg_user_id: int) -> bool:
    """Return ban status for the user."""

    row = await fetchone("SELECT is_banned FROM users WHERE tg_user_id=%s", tg_user_id)
    return bool(row and row.get("is_banned"))


async def all_user_ids(banned: bool | None = None) -> List[int]:
    """Return Telegram IDs of all users, optionally filtering by ban status."""

    if banned is None:
        rows = await fetchall("SELECT tg_user_id FROM users ORDER BY tg_user_id")
    else:
        rows = await fetchall(
            "SELECT tg_user_id FROM users WHERE is_banned=%s ORDER BY tg_user_id",
            banned,
        )
    return [int(row["tg_user_id"]) for row in rows]
