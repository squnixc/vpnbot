from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_admin_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="/stats"), KeyboardButton(text="/peers")],
        [KeyboardButton(text="/traffic"), KeyboardButton(text="/sysinfo")],
        [KeyboardButton(text="/restart_wg")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
