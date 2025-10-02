import logging

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from keyboards.main import get_share_keyboard
from states.states import MenuState
from utils.storage import get_user_locale
from utils.texts import get_all_translations, t

router = Router()


async def _resolve_locale(state: FSMContext, user_id: int) -> str:
    data = await state.get_data()
    locale = data.get("locale")
    if locale:
        return locale
    locale = await get_user_locale(user_id)
    await state.update_data(locale=locale)
    return locale


@router.message(MenuState.main_menu, F.text.in_(get_all_translations("btn_invite_friend")))
async def referral_start(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    bot_username = (await message.bot.get_me()).username
    ref_link = f"https://t.me/{bot_username}?start={message.from_user.id}"
    await message.answer(
        t("referral_intro", locale),
        reply_markup=get_share_keyboard(ref_link, locale),
    )
    logging.info("Referral link sent to %s", message.from_user.id)
