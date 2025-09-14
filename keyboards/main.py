from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from utils.texts import t


def get_intro_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [[KeyboardButton(text="🚀 Вперед!")]]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text=t("btn_devices")), KeyboardButton(text=t("btn_subscription"))],
        [KeyboardButton(text="🤝 Пригласить друга"), KeyboardButton(text=t("btn_questions"))],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_devices_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="📱Телефон"), KeyboardButton(text="💻Компьютер")],
        [KeyboardButton(text="Мои устройства"), KeyboardButton(text="⬅️ Назад")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_subscription_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="1 месяц - 99₽"), KeyboardButton(text="🔹3 месяца - 249₽")],
        [KeyboardButton(text="🔸6 месяцев - 450₽")],
        [KeyboardButton(text="⬅️ Назад")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_payment_methods_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="💳 Банковская карта", callback_data="pay_card")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
from urllib.parse import quote_plus


def get_share_keyboard(url: str) -> InlineKeyboardMarkup:
    share_url = f"https://t.me/share/url?url={quote_plus(url)}"
    keyboard = [[InlineKeyboardButton(text="Поделиться ссылкой", url=share_url)]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_phone_instructions_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text=t("btn_android")),
            KeyboardButton(text=t("btn_ios")),
        ],
        [KeyboardButton(text=t("btn_main_menu"))],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_pc_instructions_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text="🔴Инструкция для Windows"),
            KeyboardButton(text="🟢Инструкция для MacOS"),
        ],
        [KeyboardButton(text=t("btn_main_menu"))],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_my_devices_keyboard(devices: list[str]) -> ReplyKeyboardMarkup:
    keyboard = [[KeyboardButton(text=name)] for name in devices]
    keyboard.append([KeyboardButton(text="⬅️ Назад")])
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_main_menu_inline() -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton(text=t("btn_main_menu"), callback_data="main_menu")]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
