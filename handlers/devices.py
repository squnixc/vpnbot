import logging
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from keyboards.main import (
    get_devices_keyboard,
    get_phone_instructions_keyboard,
    get_pc_instructions_keyboard,
)
from handlers.start import show_main_menu
from states.states import MenuState, DeviceState
from utils.file import create_temp_conf_file
from utils.qr import create_qr_code
from utils.userdata import mark_device_connected
from vpn.wireguard import generate_peer

router = Router()


@router.message(MenuState.main_menu, F.text == "📱 Устройства")
async def choose_device(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        "📲Выбери устройство, которое хочешь подключить\n"
        "(Это займёт всего пару минут — всё просто!)",
        reply_markup=get_devices_keyboard(),
    )
    await state.set_state(DeviceState.choose_device)


@router.message(F.text == "📱Телефон")
async def phone_selected(message: types.Message, state: FSMContext) -> None:
    config = generate_peer(message.from_user.id)
    conf_file = create_temp_conf_file(config)
    qr_file = create_qr_code(config)
    await message.answer_photo(
        types.FSInputFile(str(qr_file)),
        caption=(
            "📥 Подключение почти готово!\n\n"
            "Ты можешь подключиться к VPN двумя способами:\n"
            "Скачать файл vpn.conf\n"
            "Или отсканировать QR-код в приложении WireGuard / AmneziaWG\n\n"
            "📖 Затем открой инструкцию для своего устройства и следуй шагам — подключение займёт меньше минуты!"
        ),
    )
    await message.answer_document(types.FSInputFile(conf_file))
    await message.answer(
        "⚠️Один конфиг работает для одного устройства!\n👇 Выбери инструкцию:",
        reply_markup=get_phone_instructions_keyboard(),
    )
    mark_device_connected(message.from_user.id, "phone")
    logging.info("Sent phone config to %s", message.from_user.id)
    await state.set_state(DeviceState.choose_device)


@router.message(F.text == "💻Компьютер")
async def pc_selected(message: types.Message, state: FSMContext) -> None:
    config = generate_peer(message.from_user.id)
    conf_file = create_temp_conf_file(config)
    qr_file = create_qr_code(config)
    await message.answer_photo(
        types.FSInputFile(str(qr_file)),
        caption=(
            "📥 Подключение почти готово!\n\n"
            "Ты можешь подключиться к VPN двумя способами:\n"
            "Скачать файл vpn.conf\n"
            "Или отсканировать QR-код в приложении WireGuard / AmneziaWG\n\n"
            "📖 Затем открой инструкцию для своего устройства и следуй шагам — подключение займёт меньше минуты!"
        ),
    )
    await message.answer_document(types.FSInputFile(conf_file))
    await message.answer(
        "⚠️Один конфиг работает для одного устройства!\n👇 Выбери инструкцию:",
        reply_markup=get_pc_instructions_keyboard(),
    )
    mark_device_connected(message.from_user.id, "computer")
    logging.info("Sent PC config to %s", message.from_user.id)
    await state.set_state(DeviceState.choose_device)


@router.message(DeviceState.choose_device, F.text == "⬅️ Назад")
async def devices_back(message: types.Message, state: FSMContext) -> None:
    await show_main_menu(message, state)


@router.message(F.text == "🔴Инструкция для Android")
async def android_instructions(message: types.Message) -> None:
    await message.answer(
        '<a href="https://telegra.ph/Android-Instr-06-25">📱Инструкция для Android</a>',
        parse_mode="HTML",
    )


@router.message(F.text == "🟢Инструкция для iPhone")
async def iphone_instructions(message: types.Message) -> None:
    await message.answer(
        '<a href="https://telegra.ph/Android-Instr-06-25">🍏Инструкция для iPhone</a>',
        parse_mode="HTML",
    )


@router.message(F.text == "🔴Инструкция для Windows")
async def windows_instructions(message: types.Message) -> None:
    await message.answer(
        '<a href="https://telegra.ph/Android-Instr-06-25">🖥️Инструкция для Windows</a>',
        parse_mode="HTML",
    )


@router.message(F.text == "🟢Инструкция для MacOS")
async def macos_instructions(message: types.Message) -> None:
    await message.answer(
        '<a href="https://telegra.ph/Android-Instr-06-25">🍏Инструкция для MacOS</a>',
        parse_mode="HTML",
    )
