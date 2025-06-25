from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


def get_intro_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [[KeyboardButton(text="Начать")]]
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
        [KeyboardButton(text="1 мес – 99₽"), KeyboardButton(text="3 мес – 249₽")],
        [KeyboardButton(text="6 мес – 450₽")],
        [KeyboardButton(text="⬅️ Назад")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_payment_methods_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="💳 Банковская карта", callback_data="pay_card")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


from urllib.parse import quote_plus


def get_share_keyboard(url: str) -> InlineKeyboardMarkup:
    share_url = f"https://t.me/share/url?url={quote_plus(url)}"
    keyboard = [[InlineKeyboardButton(text="Поделиться ссылкой", url=share_url)]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_phone_instructions_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Android", callback_data="android"),
         InlineKeyboardButton(text="iPhone", callback_data="iphone")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="home")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_pc_instructions_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Windows", callback_data="windows"),
         InlineKeyboardButton(text="MacOS", callback_data="mac")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="home")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
