import logging
import re
from typing import Mapping
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from keyboards.main import (
    get_devices_keyboard,
    get_phone_instructions_keyboard,
    get_pc_instructions_keyboard,
    get_my_devices_keyboard,
)
from handlers.start import show_main_menu
from states.states import MenuState, DeviceState
from utils.file import create_temp_conf_file
from utils.qr import create_qr_code
from utils.userdata import mark_device_connected, get_user_info
from utils.plans import get_plan_limit
from utils.texts import t
from vpn.wireguard import generate_peer

router = Router()


async def _device_limit_info(user_id: int) -> tuple[dict, int, int]:
    info = await get_user_info(user_id)
    limit = info.get("device_limit") or get_plan_limit(info.get("plan"))
    peers = info.get("peers", len(info.get("devices", {})))
    return info, peers, limit


def _next_device_index(devices: Mapping[str, object], base_label: str) -> int:
    pattern = re.compile(rf"^{re.escape(base_label)}(?: \((?P<index>\d+)\))?$")
    max_index = 0
    for label in devices.keys():
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
    await message.answer(
        t("devices_choose"),
        reply_markup=get_devices_keyboard(),
    )
    await state.set_state(DeviceState.choose_device)


@router.message(MenuState.main_menu, F.text == t("btn_devices"))
async def choose_device(message: types.Message, state: FSMContext) -> None:
    await show_devices_menu(message, state)


@router.message(
    DeviceState.choose_device, F.text.in_(("📱 Телефон", "📱Телефон"))
)
async def phone_selected(message: types.Message, state: FSMContext) -> None:
    info, peers, limit = await _device_limit_info(message.from_user.id)
    if peers >= limit:
        await message.answer(t("devices_limit_reached"))
        return
    config = await generate_peer(message.from_user.id)
    devices = info.get("devices", {})
    next_index = _next_device_index(devices, "📱 Телефон")
    device_label = _format_device_label("📱 Телефон", next_index)
    config_name = _build_config_basename("phone", next_index)
    conf_file = create_temp_conf_file(config, filename=f"{config_name}.conf")
    qr_file = create_qr_code(config)
    await message.answer_photo(
        types.FSInputFile(str(qr_file)),
        caption=t("device_ready_title") + "\n\n" + t("device_ready_body"),
    )
    await message.answer_document(types.FSInputFile(conf_file))
    await message.answer(
        t("devices_pick_guide"),
        reply_markup=get_phone_instructions_keyboard(),
    )
    await mark_device_connected(message.from_user.id, device_label, config)
    logging.info(
        "Sent phone config to %s (%s)", message.from_user.id, device_label
    )
    await state.set_state(DeviceState.choose_device)


@router.message(
    DeviceState.choose_device, F.text.in_(("💻 Компьютер", "💻Компьютер"))
)
async def pc_selected(message: types.Message, state: FSMContext) -> None:
    info, peers, limit = await _device_limit_info(message.from_user.id)
    if peers >= limit:
        await message.answer(t("devices_limit_reached"))
        return
    config = await generate_peer(message.from_user.id)
    devices = info.get("devices", {})
    next_index = _next_device_index(devices, "💻 Компьютер")
    device_label = _format_device_label("💻 Компьютер", next_index)
    config_name = _build_config_basename("desktop", next_index)
    conf_file = create_temp_conf_file(config, filename=f"{config_name}.conf")
    qr_file = create_qr_code(config)
    await message.answer_photo(
        types.FSInputFile(str(qr_file)),
        caption=t("device_ready_title") + "\n\n" + t("device_ready_body"),
    )
    await message.answer_document(types.FSInputFile(conf_file))
    await message.answer(
        t("devices_pick_guide"),
        reply_markup=get_pc_instructions_keyboard(),
    )
    await mark_device_connected(message.from_user.id, device_label, config)
    logging.info(
        "Sent PC config to %s (%s)", message.from_user.id, device_label
    )
    await state.set_state(DeviceState.choose_device)


