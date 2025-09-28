import logging
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from datetime import datetime, timedelta

from keyboards.main import (
    get_intro_keyboard,
    get_main_keyboard,
)
from states.states import MenuState
from utils.userdata import get_user_info, format_timedelta
from utils.storage import register_referral, update_expiration, grant_trial_if_new
from utils.plans import get_plan_title, get_plan_limit
from utils.texts import t

REFERRAL_REWARD_MINUTES = 7 * 24 * 60
TRIAL_PERIOD_MINUTES = 7 * 24 * 60

router = Router()


@router.message(CommandStart())
async def command_start(message: types.Message, state: FSMContext) -> None:
    await _process_referral(message)

    trial_granted = await grant_trial_if_new(message.from_user.id, TRIAL_PERIOD_MINUTES)
    if trial_granted:
        await message.answer(
            "🎁 Твой бонус: 7 дней бесплатно!\n"
            "Попробуй быстрый и защищённый доступ без ограничений."
        )

    data = await state.get_data()
    if not data.get("seen_intro"):
        await message.answer(
            t("start_pitch"),
            reply_markup=get_intro_keyboard(),
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
    devices = info.get("devices", {})
    expires = info.get("expires_at")
    time_left = (expires - datetime.utcnow()) if expires else timedelta()
    active_for = (
        format_timedelta(time_left)
        if time_left.total_seconds() > 0
        else "0 секунд"
    )
    def normalize_device_name(name: str) -> str:
        trimmed = name.lstrip()
        while trimmed and not trimmed[0].isalnum():
            trimmed = trimmed[1:].lstrip()
        return trimmed or name

    plan_value = info.get("plan")
    plan_title = get_plan_title(plan_value)
    device_limit = info.get("device_limit") or get_plan_limit(plan_value)
    connected_devices = len(devices)
    devices_counter = f"(Устройства: {connected_devices} / {device_limit})"

    if devices:
        device_lines = "\n".join(
            f"- {normalize_device_name(device_name)}" for device_name in devices.keys()
        )
        connections_block = f"📟 Подключения:\n{device_lines}"
    else:
        connections_block = "📟 Подключения:\nНет подключений"

    status_text = t("status_text").format(
        connections_block=connections_block,
        active_for=active_for,
        plan_title=plan_title,
        devices_counter=devices_counter,
    )
    await message.answer(
        status_text,
        reply_markup=get_main_keyboard(),
    )
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
        await message.bot.send_message(
            referrer_id,
            "🎉 Ваш друг присоединился!\nВам начислено +7 дней к подписке ✨",
        )
    except Exception as exc:  # noqa: BLE001
        logging.exception("Failed to notify referrer %s: %s", referrer_id, exc)
    else:
        logging.info("Referral reward granted to %s by %s", referrer_id, new_user_id)


@router.message(F.text == t("btn_main_menu"))
async def main_menu_button(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)


@router.callback_query(F.data == "main_menu")
async def main_menu_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    try:
        await callback.message.delete()
    except Exception as e:  # noqa: BLE001
        logging.exception("Failed to delete message: %s", e)
    await show_main_menu(callback.message, state)
