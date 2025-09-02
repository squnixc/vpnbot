import os
import logging
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config import config
from keyboards.admin import (
    get_admin_main_keyboard,
    get_admin_panel_keyboard,
    get_about_keyboard,
    get_send_keyboard,
    get_gift_keyboard,
    get_manage_keyboard,
    get_config_keyboard,
)
from utils.storage import (
    ban_user,
    unban_user,
    get_user,
    all_user_ids,
    update_expiration,
)
from states.states import AdminState
from handlers.start import show_main_menu
from utils.file import create_temp_conf_file
from vpn.wireguard import generate_peer

router = Router()


def _is_admin(user_id: int) -> bool:
    return user_id == config.admin_id


@router.message(Command("admin"))
async def admin_start(message: types.Message, state: FSMContext) -> None:
    if not _is_admin(message.from_user.id):
        return
    parts = message.text.split(maxsplit=1)
    if len(parts) == 2 and parts[1] == config.admin_key:
        await message.answer(
            "Админ режим активирован", reply_markup=get_admin_main_keyboard()
        )
        await state.set_state(AdminState.main)
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


async def _show_admin_main(message: types.Message, state: FSMContext) -> None:
    await message.answer("Выберите действие:", reply_markup=get_admin_main_keyboard())
    await state.set_state(AdminState.main)


@router.message(AdminState.main, Command("admin_panel"))
@router.message(AdminState.main, lambda m: m.text == "/admin_panel")
async def show_panel(message: types.Message, state: FSMContext) -> None:
    await message.answer("Админ панель", reply_markup=get_admin_panel_keyboard())
    await state.set_state(AdminState.panel)


@router.message(AdminState.main, Command("about"))
@router.message(AdminState.main, lambda m: m.text == "/about")
async def show_about(message: types.Message, state: FSMContext) -> None:
    await message.answer("О боте", reply_markup=get_about_keyboard())
    await state.set_state(AdminState.about)


@router.message(AdminState.main, Command("manage"))
@router.message(AdminState.main, lambda m: m.text == "/manage")
async def show_manage(message: types.Message, state: FSMContext) -> None:
    await message.answer("Управление", reply_markup=get_manage_keyboard())
    await state.set_state(AdminState.manage)


@router.message(AdminState.main, Command("main_menu"))
@router.message(AdminState.main, lambda m: m.text == "/main_menu")
async def leave_admin(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)


@router.message(AdminState.panel, Command("back"))
@router.message(AdminState.panel, lambda m: m.text == "/back")
async def panel_back(message: types.Message, state: FSMContext) -> None:
    await _show_admin_main(message, state)


@router.message(AdminState.about, Command("back"))
@router.message(AdminState.about, lambda m: m.text == "/back")
async def about_back(message: types.Message, state: FSMContext) -> None:
    await _show_admin_main(message, state)


@router.message(AdminState.manage, Command("back"))
@router.message(AdminState.manage, lambda m: m.text == "/back")
async def manage_back(message: types.Message, state: FSMContext) -> None:
    await _show_admin_main(message, state)


@router.message(AdminState.about, Command("send"))
@router.message(AdminState.about, lambda m: m.text == "/send")
async def about_send(message: types.Message, state: FSMContext) -> None:
    await message.answer("Отправить сообщение", reply_markup=get_send_keyboard())
    await state.set_state(AdminState.send)


@router.message(AdminState.about, Command("gift"))
@router.message(AdminState.about, lambda m: m.text == "/gift")
async def about_gift(message: types.Message, state: FSMContext) -> None:
    await message.answer("Выдать подарок", reply_markup=get_gift_keyboard())
    await state.set_state(AdminState.gift)


@router.message(AdminState.about, Command("config"))
@router.message(AdminState.about, lambda m: m.text == "/config")
async def about_config(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        "Выдать конфиг. Введите Telegram ID пользователя:",
        reply_markup=get_config_keyboard(),
    )
    await state.set_state(AdminState.config)


@router.message(AdminState.send, Command("back"))
@router.message(AdminState.send, lambda m: m.text == "/back")
async def send_back(message: types.Message, state: FSMContext) -> None:
    # Return to the "about" menu when leaving the sending section
    await show_about(message, state)


@router.message(AdminState.gift, Command("back"))
@router.message(AdminState.gift, lambda m: m.text == "/back")
async def gift_back(message: types.Message, state: FSMContext) -> None:
    # Return to the "about" menu when leaving the gifting section
    await show_about(message, state)


@router.message(AdminState.config, Command("back"))
@router.message(AdminState.config, lambda m: m.text == "/back")
async def config_back(message: types.Message, state: FSMContext) -> None:
    # Return to the "about" menu when leaving the config section
    await show_about(message, state)


@router.message(AdminState.send, Command("to_one"))
async def send_to_one(message: types.Message) -> None:
    if not _is_admin(message.from_user.id):
        return
    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        await message.answer("Usage: /to_one <user_id> <text>")
        return
    try:
        uid = int(parts[1])
    except Exception:
        await message.answer("Invalid user id")
        return
    await message.bot.send_message(uid, parts[2])
    await message.answer("Message sent")


@router.message(AdminState.send, Command("to_all"))
async def send_to_all(message: types.Message) -> None:
    if not _is_admin(message.from_user.id):
        return
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.answer("Usage: /to_all <text>")
        return
    for uid in all_user_ids():
        try:
            await message.bot.send_message(uid, parts[1])
        except Exception:
            pass
    await message.answer("Message sent to all users")


@router.message(AdminState.gift, Command("to_one"))
async def gift_to_one(message: types.Message) -> None:
    if not _is_admin(message.from_user.id):
        return
    parts = message.text.split()
    if len(parts) != 3:
        await message.answer("Usage: /to_one <user_id> <minutes>")
        return
    try:
        uid = int(parts[1])
        mins = int(parts[2])
    except Exception:
        await message.answer("Invalid arguments")
        return
    update_expiration(uid, mins)
    await message.answer("Gift applied")


@router.message(AdminState.gift, Command("to_all"))
async def gift_to_all(message: types.Message) -> None:
    if not _is_admin(message.from_user.id):
        return
    parts = message.text.split(maxsplit=1)
    if len(parts) != 2:
        await message.answer("Usage: /to_all <minutes>")
        return
    try:
        mins = int(parts[1])
    except Exception:
        await message.answer("Invalid minutes")
        return
    for uid in all_user_ids():
        update_expiration(uid, mins)
    await message.answer("Gift applied to all users")


@router.message(AdminState.config)
async def send_config(message: types.Message, state: FSMContext) -> None:
    if not _is_admin(message.from_user.id):
        return
    try:
        uid = int(message.text.strip())
    except Exception:
        await message.answer("Введите корректный ID пользователя")
        return
    try:
        cfg = generate_peer(uid)
    except Exception as exc:
        await message.answer(str(exc))
        await show_about(message, state)
        return
    conf_file = create_temp_conf_file(cfg)
    await message.bot.send_message(uid, "Вам выдан конфиг")
    await message.bot.send_document(uid, types.FSInputFile(conf_file))
    await message.answer("Конфиг отправлен")
    await show_about(message, state)
