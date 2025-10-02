from datetime import timedelta
from typing import Any, Dict

from .plans import get_plan_limit
from .storage import (
    get_user,
    save_device_config,
    touch_user,
    update_expiration,
)
from .texts import t

CONFIG_DURATION_MINUTES = 2


async def mark_device_connected(user_id: int, device: str, config: str) -> None:
    """Store device config and update expiry."""

    await save_device_config(user_id, device, config)
    await update_expiration(user_id, CONFIG_DURATION_MINUTES)


async def get_user_info(user_id: int) -> Dict[str, Any]:
    """Return stored info for user and ensure it is stored."""

    info = await get_user(user_id)
    await touch_user(user_id)
    return info


def plural(value: int, forms: tuple[str, str, str]) -> str:
    value = abs(value) % 100
    if 10 < value < 20:
        return forms[2]
    if value % 10 == 1:
        return forms[0]
    if 2 <= value % 10 <= 4:
        return forms[1]
    return forms[2]


def _get_forms(key: str, locale: str | None) -> tuple[str, str, str]:
    value = t(key, locale)
    parts = value.split("|")
    if len(parts) == 3:
        return tuple(parts)  # type: ignore[return-value]
    return (value, value, value)


def format_timedelta(td: timedelta, locale: str | None = None) -> str:
    total_seconds = int(td.total_seconds())
    if total_seconds <= 0:
        return t("time_zero", locale)
    days, rem = divmod(total_seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)
    parts = []
    if days:
        parts.append(f"{days} {plural(days, _get_forms('time_day_forms', locale))}")
    if hours:
        parts.append(f"{hours} {plural(hours, _get_forms('time_hour_forms', locale))}")
    if minutes:
        parts.append(f"{minutes} {plural(minutes, _get_forms('time_minute_forms', locale))}")
    if seconds and not days and not hours:
        parts.append(f"{seconds} {plural(seconds, _get_forms('time_second_forms', locale))}")
    return " ".join(parts)
