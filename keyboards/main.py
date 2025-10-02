from urllib.parse import quote_plus

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from utils.subscription_plans import SUBSCRIPTION_PLANS
from utils.texts import t


def get_intro_keyboard(locale: str) -> ReplyKeyboardMarkup:
    keyboard = [[KeyboardButton(text=t("btn_intro_continue", locale))]]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_main_keyboard(locale: str) -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text=t("btn_devices", locale)),
            KeyboardButton(text=t("btn_subscription", locale)),
        ],
        [
            KeyboardButton(text=t("btn_invite_friend", locale)),
            KeyboardButton(text=t("btn_questions", locale)),
        ],
        [KeyboardButton(text=t("btn_main_menu", locale))],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_devices_keyboard(locale: str) -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text=t("btn_phone", locale)),
            KeyboardButton(text=t("btn_computer", locale)),
        ],
        [
            KeyboardButton(text=t("btn_my_devices", locale)),
            KeyboardButton(text=t("btn_back", locale)),
        ],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_subscription_plan_keyboard(locale: str) -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text=t(config["button_key"], locale))]
        for config in SUBSCRIPTION_PLANS.values()
    ]
    keyboard.append([KeyboardButton(text=t("btn_back", locale))])
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_subscription_duration_keyboard(plan_key: str, locale: str) -> ReplyKeyboardMarkup:
    plan_config = SUBSCRIPTION_PLANS.get(plan_key, {})
    durations = [
        t(duration_key, locale)
        for duration_key, _ in plan_config.get("durations", ())  # type: ignore[call-arg]
    ]
    keyboard: list[list[KeyboardButton]] = []
    if len(durations) >= 2:
        keyboard.append(
            [KeyboardButton(text=durations[0]), KeyboardButton(text=durations[1])]
        )
        remaining = durations[2:]
    else:
        remaining = durations
    for label in remaining:
        keyboard.append([KeyboardButton(text=label)])
    keyboard.append([KeyboardButton(text=t("btn_back", locale))])
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_payment_methods_keyboard(locale: str) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text=t("btn_pay_card", locale), callback_data="pay_card")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_payment_navigation_keyboard(locale: str) -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text=t("btn_back", locale))],
        [KeyboardButton(text=t("btn_main_menu", locale))],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_share_keyboard(url: str, locale: str) -> InlineKeyboardMarkup:
    share_url = f"https://t.me/share/url?url={quote_plus(url)}"
    keyboard = [[InlineKeyboardButton(text=t("btn_share_link", locale), url=share_url)]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_main_menu_only_keyboard(locale: str) -> ReplyKeyboardMarkup:
    keyboard = [[KeyboardButton(text=t("btn_main_menu", locale))]]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_phone_instructions_keyboard(locale: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                text=t("btn_android", locale), callback_data="instruction_android"
            )
        ],
        [
            InlineKeyboardButton(
                text=t("btn_ios", locale), callback_data="instruction_ios"
            )
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_pc_instructions_keyboard(locale: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                text=t("btn_windows_instructions", locale),
                callback_data="instruction_windows",
            )
        ],
        [
            InlineKeyboardButton(
                text=t("btn_macos_instructions", locale),
                callback_data="instruction_macos",
            )
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_my_devices_keyboard(devices: list[str], locale: str) -> ReplyKeyboardMarkup:
    keyboard = [[KeyboardButton(text=name)] for name in devices]
    keyboard.append([KeyboardButton(text=t("btn_back", locale))])
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_main_menu_inline(locale: str) -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton(text=t("btn_main_menu", locale), callback_data="main_menu")]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
