import logging
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from keyboards.main import get_share_keyboard
from states.states import MenuState, ReferralState
from handlers.start import show_main_menu

router = Router()


@router.message(MenuState.main_menu, F.text == "🤝 Пригласить друга")
async def referral_start(message: types.Message, state: FSMContext) -> None:
    bot_username = (await message.bot.get_me()).username
    ref_link = f"https://t.me/{bot_username}?start={message.from_user.id}"
    await message.answer(
        "Поделитесь ссылкой с другом:",
        reply_markup=get_share_keyboard(ref_link),
    )
    await state.set_state(ReferralState.waiting_for_share)
    logging.info("Referral link sent to %s", message.from_user.id)


@router.message(ReferralState.waiting_for_share, F.text)
async def referral_back(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)
