from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from states.states import FAQState
from handlers.start import show_main_menu

router = Router()

FAQ_TEXT = (
    "❓ Что, как и почему?\n"
    "Мы собрали все частые вопросы в одной статье\n"
    "\uD83D\uDC47 Загляни в ЧаВо — там всё просто\n"
    "❓ЧаВо: https://telegra.ph/faq-01"
    "\n\n📬 Есть вопросы? Напишите нам: @support_handle"
)


@router.message(F.text == "❓ Вопросы")
async def faq_start(message: types.Message, state: FSMContext) -> None:
    await message.answer(FAQ_TEXT)
    await show_main_menu(message, state)
