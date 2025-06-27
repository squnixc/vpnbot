import os
import logging
from aiogram import Router, types
from aiogram.filters import Command

from config import config
from keyboards.admin import get_admin_keyboard
from utils.storage import ban_user, unban_user, get_user

router = Router()


def _is_admin(user_id: int) -> bool:
    return user_id == config.admin_id


@router.message(Command("admin"))
async def admin_start(message: types.Message) -> None:
    if not _is_admin(message.from_user.id):
        return
    parts = message.text.split(maxsplit=1)
    if len(parts) == 2 and parts[1] == config.admin_key:
        await message.answer(
            "Админ режим активирован", reply_markup=get_admin_keyboard()
        )
    else:
        await message.answer("Неверный ключ")


@router.message(Command("ban"))
async def cmd_ban(message: types.Message) -> None:
    if not _is_admin(message.from_user.id):
        return
    try:
        uid = int(message.text.split()[1])
    except Exception:
        await message.answer("Usage: /ban <user_id>")
        return
    ban_user(uid)
    await message.answer(f"User {uid} banned")


@router.message(Command("unban"))
async def cmd_unban(message: types.Message) -> None:
    if not _is_admin(message.from_user.id):
        return
    try:
        uid = int(message.text.split()[1])
    except Exception:
        await message.answer("Usage: /unban <user_id>")
        return
    unban_user(uid)
    await message.answer(f"User {uid} unbanned")


@router.message(Command("devices"))
async def cmd_devices(message: types.Message) -> None:
    if not _is_admin(message.from_user.id):
        return
    try:
        uid = int(message.text.split()[1])
    except Exception:
        await message.answer("Usage: /devices <user_id>")
        return
    info = get_user(uid)
    await message.answer(str(info))
