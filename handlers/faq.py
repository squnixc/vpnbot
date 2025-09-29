from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from states.states import FAQState, MenuState
from keyboards.main import get_main_keyboard
from utils.texts import t

router = Router()

FAQ_URL = "https://telegra.ph/faq-01"
SUPPORT_HANDLE = "support_handle"


@router.message(F.text == t("btn_questions"))
async def faq_start(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        t("faq_title")
        + "\n"
        + t("faq_body").format(
            faq_url=FAQ_URL,
            support_handle=SUPPORT_HANDLE,
            tg_id=message.from_user.id,
        ),
        reply_markup=get_main_keyboard(),
    )
    await state.set_state(MenuState.main_menu)
