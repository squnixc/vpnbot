from datetime import datetime, timedelta
from typing import Dict, Any

CONFIG_DURATION_MINUTES = 2

_user_data: Dict[int, Dict[str, Any]] = {}


def mark_device_connected(user_id: int, device: str) -> None:
    """Mark device as connected and update expiry."""
    expires = datetime.utcnow() + timedelta(minutes=CONFIG_DURATION_MINUTES)
    info = _user_data.setdefault(user_id, {"phone": False, "computer": False, "expires_at": expires})
    info[device] = True
    info["expires_at"] = expires


def get_user_info(user_id: int) -> Dict[str, Any]:
    """Return stored info for user."""
    return _user_data.get(user_id, {"phone": False, "computer": False, "expires_at": None})

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
    phone_status = "Подключён" if info.get("phone") and active else "Не подключён"
    pc_status = "Подключён" if info.get("computer") and active else "Не подключён"
    time_text = format_timedelta(time_left) if active else "0 секунд"
    return (
        "👋 <b>Вот информация о твоих устройствах и подписке</b>\n\n"
        "Здесь можно узнать какие устройства у тебя подключены и статус подписки."\n\n"
        "🧾 <b>Статус подключения:</b>\n"
        f"<b>Телефон</b> — {phone_status}\n"
        f"<b>Компьютер</b> — {pc_status}\n\n"
        f"🕒 <b>Подписка активна:</b> {time_text}\n"
        "🎁 <b>Бонус:</b> +7 дней за каждого приглашённого друга!"
    )
