from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from keyboards.main import get_main_keyboard
from states.states import MenuState
from utils.storage import get_user_locale
from utils.texts import get_all_translations, t

router = Router()

FAQ_URL = "https://telegra.ph/faq-01"
SUPPORT_HANDLE = "support_handle"


async def _resolve_locale(state: FSMContext, user_id: int) -> str:
    data = await state.get_data()
    locale = data.get("locale")
    if locale:
        return locale
    locale = await get_user_locale(user_id)
    await state.update_data(locale=locale)
    return locale


@router.message(F.text.in_(get_all_translations("btn_questions")))
async def faq_start(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    body = t("faq_body", locale).format(
        faq_url=FAQ_URL,
        support_handle=SUPPORT_HANDLE,
        tg_id=message.from_user.id,
    )
    await message.answer(
        t("faq_title", locale) + "\n" + body,
        reply_markup=get_main_keyboard(locale),
    )
    await state.set_state(MenuState.main_menu)
