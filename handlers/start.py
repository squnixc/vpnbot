import logging
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from keyboards.main import (
    get_intro_keyboard,
    get_main_keyboard,
    get_connect_device_keyboard,
)
from states.states import MenuState
from utils.userdata import build_main_menu_text

router = Router()


@router.message(CommandStart())
async def command_start(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get("seen_intro"):
        await message.answer(
            "🚀 Быстрый и простой VPN прямо в Telegram.\n"
            "Подключайся и забудь о блокировках!",
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
    text = build_main_menu_text(message.from_user.id)
    await message.answer(text, reply_markup=get_main_keyboard(), parse_mode="HTML")
    await message.answer("\u200b", reply_markup=get_connect_device_keyboard())
    await state.set_state(MenuState.main_menu)


@router.message(F.text == "🏠 Главное меню")
async def main_menu_button(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)
