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

router = Router()


PLANS = {
    "1 мес – 99₽": 99_00,
    "3 мес – 249₽": 249_00,
    "6 мес – 450₽": 450_00,
}


@router.message(MenuState.main_menu, F.text == "💎 Подписка")
async def subscription_plans(message: types.Message, state: FSMContext) -> None:
    text = (
        "Доступ к VPN после пробного периода.\n"
        "Выберите тарифный план:"
    )
    await message.answer(text, reply_markup=get_subscription_keyboard())
    await state.set_state(SubscriptionState.plans)


async def _show_payment_options(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    old_msg_id = data.get("payment_message_id")
    if old_msg_id:
        try:
            await message.bot.delete_message(message.chat.id, old_msg_id)
        except Exception as e:  # noqa: BLE001
            logging.exception("Failed to delete previous payment message: %s", e)
    await state.update_data(plan=message.text)
    sent = await message.answer(
        f"Тариф {message.text}. Выберите способ оплаты",
        reply_markup=get_payment_methods_keyboard(),
    )
    await state.update_data(payment_message_id=sent.message_id)
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
