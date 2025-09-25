import logging
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from keyboards.main import (
    get_main_keyboard,
    get_subscription_plan_keyboard,
    get_subscription_duration_keyboard,
    get_payment_methods_keyboard,
)
from handlers.start import show_main_menu
from states.states import MenuState, SubscriptionState
from utils.texts import t

router = Router()


PLANS = {
    "devices_2": {
        "button": "💷Устройства: 2 - 99₽/мес.",
        "title": "Устройства: 2",
        "durations": {
            "1 месяц - 99₽": 99_00,
            "🔹3 месяца - 249₽": 249_00,
            "🔸6 месяцев - 399₽": 399_00,
        },
    },
    "devices_5": {
        "button": "💴Устройства: 5 - 169₽/мес.",
        "title": "Устройства: 5",
        "durations": {
            "1 месяц - 169₽": 169_00,
            "🔹3 месяца - 449₽": 449_00,
            "🔸6 месяцев - 749₽": 749_00,
        },
    },
}

PLAN_BY_BUTTON = {config["button"]: key for key, config in PLANS.items()}
ALL_PLAN_BUTTONS = tuple(PLAN_BY_BUTTON.keys())
ALL_DURATION_BUTTONS = tuple(
    duration
    for config in PLANS.values()
    for duration in config["durations"].keys()
)


async def _send_plan_intro(message: types.Message, state: FSMContext) -> None:
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

    await state.update_data(
        payment_message_id=None,
        plan_key=None,
        plan_title=None,
        duration=None,
        price=None,
    )
    await message.answer(
        t("subscription_intro"),
        reply_markup=get_subscription_plan_keyboard(),
    )
    await state.set_state(SubscriptionState.plan_type)


@router.message(MenuState.main_menu, F.text == t("btn_subscription"))
async def subscription_plans(message: types.Message, state: FSMContext) -> None:
    await _send_plan_intro(message, state)


async def _show_payment_options(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    plan_key = data.get("plan_key")
    if not plan_key:
        await _send_plan_intro(message, state)
        return

    plan_config = PLANS.get(plan_key, {})
    duration_price = plan_config.get("durations", {}).get(message.text)
    if duration_price is None:
        await message.answer("Пожалуйста, выбери один из предложенных тарифов.")
        return

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

    sent = await message.answer(
        "🫶Спасибо за доверие!\n\n"
        "Ты на шаг ближе к свободному, безопасному и быстрому интернету — без ограничений.\n"
        "Мы постарались сделать процесс максимально удобным.\n\n"
        "👇Выбери подходящий способ оплаты:",
        reply_markup=get_payment_methods_keyboard(),
    )
    await state.update_data(
        payment_message_id=sent.message_id,
        duration=message.text,
        price=duration_price,
    )
    await state.set_state(SubscriptionState.payment_method)


@router.message(SubscriptionState.plan_type, F.text.in_(ALL_PLAN_BUTTONS))
async def choose_plan_type(message: types.Message, state: FSMContext) -> None:
    plan_key = PLAN_BY_BUTTON.get(message.text)
    if not plan_key:
        await message.answer("Выберите один из доступных планов.")
        return

    plan_config = PLANS[plan_key]
    duration_lines = "\n".join(plan_config["durations"].keys())
    await state.update_data(
        plan_key=plan_key,
        plan_title=plan_config["title"],
        duration=None,
        price=None,
    )
    await message.answer(
        "Выбери срок подписки:\n"
        f"{duration_lines}\n"
        f"(для плана {plan_config['title']})",
        reply_markup=get_subscription_duration_keyboard(plan_key),
    )
    await state.set_state(SubscriptionState.duration)


@router.message(SubscriptionState.duration, F.text.in_(ALL_DURATION_BUTTONS))
async def choose_duration(message: types.Message, state: FSMContext) -> None:
    await _show_payment_options(message, state)


@router.message(SubscriptionState.payment_method, F.text.in_(ALL_DURATION_BUTTONS))
async def change_duration(message: types.Message, state: FSMContext) -> None:
    await _show_payment_options(message, state)


@router.callback_query(SubscriptionState.payment_method, F.data == "pay_card")
async def process_payment(call: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    plan_key = data.get("plan_key")
    plan_config = PLANS.get(plan_key, {})
    plan_title = plan_config.get("title", plan_key)
    duration = data.get("duration")
    price = data.get("price", 0)
    await call.message.answer(
        "Оплата создана (мок)", reply_markup=get_main_keyboard()
    )
    # TODO: send real invoice via BotFather payments
    await state.set_state(MenuState.main_menu)
    logging.info(
        "User %s started payment for %s (%s) — %s",
        call.from_user.id,
        plan_title,
        duration,
        price,
    )



@router.message(SubscriptionState.payment_method, F.text == "⬅️ Назад")
async def payment_back(message: types.Message, state: FSMContext) -> None:
    await _send_plan_intro(message, state)


@router.message(SubscriptionState.duration, F.text == "⬅️ Назад")
async def duration_back(message: types.Message, state: FSMContext) -> None:
    await _send_plan_intro(message, state)


@router.message(SubscriptionState.plan_type, F.text == "⬅️ Назад")
async def plan_back(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)
