import json
import logging
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import LabeledPrice

from keyboards.main import (
    get_main_keyboard,
    get_subscription_keyboard,
    get_payment_methods_keyboard,
)
from handlers.start import show_main_menu
from states.states import MenuState, SubscriptionState
from utils.texts import t

router = Router()


PLANS = {
    "1 месяц - 99₽": 99_00,
    "🔹3 месяца - 249₽": 249_00,
    "🔸6 месяцев - 450₽": 450_00,
}


@router.message(MenuState.main_menu, F.text == t("btn_subscription"))
async def subscription_plans(message: types.Message, state: FSMContext) -> None:
    await message.answer(t("sub_title"))
    await message.answer(t("sub_list"))
    await message.answer(t("sub_footer"), reply_markup=get_subscription_keyboard())
    await state.set_state(SubscriptionState.plans)


async def _show_payment_options(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    old_msg_id = data.get("payment_message_id")
    if old_msg_id:
        try:
            await message.bot.delete_message(
                chat_id=message.chat.id,
                message_id=old_msg_id,
                revoke=True,
            )
        except Exception as e:  # noqa: BLE001
            logging.exception("Failed to delete previous payment message: %s", e)

    old_plan_msg_id = data.get("plan_message_id")
    if old_plan_msg_id:
        try:
            await message.bot.delete_message(
                chat_id=message.chat.id,
                message_id=old_plan_msg_id,
                revoke=True,
            )
        except Exception as e:  # noqa: BLE001
            logging.exception("Failed to delete previous plan message: %s", e)
    await state.update_data(plan=message.text)
    sent = await message.answer(
        "🫶Спасибо за доверие!\n\n"
        "Ты на шаг ближе к свободному, безопасному и быстрому интернету — без ограничений.\n"
        "Мы постарались сделать процесс максимально удобным.\n\n"
        "👇Выбери подходящий способ оплаты:",
        reply_markup=get_payment_methods_keyboard(),
    )
    await state.update_data(
        payment_message_id=sent.message_id, plan_message_id=message.message_id
    )
    await state.set_state(SubscriptionState.payment_method)


@router.message(SubscriptionState.plans, F.text.in_(list(PLANS.keys())))
async def choose_plan(message: types.Message, state: FSMContext) -> None:
    await _show_payment_options(message, state)


@router.message(SubscriptionState.payment_method, F.text.in_(list(PLANS.keys())))
async def change_plan(message: types.Message, state: FSMContext) -> None:
    await _show_payment_options(message, state)


@router.callback_query(SubscriptionState.payment_method, F.data == "pay_card")
async def process_payment(call: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    plan = data.get("plan")
    price = PLANS.get(plan, 0)
    await call.message.answer(
        "Оплата создана (мок)", reply_markup=get_main_keyboard()
    )
    # TODO: send real invoice via BotFather payments
    await state.set_state(MenuState.main_menu)
    logging.info("User %s started payment %s", call.from_user.id, plan)



@router.message(SubscriptionState.payment_method, F.text == "⬅️ Назад")
async def payment_back(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)


@router.message(SubscriptionState.plans, F.text == "⬅️ Назад")
async def plan_back(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)
