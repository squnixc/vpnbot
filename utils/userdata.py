from datetime import datetime, timedelta
from typing import Dict, Any

from .storage import (
    get_user,
    save_user,
)

CONFIG_DURATION_MINUTES = 2


def mark_device_connected(user_id: int, device: str, config: str) -> None:
    """Store device config and update expiry."""
    info = get_user(user_id)
    expires = datetime.utcnow() + timedelta(minutes=CONFIG_DURATION_MINUTES)
    devices = info.get("devices", {})
    devices[device] = {"config": config}
    info["devices"] = devices
    info["expires_at"] = expires
    save_user(user_id, info)


def get_user_info(user_id: int) -> Dict[str, Any]:
    """Return stored info for user and ensure it is stored."""
    info = get_user(user_id)
    save_user(user_id, info)
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


def format_timedelta(td: timedelta) -> str:
    total_seconds = int(td.total_seconds())
    if total_seconds <= 0:
        return "0 секунд"
    days, rem = divmod(total_seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)
    parts = []
    if days:
        parts.append(f"{days} {plural(days, ('день','дня','дней'))}")
    if hours:
        parts.append(f"{hours} {plural(hours, ('час','часа','часов'))}")
    if minutes:
        parts.append(f"{minutes} {plural(minutes, ('минута','минуты','минут'))}")
    if seconds and not days and not hours:
        parts.append(f"{seconds} {plural(seconds, ('секунда','секунды','секунд'))}")
    return " ".join(parts)


def build_main_menu_text(user_id: int) -> str:
    info = get_user_info(user_id)
    expires = info.get("expires_at")
    if expires:
        time_left = expires - datetime.utcnow()
    else:
        time_left = timedelta(seconds=0)
    active = time_left.total_seconds() > 0
    devices = info.get("devices", {})
    if devices:
        status_lines = []
        for name in devices.keys():
            status = "Подключён" if active else "Не подключён"
            status_lines.append(f"<b>{name}</b> — {status}")
        devices_text = "\n".join(status_lines)
    else:
        devices_text = "Устройства не подключены"
    time_text = format_timedelta(time_left) if active else "0 секунд"
    return (
        "👋 <b>Вот информация о твоих устройствах и подписке</b>\n\n"
        "Здесь можно узнать какие устройства у тебя подключены и статус подписки.\n\n"
        "🧾 <b>Статус подключения:</b>\n"
        f"{devices_text}\n\n"
        f"🕒 <b>Подписка активна:</b> {time_text}\n\n"
        "🎁 <b>Бонус:</b> +7 дней за каждого приглашённого друга!"
    )
