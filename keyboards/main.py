from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def get_intro_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [[KeyboardButton(text="🚀 Вперед!")]]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="📱 Устройства"), KeyboardButton(text="💎 Подписка")],
        [KeyboardButton(text="🤝 Пригласить друга"), KeyboardButton(text="❓ Вопросы")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_devices_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="Телефон"), KeyboardButton(text="Компьютер")],
        [KeyboardButton(text="⬅️ Назад")],
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


def get_connect_device_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="🔌 Подключить устройство", callback_data="open_devices")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


from urllib.parse import quote_plus


def get_share_keyboard(url: str) -> InlineKeyboardMarkup:
    share_url = f"https://t.me/share/url?url={quote_plus(url)}"
    keyboard = [[InlineKeyboardButton(text="Поделиться ссылкой", url=share_url)]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_phone_instructions_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="Android"), KeyboardButton(text="iPhone")],
        [KeyboardButton(text="🏠 Главное меню")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_pc_instructions_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="Windows"), KeyboardButton(text="MacOS")],
        [KeyboardButton(text="🏠 Главное меню")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
