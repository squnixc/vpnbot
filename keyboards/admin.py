from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_admin_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="/admin_panel")],
        [KeyboardButton(text="/about")],
        [KeyboardButton(text="/manage")],
        [KeyboardButton(text="/main_menu")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_admin_panel_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="/stats")],
        [KeyboardButton(text="/peers")],
        [KeyboardButton(text="/traffic")],
        [KeyboardButton(text="/sysinfo")],
        [KeyboardButton(text="/restart_wg")],
        [KeyboardButton(text="/back")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_about_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="/send")],
        [KeyboardButton(text="/gift")],
        [KeyboardButton(text="/config")],
        [KeyboardButton(text="/back")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_send_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="/to_one"), KeyboardButton(text="/to_all")],
        [KeyboardButton(text="/back")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_gift_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="/to_one"), KeyboardButton(text="/to_all")],
        [KeyboardButton(text="/back")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_config_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [[KeyboardButton(text="/back")]]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_manage_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="/ban"), KeyboardButton(text="/unban")],
        [KeyboardButton(text="/back")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
