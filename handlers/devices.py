import logging
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from keyboards.main import (
    get_devices_keyboard,
    get_main_keyboard,
    get_phone_instructions_keyboard,
    get_pc_instructions_keyboard,
)
from states.states import MenuState, DeviceState
from utils.file import create_temp_conf_file
from utils.qr import create_qr_code
from vpn.wireguard import generate_peer

router = Router()


@router.message(MenuState.main_menu, F.text == "📱 Устройства")
async def choose_device(message: types.Message, state: FSMContext) -> None:
    await message.answer("Выберите устройство", reply_markup=get_devices_keyboard())
    await state.set_state(DeviceState.choose_device)


@router.message(DeviceState.choose_device, F.text == "Телефон")
async def phone_selected(message: types.Message, state: FSMContext) -> None:
    config = generate_peer(message.from_user.id)
    conf_file = create_temp_conf_file(config)
    qr_file = create_qr_code(config)
    await message.answer_photo(types.FSInputFile(qr_file), caption="Ваш конфиг")
    await message.answer_document(types.FSInputFile(conf_file))
    await message.answer(
        "Инструкции", reply_markup=get_phone_instructions_keyboard()
    )
    logging.info("Sent phone config to %s", message.from_user.id)


@router.message(DeviceState.choose_device, F.text == "Компьютер")
async def pc_selected(message: types.Message, state: FSMContext) -> None:
    config = generate_peer(message.from_user.id)
    conf_file = create_temp_conf_file(config)
    qr_file = create_qr_code(config)
    await message.answer_photo(types.FSInputFile(qr_file), caption="Ваш конфиг")
    await message.answer_document(types.FSInputFile(conf_file))
    await message.answer(
        "Инструкции", reply_markup=get_pc_instructions_keyboard()
    )
    logging.info("Sent PC config to %s", message.from_user.id)


@router.message(DeviceState.choose_device, F.text == "⬅️ Назад")
async def devices_back(message: types.Message, state: FSMContext) -> None:
    await message.answer("Главное меню", reply_markup=get_main_keyboard())
    await state.set_state(MenuState.main_menu)
