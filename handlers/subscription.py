import logging
from typing import Dict

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from handlers.start import show_main_menu
from keyboards.main import (
    get_main_keyboard,
    get_payment_methods_keyboard,
    get_payment_navigation_keyboard,
    get_subscription_duration_keyboard,
    get_subscription_plan_keyboard,
)
from states.states import MenuState, SubscriptionState
from utils.storage import get_user_locale
from utils.subscription_plans import SUBSCRIPTION_PLANS
from utils.texts import get_all_translations, t

router = Router()


def _prepare_plan_mappings() -> tuple[Dict[str, str], Dict[str, Dict[str, str]], Dict[str, Dict[str, int]]]:
    plan_by_button: Dict[str, str] = {}
    duration_by_text: Dict[str, Dict[str, str]] = {}
    prices: Dict[str, Dict[str, int]] = {}
    for plan_key, config in SUBSCRIPTION_PLANS.items():
        button_key = config["button_key"]
        for text in get_all_translations(button_key):
            plan_by_button[text] = plan_key
        duration_mapping: Dict[str, str] = {}
        price_mapping: Dict[str, int] = {}
        for duration_key, price in config["durations"]:  # type: ignore[index]
            for text in get_all_translations(duration_key):
                duration_mapping[text] = duration_key
            price_mapping[duration_key] = price
        duration_by_text[plan_key] = duration_mapping
        prices[plan_key] = price_mapping
    return plan_by_button, duration_by_text, prices


PLAN_BY_BUTTON, DURATION_BY_TEXT, DURATION_PRICES = _prepare_plan_mappings()
ALL_PLAN_BUTTONS = tuple(PLAN_BY_BUTTON.keys())
ALL_DURATION_BUTTONS = tuple(
    text for mapping in DURATION_BY_TEXT.values() for text in mapping.keys()
)
BACK_BUTTONS = tuple(get_all_translations("btn_back"))


async def _resolve_locale(state: FSMContext, user_id: int) -> str:
    data = await state.get_data()
    locale = data.get("locale")
    if locale:
        return locale
    locale = await get_user_locale(user_id)
    await state.update_data(locale=locale)
    return locale


async def _delete_payment_message(message: types.Message, data: dict) -> None:
    old_msg_id = data.get("payment_message_id")
    if not old_msg_id:
        return

    try:
        await message.bot.delete_message(
            chat_id=message.chat.id,
            message_id=old_msg_id,
            revoke=True,
        )
    except Exception as exc:  # noqa: BLE001
        logging.exception("Failed to delete previous payment message: %s", exc)


