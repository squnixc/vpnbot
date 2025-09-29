from __future__ import annotations

from typing import Dict, Set

SUPPORTED_LOCALES = [
    "en",
    "ru",
    "ar",
    "be",
    "ca",
    "hr",
    "cs",
    "nl",
    "fi",
    "fr",
    "de",
    "he",
    "hu",
    "id",
    "it",
    "kk",
    "ko",
    "ms",
    "no",
    "fa",
    "pl",
    "pt-br",
    "ro",
    "sr",
    "sk",
    "es",
    "sv",
    "tr",
    "uk",
    "uz",
    "vi",
]

TEXTS: Dict[str, Dict[str, str]] = {
    "en": {
        "start_pitch": "🚀 Fast and easy access in Telegram.\nStay private, stable, and fast wherever you are.",
        "start_trial_granted": "🎁 Your bonus: 7 days for free!\nEnjoy fast and secure access without limits.",
        "status_header": "👋 <b>Here is information about your devices and subscription</b>",
        "status_plan_line": "📦 <b>Your plan:</b> {plan_title}",
        "status_devices_counter": "(<b>Devices:</b> {connected} / {limit})",
        "status_connections_header": "📟 <b>Connections</b>",
        "status_connections_empty": "No connected devices yet",
        "status_active_line": "🕒 <b>Subscription active:</b> {duration}",
        "status_bonus_line": "🎁 <b>Bonus:</b> +7 days for every invited friend!",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 seconds",
        "time_day_forms": "day|days|days",
        "time_hour_forms": "hour|hours|hours",
        "time_minute_forms": "minute|minutes|minutes",
        "time_second_forms": "second|seconds|seconds",
        "btn_intro_continue": "🚀 Let's go!",
        "btn_devices": "📟 Devices",
        "btn_subscription": "🔒 Subscription",
        "btn_invite_friend": "🤝 Invite a friend",
        "btn_questions": "❓ FAQ & Support",
        "btn_main_menu": "🏠 Main menu",
        "btn_back": "⬅️ Back",
        "btn_phone": "📱 Phone",
        "btn_computer": "💻 Computer",
        "btn_my_devices": "🔌 My devices",
        "btn_android": "📚 Android guide",
        "btn_ios": "📚 iPhone guide",
        "btn_windows_instructions": "🔴 Windows guide",
        "btn_macos_instructions": "🟢 macOS guide",
        "btn_share_link": "Share the link",
        "btn_pay_card": "💳 Bank card",
        "devices_choose": "Choose how you want to connect:",
        "devices_generation_in_progress": "⏳ Configuration is already being generated. Please wait for the file/QR.",
        "devices_limit_reached": "⚠️ Device limit reached. Remove one before adding a new device.",
        "device_ready_title": "✅ Configuration is ready!",
        "device_ready_body": "Scan the QR code or download the config file to connect.",
        "devices_pick_guide": "Need instructions? Choose your platform:",
        "devices_none": "You have no connected devices yet.",
        "devices_list_intro": "👇 Your connected devices:",
        "devices_select_prompt": "Please choose a device from the list.",
        "device_default_name": "Device {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide for Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide for iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide for Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide for macOS</a>",
        "subscription_intro": "Choose how many devices you want to connect:",
        "subscription_duration_prompt": "⏱️ Choose subscription duration:\n{options}",
        "subscription_duration_hint": "💡 Longer periods are cheaper per month.",
        "subscription_payment_thanks": (
            "🫶 Thank you for your trust!\n\n"
            "You are one step closer to a secure, stable, and fast internet.\n"
            "We made the process as convenient as possible.\n\n"
            "👇 Pick a payment method:"
        ),
        "subscription_payment_change": "🔁 Want to change the plan? Use the buttons below before paying.",
        "subscription_invalid_plan": "Please choose one of the available plans.",
        "subscription_invalid_duration": "Please choose one of the suggested durations.",
        "subscription_payment_created": "Payment created (mock)",
        "plan_devices_2_button": "💫 Devices: 2 - 99₽/month",
        "plan_devices_5_button": "✨ Devices: 5 - 169₽/month",
        "plan_devices_2_title": "2 devices",
        "plan_devices_5_title": "5 devices",
        "plan_devices_2_duration_1m": "1 month - 99₽",
        "plan_devices_2_duration_3m": "🔹3 months - 249₽",
        "plan_devices_2_duration_6m": "🔸6 months - 399₽",
        "plan_devices_5_duration_1m": "1 month - 169₽",
        "plan_devices_5_duration_3m": "🔹3 months - 449₽",
        "plan_devices_5_duration_6m": "🔸6 months - 749₽",
        "faq_title": "❓ Frequently asked questions",
        "faq_body": (
            "Find answers in our FAQ: {faq_url}\n"
            "Need help? Write to @{support_handle}.\n"
            "Your Telegram ID: {tg_id}"
        ),
        "referral_intro": (
            "🤝 Invite friends — get bonus days.\n\n"
            "Each friend who connects via your link gives you +7 days of subscription.\n\n"
            "Share the link and enjoy longer — for free."
        ),
        "referral_reward_notification": "🎉 Your friend joined!\nYou received +7 days to your subscription ✨",
        "plan_title_trial": "Trial period",
        "plan_title_device2": "2 devices",
        "plan_title_device5": "5 devices",
    },
    "ru": {
        "start_pitch": "🚀 Удобный сервис прямо в Telegram.\nСохраняй приватность и стабильность где угодно.",
        "start_trial_granted": "🎁 Твой бонус: 7 дней бесплатно!\nПопробуй быстрый и защищённый доступ без ограничений.",
        "status_header": "👋 <b>Вот информация о твоих устройствах и подписке</b>",
        "status_plan_line": "📦 <b>Твой план:</b> {plan_title}",
        "status_devices_counter": "(<b>Устройства:</b> {connected} / {limit})",
        "status_connections_header": "📟 <b>Подключения</b>",
        "status_connections_empty": "Пока нет подключений",
        "status_active_line": "🕒 <b>Подписка активна:</b> {duration}",
        "status_bonus_line": "🎁 <b>Бонус:</b> +7 дней за каждого приглашённого друга!",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 секунд",
        "time_day_forms": "день|дня|дней",
        "time_hour_forms": "час|часа|часов",
        "time_minute_forms": "минута|минуты|минут",
        "time_second_forms": "секунда|секунды|секунд",
        "btn_intro_continue": "🚀 Вперёд!",
        "btn_devices": "📟 Устройства",
        "btn_subscription": "🔒 Подписка",
        "btn_invite_friend": "🤝 Пригласить друга",
        "btn_questions": "❓ Вопросы и поддержка",
        "btn_main_menu": "🏠 Главное меню",
        "btn_back": "⬅️ Назад",
        "btn_phone": "📱 Телефон",
        "btn_computer": "💻 Компьютер",
        "btn_my_devices": "🔌 Мои устройства",
        "btn_android": "📚 Инструкция для Android",
        "btn_ios": "📚 Инструкция для iPhone",
        "btn_windows_instructions": "🔴 Инструкция для Windows",
        "btn_macos_instructions": "🟢 Инструкция для macOS",
        "btn_share_link": "Поделиться ссылкой",
        "btn_pay_card": "💳 Банковская карта",
        "devices_choose": "Выбери, как хочешь подключиться:",
        "devices_generation_in_progress": "⏳ Конфиг уже генерируется. Дождись файла или QR-кода.",
        "devices_limit_reached": "⚠️ Достигнут лимит устройств. Удали одно, чтобы добавить новое.",
        "device_ready_title": "✅ Конфигурация готова!",
        "device_ready_body": "Отсканируй QR-код или скачай конфиг, чтобы подключиться.",
        "devices_pick_guide": "Нужна инструкция? Выбери платформу:",
        "devices_none": "У тебя ещё нет подключённых устройств.",
        "devices_list_intro": "👇 Список твоих подключённых устройств:",
        "devices_select_prompt": "Пожалуйста, выбери устройство из списка.",
        "device_default_name": "Устройство {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Инструкция для Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Инструкция для iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Инструкция для Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Инструкция для macOS</a>",
        "subscription_intro": "Выбери, сколько устройств хочешь подключить:",
        "subscription_duration_prompt": "⏱️Выбери срок подписки:\n{options}",
        "subscription_duration_hint": "💡 Стоимость ниже при оплате за больший срок.",
        "subscription_payment_thanks": (
            "🫶 Спасибо за доверие!\n\n"
            "Ты на шаг ближе к безопасному, стабильному и быстрому интернету.\n"
            "Мы постарались сделать процесс максимально удобным.\n\n"
            "👇 Выбери подходящий способ оплаты:"
        ),
        "subscription_payment_change": "🔁 Чтобы изменить тариф до оплаты, воспользуйся кнопками ниже.",
        "subscription_invalid_plan": "Выбери один из доступных планов.",
        "subscription_invalid_duration": "Пожалуйста, выбери один из предложенных тарифов.",
        "subscription_payment_created": "Оплата создана (мок)",
        "plan_devices_2_button": "💫 Устройства: 2 - 99₽/мес.",
        "plan_devices_5_button": "✨ Устройства: 5 - 169₽/мес.",
        "plan_devices_2_title": "2 устройства",
        "plan_devices_5_title": "5 устройств",
        "plan_devices_2_duration_1m": "1 месяц - 99₽",
        "plan_devices_2_duration_3m": "🔹3 месяца - 249₽",
        "plan_devices_2_duration_6m": "🔸6 месяцев - 399₽",
        "plan_devices_5_duration_1m": "1 месяц - 169₽",
        "plan_devices_5_duration_3m": "🔹3 месяца - 449₽",
        "plan_devices_5_duration_6m": "🔸6 месяцев - 749₽",
        "faq_title": "❓ Частые вопросы",
        "faq_body": (
            "Ответы ищи в FAQ: {faq_url}\n"
            "Нужна помощь? Напиши @{support_handle}.\n"
            "Твой Telegram ID: {tg_id}"
        ),
        "referral_intro": (
            "🤝 Приглашай друзей — получай дни в подарок.\n\n"
            "За каждого подключившегося по твоей ссылке получи +7 дней к подписке.\n\n"
            "Поделись ссылкой и пользуйся дольше — бесплатно."
        ),
        "referral_reward_notification": "🎉 Ваш друг присоединился!\nВам начислено +7 дней к подписке ✨",
        "plan_title_trial": "Бесплатный период",
        "plan_title_device2": "2 устройства",
        "plan_title_device5": "5 устройств",
    },
}

for locale in SUPPORTED_LOCALES:
    TEXTS.setdefault(locale, {})


def normalize_locale(locale: str | None) -> str:
    if not locale:
        return "en"
    normalized = locale.lower().split("-")[0]
    if normalized in TEXTS:
        return normalized
    # handle Portuguese (Brazil)
    if normalized == "pt" and locale.lower() in ("pt-br", "pt_br"):
        return "pt-br"
    return "en"


def t(key: str, locale: str | None = None) -> str:
    language = normalize_locale(locale)
    translations = TEXTS.get(language, TEXTS["en"])
    if key in translations:
        value = translations[key]
        if value:
            return value
    fallback = TEXTS["en"].get(key)
    if fallback:
        return fallback
    return key


def get_all_translations(key: str) -> Set[str]:
    values: Set[str] = set()
    for translations in TEXTS.values():
        value = translations.get(key)
        if value:
            values.add(value)
    fallback = TEXTS["en"].get(key)
    if fallback:
        values.add(fallback)
    if not values:
        values.add(key)
    return values
