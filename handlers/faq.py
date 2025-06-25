from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from states.states import FAQState, MenuState
from keyboards.main import get_main_keyboard

router = Router()

FAQ_TEXT = (
    "❓ Что, как и почему?\n"
    "Мы собрали все частые вопросы в одной статье\n"
    "👇 Загляни в ЧаВо — там всё просто\n"
    "❓ЧаВо: https://telegra.ph/faq-01"
    "\n\n📬 Есть вопросы? Напишите нам: @support_handle"
)


@router.message(F.text == "❓ Вопросы")
async def faq_start(message: types.Message, state: FSMContext) -> None:
    await message.answer(FAQ_TEXT, reply_markup=get_main_keyboard())
    await state.set_state(MenuState.main_menu)
