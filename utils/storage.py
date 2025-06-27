import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict

USERS_FILE = Path("users.json")


def _load() -> Dict[str, Any]:
    try:
        with USERS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        for info in data.values():
            if info.get("expires_at"):
                info["expires_at"] = datetime.fromisoformat(info["expires_at"])
        return data
    except Exception:
        return {}


def _save(data: Dict[str, Any]) -> None:
    serializable = {}
    for uid, info in data.items():
        ser = info.copy()
        if ser.get("expires_at"):
            ser["expires_at"] = ser["expires_at"].isoformat()
        serializable[uid] = ser
    with USERS_FILE.open("w", encoding="utf-8") as f:
        json.dump(serializable, f, ensure_ascii=False, indent=2)


def get_user(user_id: int) -> Dict[str, Any]:
    data = _load()
    uid = str(user_id)
    return data.get(
        uid,
        {
            "phone": False,
            "computer": False,
            "expires_at": None,
            "peers": 0,
            "banned": False,
        },
    )


def save_user(user_id: int, info: Dict[str, Any]) -> None:
    data = _load()
    data[str(user_id)] = info
    _save(data)


def increment_peers(user_id: int) -> None:
    info = get_user(user_id)
    info["peers"] = info.get("peers", 0) + 1
    save_user(user_id, info)


def peers_count(user_id: int) -> int:
    return get_user(user_id).get("peers", 0)


def ban_user(user_id: int) -> None:
    info = get_user(user_id)
    info["banned"] = True
    save_user(user_id, info)


def unban_user(user_id: int) -> None:
    info = get_user(user_id)
    info["banned"] = False
    save_user(user_id, info)


def is_banned(user_id: int) -> bool:
    return get_user(user_id).get("banned", False)


def update_expiration(user_id: int, minutes: int) -> None:
    info = get_user(user_id)
    info["expires_at"] = datetime.utcnow() + timedelta(minutes=minutes)
    save_user(user_id, info)


def all_user_ids() -> list[int]:
    """Return list of all known user IDs."""
    data = _load()
    return [int(uid) for uid in data.keys()]
