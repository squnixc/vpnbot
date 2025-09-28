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
        [KeyboardButton(text=t("btn_main_menu"))],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_devices_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="📱 Телефон"), KeyboardButton(text="💻 Компьютер")],
        [KeyboardButton(text="🔌 Мои устройства"), KeyboardButton(text="⬅️ Назад")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_subscription_plan_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="💫 Устройства: 2 - 99₽/мес.")],
        [KeyboardButton(text="✨ Устройства: 5 - 169₽/мес.")],
        [KeyboardButton(text="⬅️ Назад")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_subscription_duration_keyboard(plan_key: str) -> ReplyKeyboardMarkup:
    plan_options = {
        "devices_2": [
            "1 месяц - 99₽",
            "🔹3 месяца - 249₽",
            "🔸6 месяцев - 399₽",
        ],
        "devices_5": [
            "1 месяц - 169₽",
            "🔹3 месяца - 449₽",
            "🔸6 месяцев - 749₽",
        ],
    }
    options = plan_options.get(plan_key, [])
    keyboard = [
        [KeyboardButton(text=options[0]), KeyboardButton(text=options[1])],
        [KeyboardButton(text=options[2])],
        [KeyboardButton(text="⬅️ Назад")],
    ] if len(options) == 3 else [[KeyboardButton(text="⬅️ Назад")]]
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


def get_main_menu_only_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [[KeyboardButton(text=t("btn_main_menu"))]]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_phone_instructions_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(text=t("btn_android"), callback_data="instruction_android"),
            InlineKeyboardButton(text=t("btn_ios"), callback_data="instruction_ios"),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_pc_instructions_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                text="🔴 Инструкция для Windows", callback_data="instruction_windows"
            ),
            InlineKeyboardButton(
                text="🟢 Инструкция для MacOS", callback_data="instruction_macos"
            ),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_my_devices_keyboard(devices: list[str]) -> ReplyKeyboardMarkup:
    keyboard = [[KeyboardButton(text=name)] for name in devices]
    keyboard.append([KeyboardButton(text="⬅️ Назад")])
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_main_menu_inline() -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton(text=t("btn_main_menu"), callback_data="main_menu")]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
