import logging
from datetime import datetime, timedelta

from aiogram import F, Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from keyboards.main import get_intro_keyboard, get_main_keyboard
from states.states import MenuState
from utils.plans import get_plan_limit, get_plan_title
from utils.storage import (
    get_user_locale,
    grant_trial_if_new,
    register_referral,
    set_user_locale,
    update_expiration,
)
from utils.texts import get_all_translations, normalize_locale, t
from utils.userdata import format_timedelta, get_user_info

REFERRAL_REWARD_MINUTES = 7 * 24 * 60
TRIAL_PERIOD_MINUTES = 7 * 24 * 60

router = Router()


@router.message(CommandStart())
async def command_start(message: types.Message, state: FSMContext) -> None:
    await _process_referral(message)

    language_code = message.from_user.language_code
    normalized_locale = normalize_locale(language_code)
    await set_user_locale(message.from_user.id, language_code)
    await state.update_data(locale=normalized_locale)

    trial_granted = await grant_trial_if_new(message.from_user.id, TRIAL_PERIOD_MINUTES)
    if trial_granted:
        await message.answer(t("start_trial_granted", normalized_locale))

    data = await state.get_data()
    if not data.get("seen_intro"):
        await message.answer(
            t("start_pitch", normalized_locale),
            reply_markup=get_intro_keyboard(normalized_locale),
        )
        await state.update_data(seen_intro=True)
        await state.set_state(MenuState.intro)
    else:
        await show_main_menu(message, state)


@router.message(MenuState.intro, F.text)
async def show_menu_after_intro(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)


async def show_main_menu(message: types.Message, state: FSMContext) -> None:
    info = await get_user_info(message.from_user.id)
    locale = info.get("locale") or (await state.get_data()).get("locale") or "en"
    await state.update_data(locale=locale)
    devices = info.get("devices", {})
    expires = info.get("expires_at")
    time_left = (expires - datetime.utcnow()) if expires else timedelta()
    active_for = (
        format_timedelta(time_left, locale)
        if time_left.total_seconds() > 0
        else t("time_zero", locale)
    )

    def normalize_device_name(name: str) -> str:
        trimmed = name.lstrip()
        while trimmed and not trimmed[0].isalnum():
            trimmed = trimmed[1:].lstrip()
        return trimmed or name

    plan_value = info.get("plan")
    plan_title = get_plan_title(plan_value, locale)
    device_limit = info.get("device_limit") or get_plan_limit(plan_value)
    connected_devices = len(devices)
    devices_counter = t("status_devices_counter", locale).format(
        connected=connected_devices,
        limit=device_limit,
    )

    if devices:
        device_lines = "\n".join(
            t("status_connections_prefix", locale).format(
                device_name=normalize_device_name(device_name)
            )
            for device_name in devices.keys()
        )
        connections_block = (
            t("status_connections_header", locale) + "\n" + device_lines
        )
    else:
        connections_block = (
            t("status_connections_header", locale)
            + "\n"
            + t("status_connections_empty", locale)
        )

    status_lines = [
        t("status_header", locale),
        "",
        t("status_plan_line", locale).format(plan_title=plan_title),
        devices_counter,
        "",
        connections_block,
        "",
        t("status_active_line", locale).format(duration=active_for),
        "",
        t("status_bonus_line", locale),
    ]
    status_text = "\n".join(status_lines)
    await message.answer(status_text, reply_markup=get_main_keyboard(locale))
    await state.set_state(MenuState.main_menu)


async def _process_referral(message: types.Message) -> None:
    """Handle referral start payload, if any."""

    text = message.text or ""
    parts = text.split(maxsplit=1)
    if len(parts) < 2:
        return

    payload = parts[1].strip()
    if not payload.isdigit():
        return

    referrer_id = int(payload)
    new_user_id = message.from_user.id

    if referrer_id == 0 or referrer_id == new_user_id:
        return

    try:
        is_new_referral = await register_referral(new_user_id, referrer_id)
    except Exception as exc:  # noqa: BLE001
        logging.exception("Failed to register referral for %s: %s", new_user_id, exc)
        return

    if not is_new_referral:
        return

    try:
        await update_expiration(referrer_id, REFERRAL_REWARD_MINUTES)
    except Exception as exc:  # noqa: BLE001
        logging.exception(
            "Failed to apply referral reward for %s from %s: %s",
            referrer_id,
            new_user_id,
            exc,
        )
        return

    try:
        locale = await get_user_locale(referrer_id)
        await message.bot.send_message(
            referrer_id,
            t("referral_reward_notification", locale),
        )
    except Exception as exc:  # noqa: BLE001
        logging.exception("Failed to notify referrer %s: %s", referrer_id, exc)
    else:
        logging.info("Referral reward granted to %s by %s", referrer_id, new_user_id)


@router.message(F.text.in_(get_all_translations("btn_main_menu")))
async def main_menu_button(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)


@router.callback_query(F.data == "main_menu")
async def main_menu_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    try:
        await callback.message.delete()
    except Exception as exc:  # noqa: BLE001
        logging.exception("Failed to delete message: %s", exc)
    await show_main_menu(callback.message, state)
