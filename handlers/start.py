import logging
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from keyboards.main import get_intro_keyboard, get_main_keyboard
from states.states import MenuState

router = Router()


@router.message(CommandStart())
async def command_start(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get("seen_intro"):
        await message.answer(
            "Добро пожаловать в VPN бот!", reply_markup=get_intro_keyboard()
        )
        await state.update_data(seen_intro=True)
        await state.set_state(MenuState.intro)
    else:
        await show_main_menu(message, state)


@router.message(MenuState.intro, F.text)
async def show_menu_after_intro(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)


async def show_main_menu(message: types.Message, state: FSMContext) -> None:
    await message.answer("Главное меню", reply_markup=get_main_keyboard())
    await state.set_state(MenuState.main_menu)