@router.message(
    DeviceState.choose_device, F.text.in_(("🔌 Мои устройства", "🔌Мои устройства"))
)
async def my_devices(message: types.Message, state: FSMContext) -> None:
    info = await get_user_info(message.from_user.id)
    devices = list(info.get("devices", {}).keys())
    if not devices:
        await message.answer(t("devices_none"), reply_markup=get_devices_keyboard())
        return
    await message.answer(
        "👇 Список твоих подключённых устройств:",
        reply_markup=get_my_devices_keyboard(devices),
    )
    await state.set_state(DeviceState.my_devices)


@router.message(DeviceState.choose_device, F.text == "⬅️ Назад")
async def devices_back(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)


@router.message(DeviceState.my_devices, F.text == "⬅️ Назад")
async def my_devices_back(message: types.Message, state: FSMContext) -> None:
    await show_devices_menu(message, state)


@router.message(DeviceState.my_devices)
async def resend_config(message: types.Message, state: FSMContext) -> None:
    info = await get_user_info(message.from_user.id)
    device = info.get("devices", {}).get(message.text)
    if not device:
        await message.answer(
            "Выбери устройство из списка",
            reply_markup=get_my_devices_keyboard(list(info.get("devices", {}).keys())),
        )
        return
    config = device.get("config")
    config_basename = _config_basename_from_label(message.text)
    conf_file = create_temp_conf_file(config, filename=f"{config_basename}.conf")
    qr_file = create_qr_code(config)
    await message.answer_photo(
        types.FSInputFile(str(qr_file)),
        caption=t("device_ready_title") + "\n\n" + t("device_ready_body"),
    )
    await message.answer_document(types.FSInputFile(conf_file))
    if message.text.startswith("📱"):
        kb = get_phone_instructions_keyboard()
    elif message.text.startswith("💻"):
        kb = get_pc_instructions_keyboard()
    else:
        kb = get_phone_instructions_keyboard()
    await message.answer(t("devices_pick_guide"), reply_markup=kb)


@router.callback_query(F.data == "instruction_android")
async def android_instructions_callback(callback: types.CallbackQuery) -> None:
    await callback.message.answer(
        '<a href="https://telegra.ph/Android-Instr-06-25">📚 Инструкция для Android</a>',
        parse_mode="HTML",
    )
    await callback.answer()


@router.message(F.text == t("btn_android"))
async def android_instructions(message: types.Message) -> None:
    await message.answer(
        '<a href="https://telegra.ph/Android-Instr-06-25">📚 Инструкция для Android</a>',
        parse_mode="HTML",
    )


@router.callback_query(F.data == "instruction_ios")
async def iphone_instructions_callback(callback: types.CallbackQuery) -> None:
    await callback.message.answer(
        '<a href="https://telegra.ph/Android-Instr-06-25">📚 Инструкция для iPhone</a>',
        parse_mode="HTML",
    )
    await callback.answer()


@router.message(F.text == t("btn_ios"))
async def iphone_instructions(message: types.Message) -> None:
    await message.answer(
        '<a href="https://telegra.ph/Android-Instr-06-25">📚 Инструкция для iPhone</a>',
        parse_mode="HTML",
    )


@router.callback_query(F.data == "instruction_windows")
async def windows_instructions_callback(callback: types.CallbackQuery) -> None:
    await callback.message.answer(
        '<a href="https://telegra.ph/Android-Instr-06-25">📚 Инструкция для Windows</a>',
        parse_mode="HTML",
    )
    await callback.answer()


@router.message(F.text == "🔴 Инструкция для Windows")
async def windows_instructions(message: types.Message) -> None:
    await message.answer(
        '<a href="https://telegra.ph/Android-Instr-06-25">📚 Инструкция для Windows</a>',
        parse_mode="HTML",
    )


@router.callback_query(F.data == "instruction_macos")
async def macos_instructions_callback(callback: types.CallbackQuery) -> None:
    await callback.message.answer(
        '<a href="https://telegra.ph/Android-Instr-06-25">📚 Инструкция для MacOS</a>',
        parse_mode="HTML",
    )
    await callback.answer()


@router.message(F.text == "🟢 Инструкция для MacOS")
async def macos_instructions(message: types.Message) -> None:
    await message.answer(
        '<a href="https://telegra.ph/Android-Instr-06-25">📚 Инструкция для MacOS</a>',
        parse_mode="HTML",
    )
