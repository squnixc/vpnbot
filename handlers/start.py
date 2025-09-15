import logging
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from datetime import datetime, timedelta

from keyboards.main import (
    get_intro_keyboard,
    get_main_keyboard,
)
from states.states import MenuState
from utils.userdata import get_user_info, format_timedelta
from utils.texts import t

router = Router()


@router.message(CommandStart())
async def command_start(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get("seen_intro"):
        await message.answer(
            t("start_pitch"),
            reply_markup=get_intro_keyboard(),
        )
        await state.update_data(seen_intro=True)
        await state.set_state(MenuState.intro)
    else:
        await show_main_menu(message, state)


@router.message(MenuState.intro, F.text)
async def show_menu_after_intro(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)


async def show_main_menu(message: types.Message, state: FSMContext) -> None:
    info = get_user_info(message.from_user.id)
    devices = info.get("devices", {})
    expires = info.get("expires_at")
    time_left = (expires - datetime.utcnow()) if expires else timedelta()
    active_for = (
        format_timedelta(time_left)
        if time_left.total_seconds() > 0
        else "0 секунд"
    )
    def normalize_device_name(name: str) -> str:
        trimmed = name.lstrip()
        while trimmed and not trimmed[0].isalnum():
            trimmed = trimmed[1:].lstrip()
        return trimmed or name

    if devices:
        device_lines = "\n".join(
            f"- {normalize_device_name(device_name)}" for device_name in devices.keys()
        )
        connections_block = f"📟 Подключения:\n{device_lines}"
    else:
        connections_block = "📟 Подключения:  Нет подключений"

    status_text = t("status_text").format(
        connections_block=connections_block,
        active_for=active_for,
    )
    await message.answer(
        status_text,
        reply_markup=get_main_keyboard(),
    )
    await state.set_state(MenuState.main_menu)


@router.message(F.text == t("btn_main_menu"))
async def main_menu_button(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)


@router.callback_query(F.data == "main_menu")
async def main_menu_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    try:
        await callback.message.delete()
    except Exception as e:  # noqa: BLE001
        logging.exception("Failed to delete message: %s", e)
    await show_main_menu(callback.message, state)
