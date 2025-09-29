import logging
import re
from asyncio import Lock
from typing import Mapping

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from handlers.start import show_main_menu
from keyboards.main import (
    get_devices_keyboard,
    get_my_devices_keyboard,
    get_pc_instructions_keyboard,
    get_phone_instructions_keyboard,
)
from states.states import DeviceState, MenuState
from utils.file import create_temp_conf_file
from utils.qr import create_qr_code
from utils.storage import get_user_locale
from utils.texts import get_all_translations, t
from utils.userdata import get_user_info, mark_device_connected
from utils.plans import get_plan_limit
from vpn.wireguard import generate_peer

router = Router()

_config_generation_lock = Lock()
_config_generation_in_progress: set[int] = set()

DEVICES_BUTTONS = tuple(get_all_translations("btn_devices"))
PHONE_BUTTONS = tuple(get_all_translations("btn_phone"))
COMPUTER_BUTTONS = tuple(get_all_translations("btn_computer"))
MY_DEVICES_BUTTONS = tuple(get_all_translations("btn_my_devices"))
BACK_BUTTONS = tuple(get_all_translations("btn_back"))
ANDROID_BUTTONS = tuple(get_all_translations("btn_android"))
IOS_BUTTONS = tuple(get_all_translations("btn_ios"))
WINDOWS_BUTTONS = tuple(get_all_translations("btn_windows_instructions"))
MACOS_BUTTONS = tuple(get_all_translations("btn_macos_instructions"))


def _expand_variants(values: tuple[str, ...]) -> set[str]:
    expanded = set(values)
    for value in values:
        expanded.add(value.replace(" ", ""))
    return expanded


async def _resolve_locale(state: FSMContext, user_id: int) -> str:
    data = await state.get_data()
    locale = data.get("locale")
    if locale:
        return locale
    locale = await get_user_locale(user_id)
    await state.update_data(locale=locale)
    return locale


async def _acquire_config_generation(user_id: int) -> bool:
    async with _config_generation_lock:
        if user_id in _config_generation_in_progress:
            return False
        _config_generation_in_progress.add(user_id)
        return True


async def _release_config_generation(user_id: int) -> None:
    async with _config_generation_lock:
        _config_generation_in_progress.discard(user_id)


async def _device_limit_info(user_id: int) -> tuple[dict, int, int]:
    info = await get_user_info(user_id)
    limit = info.get("device_limit") or get_plan_limit(info.get("plan"))
    peers = info.get("peers", len(info.get("devices", {})))
    return info, peers, limit


def _next_device_index(devices: Mapping[str, object], label_key: str) -> int:
    possible_labels = _expand_variants(tuple(get_all_translations(label_key)))
    max_index = 0
    for label in devices.keys():
        for base_label in possible_labels:
            pattern = re.compile(rf"^{re.escape(base_label)}(?: \((?P<index>\d+)\))?$")
            match = pattern.match(label)
            if not match:
                continue
            index = match.group("index")
            if index:
                max_index = max(max_index, int(index))
            else:
                max_index = max(max_index, 1)
    return max_index + 1 if max_index else 1


def _format_device_label(base_label: str, index: int) -> str:
    return base_label if index == 1 else f"{base_label} ({index})"


def _build_config_basename(base_slug: str, index: int) -> str:
    return base_slug if index == 1 else f"{base_slug}({index})"


def _config_basename_from_label(label: str) -> str:
    if label.startswith("📱"):
        base = "phone"
    elif label.startswith("💻"):
        base = "desktop"
    else:
        base = "device"
    match = re.search(r"\((\d+)\)\s*$", label)
    if match:
        return f"{base}({match.group(1)})"
    return base