async def _send_plan_intro(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    data = await state.get_data()
    await _delete_payment_message(message, data)
    await state.update_data(
        payment_message_id=None,
        plan_key=None,
        plan_title_key=None,
        duration_key=None,
        price=None,
    )
    await message.answer(
        t("subscription_intro", locale),
        reply_markup=get_subscription_plan_keyboard(locale),
    )
    await state.set_state(SubscriptionState.plan_type)


@router.message(MenuState.main_menu, F.text.in_(get_all_translations("btn_subscription")))
async def subscription_plans(message: types.Message, state: FSMContext) -> None:
    await _send_plan_intro(message, state)


async def _show_duration_selection(
    message: types.Message, state: FSMContext, plan_key: str
) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    plan_config = SUBSCRIPTION_PLANS.get(plan_key)
    if not plan_config:
        await _send_plan_intro(message, state)
        return

    duration_keys = [duration_key for duration_key, _ in plan_config["durations"]]  # type: ignore[index]
    duration_labels = [t(key, locale) for key in duration_keys]
    options_line = "  / ".join(duration_labels)
    prompt = t("subscription_duration_prompt", locale).format(options=options_line)
    hint = t("subscription_duration_hint", locale)
    await message.answer(
        prompt + "\n\n" + hint,
        reply_markup=get_subscription_duration_keyboard(plan_key, locale),
    )
    await state.set_state(SubscriptionState.duration)


async def _show_payment_options(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    data = await state.get_data()
    plan_key = data.get("plan_key")
    if not plan_key:
        await _send_plan_intro(message, state)
        return

    duration_mapping = DURATION_BY_TEXT.get(plan_key, {})
    duration_key = duration_mapping.get(message.text)
    if not duration_key:
        await message.answer(t("subscription_invalid_duration", locale))
        return

    duration_price = DURATION_PRICES.get(plan_key, {}).get(duration_key)
    if duration_price is None:
        await message.answer(t("subscription_invalid_duration", locale))
        return

    await _delete_payment_message(message, data)

    sent = await message.answer(
        t("subscription_payment_thanks", locale),
        reply_markup=get_payment_methods_keyboard(locale),
    )
    await message.answer(
        t("subscription_payment_change", locale),
        reply_markup=get_payment_navigation_keyboard(locale),
    )
    await state.update_data(
        payment_message_id=sent.message_id,
        duration_key=duration_key,
        price=duration_price,
    )
    await state.set_state(SubscriptionState.payment_method)


@router.message(SubscriptionState.plan_type, F.text.in_(ALL_PLAN_BUTTONS))
async def choose_plan_type(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    plan_key = PLAN_BY_BUTTON.get(message.text)
    if not plan_key:
        await message.answer(t("subscription_invalid_plan", locale))
        return

    plan_config = SUBSCRIPTION_PLANS[plan_key]
    await state.update_data(
        plan_key=plan_key,
        plan_title_key=plan_config["title_key"],
        duration_key=None,
        price=None,
    )
    await _show_duration_selection(message, state, plan_key)


@router.message(SubscriptionState.duration, F.text.in_(ALL_DURATION_BUTTONS))
async def choose_duration(message: types.Message, state: FSMContext) -> None:
    await _show_payment_options(message, state)


@router.message(SubscriptionState.payment_method, F.text.in_(ALL_DURATION_BUTTONS))
async def change_duration(message: types.Message, state: FSMContext) -> None:
    await _show_payment_options(message, state)


@router.callback_query(SubscriptionState.payment_method, F.data == "pay_card")
async def process_payment(call: types.CallbackQuery, state: FSMContext) -> None:
    locale = await _resolve_locale(state, call.from_user.id)
    data = await state.get_data()
    plan_key = data.get("plan_key")
    plan_title_key = data.get("plan_title_key")
    plan_title = t(plan_title_key, locale) if plan_title_key else plan_key
    duration_key = data.get("duration_key")
    duration_label = t(duration_key, locale) if duration_key else duration_key
    price = data.get("price", 0)
    await call.message.answer(
        t("subscription_payment_created", locale),
        reply_markup=get_main_keyboard(locale),
    )
    await state.set_state(MenuState.main_menu)
    logging.info(
        "User %s started payment for %s (%s) — %s",
        call.from_user.id,
        plan_title,
        duration_label,
        price,
    )


@router.message(SubscriptionState.payment_method, F.text.in_(BACK_BUTTONS))
async def payment_back(message: types.Message, state: FSMContext) -> None:
    await _resolve_locale(state, message.from_user.id)
    data = await state.get_data()
    await _delete_payment_message(message, data)
    plan_key = data.get("plan_key")
    await state.update_data(
        payment_message_id=None,
        duration_key=None,
        price=None,
    )
    if not plan_key:
        await _send_plan_intro(message, state)
        return

    await _show_duration_selection(message, state, plan_key)


@router.message(SubscriptionState.duration, F.text.in_(BACK_BUTTONS))
async def duration_back(message: types.Message, state: FSMContext) -> None:
    await _send_plan_intro(message, state)


@router.message(SubscriptionState.plan_type, F.text.in_(BACK_BUTTONS))
async def plan_back(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)