async def show_devices_menu(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    await message.answer(
        t("devices_choose", locale),
        reply_markup=get_devices_keyboard(locale),
    )
    await state.set_state(DeviceState.choose_device)


@router.message(MenuState.main_menu, F.text.in_(DEVICES_BUTTONS))
async def choose_device(message: types.Message, state: FSMContext) -> None:
    await show_devices_menu(message, state)


@router.message(DeviceState.choose_device, F.text.in_(PHONE_BUTTONS))
async def phone_selected(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    user_id = message.from_user.id
    if not await _acquire_config_generation(user_id):
        await message.answer(t("devices_generation_in_progress", locale))
        return
    try:
        info, peers, limit = await _device_limit_info(user_id)
        if peers >= limit:
            await message.answer(t("devices_limit_reached", locale))
            return
        config = await generate_peer(user_id)
        devices = info.get("devices", {})
        next_index = _next_device_index(devices, "btn_phone")
        base_label = t("btn_phone", locale)
        device_label = _format_device_label(base_label, next_index)
        config_name = _build_config_basename("phone", next_index)
        conf_file = create_temp_conf_file(config, filename=f"{config_name}.conf")
        qr_file = create_qr_code(config)
        await message.answer_photo(
            types.FSInputFile(str(qr_file)),
            caption=t("device_ready_title", locale) + "\n\n" + t("device_ready_body", locale),
        )
        await message.answer(
            t("devices_pick_guide", locale),
            reply_markup=get_phone_instructions_keyboard(locale),
        )
        await message.answer_document(types.FSInputFile(conf_file))
        await mark_device_connected(user_id, device_label, config)
        logging.info("Sent phone config to %s (%s)", user_id, device_label)
        await state.set_state(DeviceState.choose_device)
    finally:
        await _release_config_generation(user_id)


@router.message(DeviceState.choose_device, F.text.in_(COMPUTER_BUTTONS))
async def pc_selected(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    user_id = message.from_user.id
    if not await _acquire_config_generation(user_id):
        await message.answer(t("devices_generation_in_progress", locale))
        return
    try:
        info, peers, limit = await _device_limit_info(user_id)
        if peers >= limit:
            await message.answer(t("devices_limit_reached", locale))
            return
        config = await generate_peer(user_id)
        devices = info.get("devices", {})
        next_index = _next_device_index(devices, "btn_computer")
        base_label = t("btn_computer", locale)
        device_label = _format_device_label(base_label, next_index)
        config_name = _build_config_basename("desktop", next_index)
        conf_file = create_temp_conf_file(config, filename=f"{config_name}.conf")
        qr_file = create_qr_code(config)
        await message.answer_photo(
            types.FSInputFile(str(qr_file)),
            caption=t("device_ready_title", locale) + "\n\n" + t("device_ready_body", locale),
        )
        await message.answer(
            t("devices_pick_guide", locale),
            reply_markup=get_pc_instructions_keyboard(locale),
        )
        await message.answer_document(types.FSInputFile(conf_file))
        await mark_device_connected(user_id, device_label, config)
        logging.info("Sent PC config to %s (%s)", user_id, device_label)
        await state.set_state(DeviceState.choose_device)
    finally:
        await _release_config_generation(user_id)


@router.message(DeviceState.choose_device, F.text.in_(MY_DEVICES_BUTTONS))
async def my_devices(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    info = await get_user_info(message.from_user.id)
    devices = list(info.get("devices", {}).keys())
    if not devices:
        await message.answer(
            t("devices_none", locale), reply_markup=get_devices_keyboard(locale)
        )
        return
    await message.answer(
        t("devices_list_intro", locale),
        reply_markup=get_my_devices_keyboard(devices, locale),
    )
    await state.set_state(DeviceState.my_devices)


@router.message(DeviceState.choose_device, F.text.in_(BACK_BUTTONS))
async def devices_back(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)


@router.message(DeviceState.my_devices, F.text.in_(BACK_BUTTONS))
async def my_devices_back(message: types.Message, state: FSMContext) -> None:
    await show_devices_menu(message, state)


@router.message(DeviceState.my_devices)
async def resend_config(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    info = await get_user_info(message.from_user.id)
    device = info.get("devices", {}).get(message.text)
    if not device:
        await message.answer(
            t("devices_select_prompt", locale),
            reply_markup=get_my_devices_keyboard(list(info.get("devices", {}).keys()), locale),
        )
        return
    config = device.get("config")
    config_basename = _config_basename_from_label(message.text)
    conf_file = create_temp_conf_file(config, filename=f"{config_basename}.conf")
    qr_file = create_qr_code(config)
    await message.answer_photo(
        types.FSInputFile(str(qr_file)),
        caption=t("device_ready_title", locale) + "\n\n" + t("device_ready_body", locale),
    )
    if any(message.text.startswith(label) for label in PHONE_BUTTONS):
        kb = get_phone_instructions_keyboard(locale)
    elif any(message.text.startswith(label) for label in COMPUTER_BUTTONS):
        kb = get_pc_instructions_keyboard(locale)
    else:
        kb = get_phone_instructions_keyboard(locale)
    await message.answer(t("devices_pick_guide", locale), reply_markup=kb)
    await message.answer_document(types.FSInputFile(conf_file))


@router.callback_query(F.data == "instruction_android")
async def android_instructions_callback(callback: types.CallbackQuery) -> None:
    locale = await get_user_locale(callback.from_user.id)
    await callback.message.answer(
        t("instruction_link_android", locale),
        parse_mode="HTML",
    )
    await callback.answer()


@router.message(F.text.in_(ANDROID_BUTTONS))
async def android_instructions(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    await message.answer(
        t("instruction_link_android", locale),
        parse_mode="HTML",
    )


@router.callback_query(F.data == "instruction_ios")
async def iphone_instructions_callback(callback: types.CallbackQuery) -> None:
    locale = await get_user_locale(callback.from_user.id)
    await callback.message.answer(
        t("instruction_link_ios", locale),
        parse_mode="HTML",
    )
    await callback.answer()


@router.message(F.text.in_(IOS_BUTTONS))
async def iphone_instructions(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    await message.answer(
        t("instruction_link_ios", locale),
        parse_mode="HTML",
    )


@router.callback_query(F.data == "instruction_windows")
async def windows_instructions_callback(callback: types.CallbackQuery) -> None:
    locale = await get_user_locale(callback.from_user.id)
    await callback.message.answer(
        t("instruction_link_windows", locale),
        parse_mode="HTML",
    )
    await callback.answer()


@router.message(F.text.in_(WINDOWS_BUTTONS))
async def windows_instructions(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    await message.answer(
        t("instruction_link_windows", locale),
        parse_mode="HTML",
    )


@router.callback_query(F.data == "instruction_macos")
async def macos_instructions_callback(callback: types.CallbackQuery) -> None:
    locale = await get_user_locale(callback.from_user.id)
    await callback.message.answer(
        t("instruction_link_macos", locale),
        parse_mode="HTML",
    )
    await callback.answer()


@router.message(F.text.in_(MACOS_BUTTONS))
async def macos_instructions(message: types.Message, state: FSMContext) -> None:
    locale = await _resolve_locale(state, message.from_user.id)
    await message.answer(
        t("instruction_link_macos", locale),
        parse_mode="HTML",
    )
