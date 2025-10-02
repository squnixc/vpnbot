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
        "status_header": "👋 Here is information about your devices and subscription",
        "status_plan_line": "📦 Your plan: {plan_title}",
        "status_devices_counter": "(Devices: {connected} / {limit})",
        "status_connections_header": "📟 Connections:",
        "status_connections_empty": "No connected devices yet",
        "status_active_line": "🕒 Subscription active: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 days for every invited friend",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 seconds",
        "time_day_forms": "day|days|days",
        "time_hour_forms": "hour|hours|hours",
        "time_minute_forms": "minute|minutes|minutes",
        "time_second_forms": "second|seconds|seconds",
        "btn_intro_continue": "🚀 Let's go!",
        "btn_devices": "📱 Devices",
        "btn_subscription": "💎 Subscription",
        "btn_invite_friend": "🤝 Invite a friend",
        "btn_questions": "❓ Questions",
        "btn_main_menu": "🏠 Main menu",
        "btn_back": "⬅️ Back",
        "btn_phone": "📱 Phone",
        "btn_computer": "💻 Computer",
        "btn_my_devices": "🔌 My devices",
        "btn_android": "🔴 Android guide",
        "btn_ios": "🟢 iPhone guide",
        "btn_windows_instructions": "🔴 Windows guide",
        "btn_macos_instructions": "🟢 MacOS guide",
        "btn_share_link": "Share the link",
        "btn_pay_card": "💳 Bank card",
        "devices_choose": (
            "📲 Choose the device you want to connect.\n"
            "(It only takes a couple of minutes — super simple!)"
        ),
        "devices_generation_in_progress": "⏳ Configuration is already being generated. Please wait for the file/QR.",
        "devices_limit_reached": "⚠️ Device limit reached. Remove one before adding a new device.",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Setup is almost done!\n\n"
            "Choose how you want to connect:\n"
            "1. Download the profile file and import it to AmneziaWG / WireGuard\n"
            "2. Scan the QR code right in the app\n\n"
            "📚 Pick the right guide and connect in just a few steps.\n\n"
            "⚠️ Each profile can be used on a single device only!"
        ),
        "devices_pick_guide": "📖 Below are guides for different systems — choose yours and follow the steps.",
        "devices_none": "You have no connected devices yet.",
        "devices_list_intro": "👇 Your connected devices:",
        "devices_select_prompt": "Please choose a device from the list.",
        "device_default_name": "Device {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide for Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide for iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide for Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide for macOS</a>",
        "subscription_intro": (
            "💎 Subscription\n"
            "✨ What you get with the subscription:\n"
            "• Fast and secure access to your services\n"
            "• No ads or distractions\n"
            "• Best price — just 99₽ per month! 🔥\n\n"
            "👉 Pick a plan for 2 or 5 devices at once."
        ),
        "subscription_duration_prompt": "⏱️ Choose subscription duration:\n{options}",
        "subscription_duration_hint": "💡 Longer periods cost less per month.",
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
        "faq_title": "❓ Questions",
        "faq_body": (
            "❓ How, what, and why?\n"
            "We collected the most popular questions in one article.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Your support ID: {tg_id}\n\n"
            "🗺 Need help? Write to @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Invite friends — get bonus days.\n\n"
            "Every friend who connects using your link adds +7 days to your subscription.\n\n"
            "Share the link and keep browsing longer for free."
        ),
        "referral_reward_notification": "🎉 Your friend joined!\nYou received +7 days to your subscription ✨",
        "plan_title_trial": "Trial period",
        "plan_title_device2": "2 devices",
        "plan_title_device5": "5 devices",
    },
    "ru": {
        "start_pitch": "🚀 Удобный сервис прямо в Telegram.\nСохраняй приватность и стабильность где угодно.",
        "start_trial_granted": "🎁 Твой бонус: 7 дней бесплатно!\nПопробуй быстрый и защищённый доступ без ограничений.",
        "status_header": (
            "👋 Ваши устройства и статус доступа\n\n"
            "Здесь можно узнать какие устройства у тебя подключены и статус подписки."
        ),
        "status_plan_line": "📦 Ваш план: {plan_title}",
        "status_devices_counter": "(Устройства: {connected} / {limit})",
        "status_connections_header": "📟 Подключения:",
        "status_connections_empty": "Пока нет подключений",
        "status_active_line": "⏱️Подписка активна: {duration}",
        "status_bonus_line": "🎁 Бонус: +7 дней за каждого приглашённого друга",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 секунд",
        "time_day_forms": "день|дня|дней",
        "time_hour_forms": "час|часа|часов",
        "time_minute_forms": "минута|минуты|минут",
        "time_second_forms": "секунда|секунды|секунд",
        "btn_intro_continue": "🚀 Вперёд!",
        "btn_devices": "📱 Устройства",
        "btn_subscription": "💎 Подписка",
        "btn_invite_friend": "🤝 Пригласить друга",
        "btn_questions": "❓ Вопросы",
        "btn_main_menu": "🏠 Главное меню",
        "btn_back": "⬅️ Назад",
        "btn_phone": "📱 Телефон",
        "btn_computer": "💻 Компьютер",
        "btn_my_devices": "🔌 Мои устройства",
        "btn_android": "🔴Инструкция для Android",
        "btn_ios": "🟢Инструкция для iPhone",
        "btn_windows_instructions": "🔴Инструкция для Windows",
        "btn_macos_instructions": "🟢Инструкция для MacOS",
        "btn_share_link": "Поделиться ссылкой",
        "btn_pay_card": "💳 Банковская карта",
        "devices_choose": (
            "📲 Выбери устройство, которое хочешь подключить.\n"
            "(Это займёт всего пару минут — всё просто!)"
        ),
        "devices_generation_in_progress": "⏳ Конфиг уже генерируется. Дождись файла или QR-кода.",
        "devices_limit_reached": "⚠️ Достигнут лимит подключений на этом тарифе",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Подключение почти готово!\n\n"
            "Выбери удобный способ:\n"
            "1. Скачать файл профиля и импортировать в AmneziaWG / WireGuard\n"
            "2. Отсканировать QR-код прямо в приложении\n\n"
            "📚 Выбери подходящую инструкцию и подключись за пару шагов.\n\n"
            "⚠️ Один профиль можно использовать только на одном устройстве!"
        ),
        "devices_pick_guide": "📖 Ниже есть инструкции для разных устройств — выбери свою ОС и следуй шагам.",
        "devices_none": "⛓️‍💥 У тебя пока нет подключённых устройств",
        "devices_list_intro": "👇 Список твоих подключённых устройств:",
        "devices_select_prompt": "Пожалуйста, выбери устройство из списка.",
        "device_default_name": "Устройство {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Инструкция для Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Инструкция для iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Инструкция для Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Инструкция для macOS</a>",
        "subscription_intro": (
            "✨ Что даёт подписка:\n"
            "• Быстрый и защищённый доступ к твоим сервисам!\n"
            "• Никакой рекламы и отвлекающих элементов.\n"
            "• Минимальная цена — всего 99₽ в месяц!🔥\n\n"
            "👉 Выбирай план: для 2 или 5 устройств одновременно."
        ),
        "subscription_duration_prompt": "⏱️Выбери срок подписки:\n{options}",
        "subscription_duration_hint": "💡Стоимость ниже при оплате на длительный срок.",
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
        "faq_title": "❓ Что, как и почему?",
        "faq_body": (
            "Мы собрали частые вопросы в одной статье.\n"
            "📖 ЧаВо: {faq_url}\n\n"
            "Ваш ID для обращения: {tg_id}\n\n"
            "🗺 Есть вопросы? Напишите нам: @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Приглашай друзей — получай дни в подарок.\n\n"
            "За каждого подключившегося по твоей ссылке — +7 дней к твоей подписке.\n\n"
            "Поделись ссылкой и пользуйся дольше — бесплатно."
        ),
        "referral_reward_notification": "🎉 Ваш друг присоединился!\nВам начислено +7 дней к подписке ✨",
        "plan_title_trial": "Бесплатный период",
        "plan_title_device2": "2 устройства",
        "plan_title_device5": "5 устройств",
    },
    "ar": {
        "start_pitch": "🚀 وصول سريع وسهل مباشرة في تيليغرام.\nحافظ على الخصوصية والاستقرار أينما كنت.",
        "start_trial_granted": "🎁 هديتك: 7 أيام مجاناً!\nاستمتع بوصول سريع وآمن بلا حدود.",
        "status_header": "👋 إليك معلومات عن أجهزتك واشتراكك",
        "status_plan_line": "📦 خطتك: {plan_title}",
        "status_devices_counter": "(الأجهزة: {connected} / {limit})",
        "status_connections_header": "📟 الاتصالات:",
        "status_connections_empty": "لا توجد أجهزة متصلة بعد",
        "status_active_line": "🕒 الاشتراك فعّال لمدة: {duration}",
        "status_bonus_line": "🎁 مكافأة: +7 أيام عن كل صديق تدعوه",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 ثانية",
        "time_day_forms": "يوم|يومان|أيام",
        "time_hour_forms": "ساعة|ساعتان|ساعات",
        "time_minute_forms": "دقيقة|دقيقتان|دقائق",
        "time_second_forms": "ثانية|ثانيتان|ثوانٍ",
        "btn_intro_continue": "🚀 هيا بنا!",
        "btn_devices": "📱 الأجهزة",
        "btn_subscription": "💎 الاشتراك",
        "btn_invite_friend": "🤝 دعوة صديق",
        "btn_questions": "❓ الأسئلة",
        "btn_main_menu": "🏠 القائمة الرئيسية",
        "btn_back": "⬅️ رجوع",
        "btn_phone": "📱 هاتف",
        "btn_computer": "💻 كمبيوتر",
        "btn_my_devices": "🔌 أجهزتي",
        "btn_android": "🔴 دليل Android",
        "btn_ios": "🟢 دليل iPhone",
        "btn_windows_instructions": "🔴 دليل Windows",
        "btn_macos_instructions": "🟢 دليل macOS",
        "btn_share_link": "مشاركة الرابط",
        "btn_pay_card": "💳 بطاقة مصرفية",
        "devices_choose": (
            "📲 اختر الجهاز الذي تريد توصيله.\n"
            "(لن يستغرق الأمر سوى بضع دقائق — الأمر سهل للغاية!)"
        ),
        "devices_generation_in_progress": "⏳ يتم إنشاء الإعدادات بالفعل. يرجى انتظار الملف أو رمز QR.",
        "devices_limit_reached": "⚠️ تم الوصول إلى حد الأجهزة. احذف جهازاً قبل إضافة جهاز جديد.",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 الإعداد أصبح شبه جاهز!\n\n"
            "اختر الطريقة المناسبة لك:\n"
            "1. نزّل ملف التكوين واستورده في AmneziaWG / WireGuard\n"
            "2. امسح رمز QR مباشرة داخل التطبيق\n\n"
            "📚 اختر الدليل المناسب واتصل في بضع خطوات فقط.\n\n"
            "⚠️ يمكن استخدام كل ملف تعريف على جهاز واحد فقط!"
        ),
        "devices_pick_guide": "📖 أدناه أدلة للأنظمة المختلفة — اختر نظامك واتبع الخطوات.",
        "devices_none": "ليس لديك أجهزة متصلة بعد.",
        "devices_list_intro": "👇 أجهزتك المتصلة:",
        "devices_select_prompt": "يرجى اختيار جهاز من القائمة.",
        "device_default_name": "الجهاز {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 دليل Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 دليل iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 دليل Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 دليل macOS</a>",
        "subscription_intro": (
            "💎 الاشتراك\n"
            "✨ ما الذي تحصل عليه مع الاشتراك:\n"
            "• وصول سريع وآمن إلى خدماتك\n"
            "• دون إعلانات أو تشتيت\n"
            "• أفضل سعر — فقط 99₽ في الشهر! 🔥\n\n"
            "👉 اختر خطة لجهازين أو خمسة أجهزة في آن واحد."
        ),
        "subscription_duration_prompt": "⏱️ اختر مدة الاشتراك:\n{options}",
        "subscription_duration_hint": "💡 كلما كانت المدة أطول كان السعر الشهري أقل.",
        "subscription_payment_thanks": (
            "🫶 شكراً لثقتك!\n\n"
            "أنت على بعد خطوة من إنترنت آمن ومستقر وسريع.\n"
            "جعلنا العملية مريحة قدر الإمكان.\n\n"
            "👇 اختر طريقة الدفع:"
        ),
        "subscription_payment_change": "🔁 تريد تغيير الخطة؟ استخدم الأزرار أدناه قبل الدفع.",
        "subscription_invalid_plan": "يرجى اختيار إحدى الخطط المتاحة.",
        "subscription_invalid_duration": "يرجى اختيار إحدى الفترات المقترحة.",
        "subscription_payment_created": "تم إنشاء الدفع (تجريبي)",
        "plan_devices_2_button": "💫 الأجهزة: 2 - 99₽/شهر",
        "plan_devices_5_button": "✨ الأجهزة: 5 - 169₽/شهر",
        "plan_devices_2_title": "جهازان",
        "plan_devices_5_title": "5 أجهزة",
        "plan_devices_2_duration_1m": "1 شهر - 99₽",
        "plan_devices_2_duration_3m": "🔹3 أشهر - 249₽",
        "plan_devices_2_duration_6m": "🔸6 أشهر - 399₽",
        "plan_devices_5_duration_1m": "1 شهر - 169₽",
        "plan_devices_5_duration_3m": "🔹3 أشهر - 449₽",
        "plan_devices_5_duration_6m": "🔸6 أشهر - 749₽",
        "faq_title": "❓ الأسئلة",
        "faq_body": (
            "❓ كيف وماذا ولماذا؟\n"
            "جمعنا أكثر الأسئلة شيوعاً في مقال واحد.\n"
            "📖 الأسئلة الشائعة: {faq_url}\n\n"
            "معرّف الدعم الخاص بك: {tg_id}\n\n"
            "🗺 هل تحتاج إلى مساعدة؟ اكتب إلى @{support_handle}"
        ),
        "referral_intro": (
            "🤝 ادعُ الأصدقاء — واحصل على أيام إضافية.\n\n"
            "كل صديق يتصل عبر رابطك يضيف +7 أيام إلى اشتراكك.\n\n"
            "شارك الرابط وتصفح لفترة أطول مجاناً."
        ),
        "referral_reward_notification": "🎉 انضم صديقك!\nحصلت على +7 أيام لاشتراكك ✨",
        "plan_title_trial": "فترة تجريبية",
        "plan_title_device2": "جهازان",
        "plan_title_device5": "5 أجهزة",
    },
    "be": {
        "start_pitch": "🚀 Хуткі і просты доступ прама ў Telegram.\nЗахоўвай прыватнасць і стабільнасць дзе б ты ні быў.",
        "start_trial_granted": "🎁 Твой бонус: 7 дзён бясплатна!\nАтрымай хуткі і абаронены доступ без абмежаванняў.",
        "status_header": (
            "👋 Твае прылады і статус падпіскі\n\n"
            "Тут можна паглядзець, якія прылады падключаныя і які ў цябе план."
        ),
        "status_plan_line": "📦 Твой план: {plan_title}",
        "status_devices_counter": "(Прылады: {connected} / {limit})",
        "status_connections_header": "📟 Падключэнні:",
        "status_connections_empty": "Пакуль няма падключэнняў",
        "status_active_line": "🕒 Падпіска дзейнічае: {duration}",
        "status_bonus_line": "🎁 Бонус: +7 дзён за кожнага запрошанага сябра",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 секунд",
        "time_day_forms": "дзень|дні|дзён",
        "time_hour_forms": "гадзіна|гадзіны|гадзін",
        "time_minute_forms": "хвіліна|хвіліны|хвілін",
        "time_second_forms": "секунда|секунды|секунд",
        "btn_intro_continue": "🚀 Пачынаем!",
        "btn_devices": "📱 Прылады",
        "btn_subscription": "💎 Падпіска",
        "btn_invite_friend": "🤝 Запрасіць сябра",
        "btn_questions": "❓ Пытанні",
        "btn_main_menu": "🏠 Галоўнае меню",
        "btn_back": "⬅️ Назад",
        "btn_phone": "📱 Тэлефон",
        "btn_computer": "💻 Камп'ютар",
        "btn_my_devices": "🔌 Мой спіс прылад",
        "btn_android": "🔴 Інструкцыя для Android",
        "btn_ios": "🟢 Інструкцыя для iPhone",
        "btn_windows_instructions": "🔴 Інструкцыя для Windows",
        "btn_macos_instructions": "🟢 Інструкцыя для macOS",
        "btn_share_link": "Падзяліцца спасылкай",
        "btn_pay_card": "💳 Банкаўская карта",
        "devices_choose": (
            "📲 Абяры прыладу, якую хочаш падключыць.\n"
            "(Гэта зойме ўсяго некалькі хвілін — усё вельмі проста!)"
        ),
        "devices_generation_in_progress": "⏳ Канфіг ужо ствараецца. Пачакай файл або QR-код.",
        "devices_limit_reached": "⚠️ Дасягнуты ліміт падключэнняў у гэтым тарыфе",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Падключэнне амаль гатова!\n\n"
            "Абяры зручны спосаб:\n"
            "1. Спампуй файл профілю і імпартуй у AmneziaWG / WireGuard\n"
            "2. Адсканіруй QR-код проста ў дадатку\n\n"
            "📚 Абяры патрэбную інструкцыю і падключыся ў некалькі крокаў.\n\n"
            "⚠️ Адзін профіль можна выкарыстоўваць толькі на адной прыладзе!"
        ),
        "devices_pick_guide": "📖 Ніжэй інструкцыі для розных сістэм — абяры сваю і выконвай крокі.",
        "devices_none": "Пакуль няма падключаных прылад.",
        "devices_list_intro": "👇 Спіс тваіх падключаных прылад:",
        "devices_select_prompt": "Калі ласка, абяры прыладу са спісу.",
        "device_default_name": "Прылада {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Інструкцыя для Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Інструкцыя для iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Інструкцыя для Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Інструкцыя для macOS</a>",
        "subscription_intro": (
            "💎 Падпіска\n"
            "✨ Што дае падпіска:\n"
            "• Хуткі і абаронены доступ да тваіх сэрвісаў\n"
            "• Ніякай рэкламы і перашкод\n"
            "• Лепшая цана — усяго 99₽ у месяц! 🔥\n\n"
            "👉 Абяры план для 2 або 5 прылад адразу."
        ),
        "subscription_duration_prompt": "⏱️ Абяры працягласць падпіскі:\n{options}",
        "subscription_duration_hint": "💡 Чым даўжэй перыяд, тым ніжэй кошт за месяц.",
        "subscription_payment_thanks": (
            "🫶 Дзякуй за давер!\n\n"
            "Ты на крок бліжэй да бяспечнага, стабільнага і хуткага інтэрнэту.\n"
            "Мы зрабілі працэс максімальна зручным.\n\n"
            "👇 Абяры спосаб аплаты:"
        ),
        "subscription_payment_change": "🔁 Хочаш змяніць план? Скарыстайся кнопкамі ніжэй да аплаты.",
        "subscription_invalid_plan": "Абяры адзін з даступных планаў.",
        "subscription_invalid_duration": "Калі ласка, абяры адну з прапанаваных працягласцяў.",
        "subscription_payment_created": "Аплата створана (тэст)",
        "plan_devices_2_button": "💫 Прылады: 2 - 99₽/мес.",
        "plan_devices_5_button": "✨ Прылады: 5 - 169₽/мес.",
        "plan_devices_2_title": "2 прылады",
        "plan_devices_5_title": "5 прылад",
        "plan_devices_2_duration_1m": "1 месяц - 99₽",
        "plan_devices_2_duration_3m": "🔹3 месяцы - 249₽",
        "plan_devices_2_duration_6m": "🔸6 месяцаў - 399₽",
        "plan_devices_5_duration_1m": "1 месяц - 169₽",
        "plan_devices_5_duration_3m": "🔹3 месяцы - 449₽",
        "plan_devices_5_duration_6m": "🔸6 месяцаў - 749₽",
        "faq_title": "❓ Пытанні",
        "faq_body": (
            "❓ Што і як?\n"
            "Мы сабралі самыя частыя пытанні ў адным матэрыяле.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Твой ID падтрымкі: {tg_id}\n\n"
            "🗺 Патрэбна дапамога? Напішы @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Запрашай сяброў — атрымлівай дні ў падарунак.\n\n"
            "За кожнага, хто падключыцца па тваёй спасылцы, — +7 дзён да падпіскі.\n\n"
            "Падзяліся спасылкай і карыстайся даўжэй бясплатна."
        ),
        "referral_reward_notification": "🎉 Твой сябар далучыўся!\nМы налічылі +7 дзён да падпіскі ✨",
        "plan_title_trial": "Пробны перыяд",
        "plan_title_device2": "2 прылады",
        "plan_title_device5": "5 прылад",
    },
    "ca": {
        "start_pitch": "🚀 Accés ràpid i fàcil directament a Telegram.\nMantén la privacitat i l'estabilitat siguis on siguis.",
        "start_trial_granted": "🎁 El teu bonus: 7 dies gratis!\nGaudeix d'un accés ràpid i segur sense límits.",
        "status_header": (
            "👋 Els teus dispositius i l'estat de la subscripció\n\n"
            "Aquí pots veure quins dispositius tens connectats i quin pla tens."
        ),
        "status_plan_line": "📦 El teu pla: {plan_title}",
        "status_devices_counter": "(Dispositius: {connected} / {limit})",
        "status_connections_header": "📟 Connexions:",
        "status_connections_empty": "Encara no hi ha connexions",
        "status_active_line": "🕒 Subscripció activa: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 dies per cada amic convidat",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 segons",
        "time_day_forms": "dia|dies|dies",
        "time_hour_forms": "hora|hores|hores",
        "time_minute_forms": "minut|minuts|minuts",
        "time_second_forms": "segon|segons|segons",
        "btn_intro_continue": "🚀 Som-hi!",
        "btn_devices": "📱 Dispositius",
        "btn_subscription": "💎 Subscripció",
        "btn_invite_friend": "🤝 Convida un amic",
        "btn_questions": "❓ Preguntes",
        "btn_main_menu": "🏠 Menú principal",
        "btn_back": "⬅️ Enrere",
        "btn_phone": "📱 Telèfon",
        "btn_computer": "💻 Ordinador",
        "btn_my_devices": "🔌 Els meus dispositius",
        "btn_android": "🔴 Guia per a Android",
        "btn_ios": "🟢 Guia per a iPhone",
        "btn_windows_instructions": "🔴 Guia per a Windows",
        "btn_macos_instructions": "🟢 Guia per a macOS",
        "btn_share_link": "Comparteix l'enllaç",
        "btn_pay_card": "💳 Targeta bancària",
        "devices_choose": (
            "📲 Tria el dispositiu que vols connectar.\n"
            "(Només et portarà uns minuts — és molt fàcil!)"
        ),
        "devices_generation_in_progress": "⏳ La configuració ja s'està generant. Espera el fitxer o el codi QR.",
        "devices_limit_reached": "⚠️ Has arribat al límit de dispositius en aquest pla",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 La configuració ja gairebé està llesta!\n\n"
            "Tria la manera més còmoda:\n"
            "1. Descarrega el fitxer del perfil i importa'l a AmneziaWG / WireGuard\n"
            "2. Escaneja el codi QR directament des de l'aplicació\n\n"
            "📚 Tria la guia adequada i connecta't en pocs passos.\n\n"
            "⚠️ Cada perfil només es pot utilitzar en un dispositiu!"
        ),
        "devices_pick_guide": "📖 A continuació tens guies per a diferents sistemes — tria el teu i segueix els passos.",
        "devices_none": "Encara no tens dispositius connectats.",
        "devices_list_intro": "👇 Llista dels teus dispositius connectats:",
        "devices_select_prompt": "Si us plau, tria un dispositiu de la llista.",
        "device_default_name": "Dispositiu {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guia per a Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guia per a iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guia per a Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guia per a macOS</a>",
        "subscription_intro": (
            "💎 Subscripció\n"
            "✨ Què inclou la subscripció:\n"
            "• Accés ràpid i segur als teus serveis\n"
            "• Sense anuncis ni distraccions\n"
            "• El millor preu — només 99₽ al mes! 🔥\n\n"
            "👉 Tria un pla per a 2 o 5 dispositius alhora."
        ),
        "subscription_duration_prompt": "⏱️ Tria la durada de la subscripció:\n{options}",
        "subscription_duration_hint": "💡 Períodes més llargs costen menys al mes.",
        "subscription_payment_thanks": (
            "🫶 Gràcies per la confiança!\n\n"
            "Ets a un pas d'un internet segur, estable i ràpid.\n"
            "Hem fet el procés tan còmode com hem pogut.\n\n"
            "👇 Tria la forma de pagament:"
        ),
        "subscription_payment_change": "🔁 Vols canviar el pla? Utilitza els botons de sota abans de pagar.",
        "subscription_invalid_plan": "Tria un dels plans disponibles.",
        "subscription_invalid_duration": "Si us plau, tria una de les durades proposades.",
        "subscription_payment_created": "Pagament creat (prova)",
        "plan_devices_2_button": "💫 Dispositius: 2 - 99₽/mes",
        "plan_devices_5_button": "✨ Dispositius: 5 - 169₽/mes",
        "plan_devices_2_title": "2 dispositius",
        "plan_devices_5_title": "5 dispositius",
        "plan_devices_2_duration_1m": "1 mes - 99₽",
        "plan_devices_2_duration_3m": "🔹3 mesos - 249₽",
        "plan_devices_2_duration_6m": "🔸6 mesos - 399₽",
        "plan_devices_5_duration_1m": "1 mes - 169₽",
        "plan_devices_5_duration_3m": "🔹3 mesos - 449₽",
        "plan_devices_5_duration_6m": "🔸6 mesos - 749₽",
        "faq_title": "❓ Preguntes",
        "faq_body": (
            "❓ Com, què i per què?\n"
            "Hem reunit les preguntes més habituals en un sol article.\n"
            "📖 Preguntes freqüents: {faq_url}\n\n"
            "El teu ID de suport: {tg_id}\n\n"
            "🗺 Necessites ajuda? Escriu a @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Convida amics — aconsegueix dies extra.\n\n"
            "Per cada amic que es connecti amb el teu enllaç — +7 dies a la subscripció.\n\n"
            "Comparteix l'enllaç i navega més temps gratis."
        ),
        "referral_reward_notification": "🎉 El teu amic s'ha unit!\nHas rebut +7 dies a la subscripció ✨",
        "plan_title_trial": "Període de prova",
        "plan_title_device2": "2 dispositius",
        "plan_title_device5": "5 dispositius",
    },
    "hr": {
        "start_pitch": "🚀 Brz i jednostavan pristup direktno u Telegramu.\nZadrži privatnost i stabilnost gdje god bio.",
        "start_trial_granted": "🎁 Tvoj bonus: 7 dana besplatno!\nIsprobaj brz i siguran pristup bez ograničenja.",
        "status_header": (
            "👋 Tvoji uređaji i status pretplate\n\n"
            "Ovdje možeš vidjeti koji su uređaji povezani i koji plan koristiš."
        ),
        "status_plan_line": "📦 Tvoj plan: {plan_title}",
        "status_devices_counter": "(Uređaji: {connected} / {limit})",
        "status_connections_header": "📟 Veze:",
        "status_connections_empty": "Još nema povezanih uređaja",
        "status_active_line": "🕒 Pretplata aktivna: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 dana za svakog pozvanog prijatelja",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 sekundi",
        "time_day_forms": "dan|dana|dana",
        "time_hour_forms": "sat|sata|sati",
        "time_minute_forms": "minuta|minute|minuta",
        "time_second_forms": "sekunda|sekunde|sekundi",
        "btn_intro_continue": "🚀 Krenimo!",
        "btn_devices": "📱 Uređaji",
        "btn_subscription": "💎 Pretplata",
        "btn_invite_friend": "🤝 Pozovi prijatelja",
        "btn_questions": "❓ Pitanja",
        "btn_main_menu": "🏠 Glavni izbornik",
        "btn_back": "⬅️ Natrag",
        "btn_phone": "📱 Telefon",
        "btn_computer": "💻 Računalo",
        "btn_my_devices": "🔌 Moji uređaji",
        "btn_android": "🔴 Upute za Android",
        "btn_ios": "🟢 Upute za iPhone",
        "btn_windows_instructions": "🔴 Upute za Windows",
        "btn_macos_instructions": "🟢 Upute za macOS",
        "btn_share_link": "Podijeli poveznicu",
        "btn_pay_card": "💳 Bankovna kartica",
        "devices_choose": (
            "📲 Odaberi uređaj koji želiš povezati.\n"
            "(Trebat će ti samo nekoliko minuta — vrlo je jednostavno!)"
        ),
        "devices_generation_in_progress": "⏳ Konfiguracija se već generira. Pričekaj datoteku ili QR kod.",
        "devices_limit_reached": "⚠️ Dosegnuto je ograničenje uređaja na ovom paketu",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Povezivanje je gotovo spremno!\n\n"
            "Odaberi način koji ti odgovara:\n"
            "1. Preuzmi profil i uvezi ga u AmneziaWG / WireGuard\n"
            "2. Skeniraj QR kod izravno u aplikaciji\n\n"
            "📚 Odaberi odgovarajući priručnik i poveži se u nekoliko koraka.\n\n"
            "⚠️ Svaki profil može se koristiti samo na jednom uređaju!"
        ),
        "devices_pick_guide": "📖 U nastavku su upute za različite sustave — odaberi svoj i slijedi korake.",
        "devices_none": "Još nemaš povezanih uređaja.",
        "devices_list_intro": "👇 Popis tvojih povezanih uređaja:",
        "devices_select_prompt": "Odaberi uređaj s popisa.",
        "device_default_name": "Uređaj {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Upute za Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Upute za iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Upute za Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Upute za macOS</a>",
        "subscription_intro": (
            "💎 Pretplata\n"
            "✨ Što dobivaš s pretplatom:\n"
            "• Brz i siguran pristup svojim servisima\n"
            "• Bez oglasa i ometanja\n"
            "• Najbolja cijena — samo 99₽ mjesečno! 🔥\n\n"
            "👉 Odaberi plan za 2 ili 5 uređaja odjednom."
        ),
        "subscription_duration_prompt": "⏱️ Odaberi trajanje pretplate:\n{options}",
        "subscription_duration_hint": "💡 Duži period znači manju cijenu po mjesecu.",
        "subscription_payment_thanks": (
            "🫶 Hvala na povjerenju!\n\n"
            "Samo si korak do sigurnog, stabilnog i brzog interneta.\n"
            "Proces smo učinili što ugodnijim.\n\n"
            "👇 Odaberi način plaćanja:"
        ),
        "subscription_payment_change": "🔁 Želiš promijeniti plan? Koristi gumbe ispod prije plaćanja.",
        "subscription_invalid_plan": "Odaberi jedan od dostupnih planova.",
        "subscription_invalid_duration": "Molimo odaberi jednu od ponuđenih opcija trajanja.",
        "subscription_payment_created": "Plaćanje kreirano (test)",
        "plan_devices_2_button": "💫 Uređaji: 2 - 99₽/mj.",
        "plan_devices_5_button": "✨ Uređaji: 5 - 169₽/mj.",
        "plan_devices_2_title": "2 uređaja",
        "plan_devices_5_title": "5 uređaja",
        "plan_devices_2_duration_1m": "1 mjesec - 99₽",
        "plan_devices_2_duration_3m": "🔹3 mjeseca - 249₽",
        "plan_devices_2_duration_6m": "🔸6 mjeseci - 399₽",
        "plan_devices_5_duration_1m": "1 mjesec - 169₽",
        "plan_devices_5_duration_3m": "🔹3 mjeseca - 449₽",
        "plan_devices_5_duration_6m": "🔸6 mjeseci - 749₽",
        "faq_title": "❓ Pitanja",
        "faq_body": (
            "❓ Kako, što i zašto?\n"
            "Najčešća pitanja prikupili smo u jednom članku.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Tvoj ID podrške: {tg_id}\n\n"
            "🗺 Trebaš pomoć? Piši @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Pozovi prijatelje — osvoji dodatne dane.\n\n"
            "Za svakog tko se poveže preko tvoje poveznice dobivaš +7 dana pretplate.\n\n"
            "Podijeli poveznicu i surfaj dulje besplatno."
        ),
        "referral_reward_notification": "🎉 Tvoj prijatelj se pridružio!\nDodali smo ti +7 dana pretplate ✨",
        "plan_title_trial": "Probno razdoblje",
        "plan_title_device2": "2 uređaja",
        "plan_title_device5": "5 uređaja",
    },
    "cs": {
        "start_pitch": "🚀 Rychlý a snadný přístup přímo v Telegramu.\nUdržuj soukromí a stabilitu, ať jsi kdekoli.",
        "start_trial_granted": "🎁 Tvůj bonus: 7 dní zdarma!\nVyzkoušej rychlý a bezpečný přístup bez omezení.",
        "status_header": (
            "👋 Tvá zařízení a stav předplatného\n\n"
            "Zde zjistíš, která zařízení máš připojená a jaký plán používáš."
        ),
        "status_plan_line": "📦 Tvůj plán: {plan_title}",
        "status_devices_counter": "(Zařízení: {connected} / {limit})",
        "status_connections_header": "📟 Připojení:",
        "status_connections_empty": "Zatím žádná připojení",
        "status_active_line": "🕒 Předplatné aktivní: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 dní za každého pozvaného přítele",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 sekund",
        "time_day_forms": "den|dny|dnů",
        "time_hour_forms": "hodina|hodiny|hodin",
        "time_minute_forms": "minuta|minuty|minut",
        "time_second_forms": "sekunda|sekundy|sekund",
        "btn_intro_continue": "🚀 Jdeme na to!",
        "btn_devices": "📱 Zařízení",
        "btn_subscription": "💎 Předplatné",
        "btn_invite_friend": "🤝 Pozvat přítele",
        "btn_questions": "❓ Otázky",
        "btn_main_menu": "🏠 Hlavní menu",
        "btn_back": "⬅️ Zpět",
        "btn_phone": "📱 Telefon",
        "btn_computer": "💻 Počítač",
        "btn_my_devices": "🔌 Moje zařízení",
        "btn_android": "🔴 Návod pro Android",
        "btn_ios": "🟢 Návod pro iPhone",
        "btn_windows_instructions": "🔴 Návod pro Windows",
        "btn_macos_instructions": "🟢 Návod pro macOS",
        "btn_share_link": "Sdílet odkaz",
        "btn_pay_card": "💳 Bankovní karta",
        "devices_choose": (
            "📲 Vyber zařízení, které chceš připojit.\n"
            "(Zabere to jen pár minut — je to opravdu jednoduché!)"
        ),
        "devices_generation_in_progress": "⏳ Konfigurace se už vytváří. Počkej na soubor nebo QR kód.",
        "devices_limit_reached": "⚠️ Byl dosažen limit zařízení pro tento tarif",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Připojení je téměř hotové!\n\n"
            "Vyber si vhodný způsob:\n"
            "1. Stáhni soubor profilu a importuj ho do AmneziaWG / WireGuard\n"
            "2. Naskenuj QR kód přímo v aplikaci\n\n"
            "📚 Vyber si správný návod a připoj se během pár kroků.\n\n"
            "⚠️ Každý profil lze použít pouze na jednom zařízení!"
        ),
        "devices_pick_guide": "📖 Níže najdeš návody pro různé systémy — vyber si svůj a postupuj podle kroků.",
        "devices_none": "Zatím nemáš žádná připojená zařízení.",
        "devices_list_intro": "👇 Seznam tvých připojených zařízení:",
        "devices_select_prompt": "Vyber zařízení ze seznamu.",
        "device_default_name": "Zařízení {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Návod pro Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Návod pro iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Návod pro Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Návod pro macOS</a>",
        "subscription_intro": (
            "💎 Předplatné\n"
            "✨ Co získáš s předplatným:\n"
            "• Rychlý a bezpečný přístup ke svým službám\n"
            "• Žádné reklamy ani rozptýlení\n"
            "• Nejlepší cena — jen 99₽ měsíčně! 🔥\n\n"
            "👉 Vyber si plán pro 2 nebo 5 zařízení najednou."
        ),
        "subscription_duration_prompt": "⏱️ Vyber délku předplatného:\n{options}",
        "subscription_duration_hint": "💡 Delší období znamená nižší cenu za měsíc.",
        "subscription_payment_thanks": (
            "🫶 Děkujeme za důvěru!\n\n"
            "Jsi o krok blíž k bezpečnému, stabilnímu a rychlému internetu.\n"
            "Proces jsme udělali co nejpohodlnější.\n\n"
            "👇 Vyber si platební metodu:"
        ),
        "subscription_payment_change": "🔁 Chceš změnit plán? Použij tlačítka níže před platbou.",
        "subscription_invalid_plan": "Vyber jeden z dostupných plánů.",
        "subscription_invalid_duration": "Vyber prosím jednu z nabízených délek.",
        "subscription_payment_created": "Platba vytvořena (test)",
        "plan_devices_2_button": "💫 Zařízení: 2 - 99₽/měs.",
        "plan_devices_5_button": "✨ Zařízení: 5 - 169₽/měs.",
        "plan_devices_2_title": "2 zařízení",
        "plan_devices_5_title": "5 zařízení",
        "plan_devices_2_duration_1m": "1 měsíc - 99₽",
        "plan_devices_2_duration_3m": "🔹3 měsíce - 249₽",
        "plan_devices_2_duration_6m": "🔸6 měsíců - 399₽",
        "plan_devices_5_duration_1m": "1 měsíc - 169₽",
        "plan_devices_5_duration_3m": "🔹3 měsíce - 449₽",
        "plan_devices_5_duration_6m": "🔸6 měsíců - 749₽",
        "faq_title": "❓ Otázky",
        "faq_body": (
            "❓ Jak, co a proč?\n"
            "Nejčastější dotazy jsme dali do jednoho článku.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Tvé ID podpory: {tg_id}\n\n"
            "🗺 Potřebuješ pomoc? Napiš @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Pozvi přátele — získej bonusové dny.\n\n"
            "Každý, kdo se připojí přes tvůj odkaz, přidá +7 dní k předplatnému.\n\n"
            "Sdílej odkaz a surfuj déle zdarma."
        ),
        "referral_reward_notification": "🎉 Tvůj přítel se přidal!\nPřipsali jsme ti +7 dní k předplatnému ✨",
        "plan_title_trial": "Zkušební období",
        "plan_title_device2": "2 zařízení",
        "plan_title_device5": "5 zařízení",
    },
    "nl": {
        "start_pitch": "🚀 Snel en eenvoudig toegang rechtstreeks in Telegram.\nBlijf privé en stabiel, waar je ook bent.",
        "start_trial_granted": "🎁 Jouw bonus: 7 dagen gratis!\nGeniet van snelle en veilige toegang zonder beperkingen.",
        "status_header": (
            "👋 Je apparaten en abonnementsstatus\n\n"
            "Hier zie je welke apparaten zijn verbonden en welk plan je gebruikt."
        ),
        "status_plan_line": "📦 Je plan: {plan_title}",
        "status_devices_counter": "(Apparaten: {connected} / {limit})",
        "status_connections_header": "📟 Verbindingen:",
        "status_connections_empty": "Nog geen verbonden apparaten",
        "status_active_line": "🕒 Abonnement actief: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 dagen voor elke uitgenodigde vriend",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 seconden",
        "time_day_forms": "dag|dagen|dagen",
        "time_hour_forms": "uur|uur|uur",
        "time_minute_forms": "minuut|minuten|minuten",
        "time_second_forms": "seconde|seconden|seconden",
        "btn_intro_continue": "🚀 Laten we gaan!",
        "btn_devices": "📱 Apparaten",
        "btn_subscription": "💎 Abonnement",
        "btn_invite_friend": "🤝 Vriend uitnodigen",
        "btn_questions": "❓ Vragen",
        "btn_main_menu": "🏠 Hoofdmenu",
        "btn_back": "⬅️ Terug",
        "btn_phone": "📱 Telefoon",
        "btn_computer": "💻 Computer",
        "btn_my_devices": "🔌 Mijn apparaten",
        "btn_android": "🔴 Handleiding voor Android",
        "btn_ios": "🟢 Handleiding voor iPhone",
        "btn_windows_instructions": "🔴 Handleiding voor Windows",
        "btn_macos_instructions": "🟢 Handleiding voor macOS",
        "btn_share_link": "Link delen",
        "btn_pay_card": "💳 Bankkaart",
        "devices_choose": (
            "📲 Kies het apparaat dat je wilt verbinden.\n"
            "(Het kost maar een paar minuten — super eenvoudig!)"
        ),
        "devices_generation_in_progress": "⏳ De configuratie wordt al gegenereerd. Wacht op het bestand of de QR-code.",
        "devices_limit_reached": "⚠️ Limiet van apparaten voor dit plan bereikt",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Verbinden is bijna klaar!\n\n"
            "Kies de manier die je het beste past:\n"
            "1. Download het profielbestand en importeer het in AmneziaWG / WireGuard\n"
            "2. Scan de QR-code direct in de app\n\n"
            "📚 Kies de juiste handleiding en maak in een paar stappen verbinding.\n\n"
            "⚠️ Elk profiel kan maar op één apparaat worden gebruikt!"
        ),
        "devices_pick_guide": "📖 Hieronder vind je handleidingen voor verschillende systemen — kies die van jou en volg de stappen.",
        "devices_none": "Je hebt nog geen verbonden apparaten.",
        "devices_list_intro": "👇 Je verbonden apparaten:",
        "devices_select_prompt": "Selecteer een apparaat uit de lijst.",
        "device_default_name": "Apparaat {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Handleiding voor Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Handleiding voor iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Handleiding voor Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Handleiding voor macOS</a>",
        "subscription_intro": (
            "💎 Abonnement\n"
            "✨ Wat krijg je met het abonnement:\n"
            "• Snelle en veilige toegang tot je services\n"
            "• Geen advertenties of afleiding\n"
            "• Beste prijs — slechts 99₽ per maand! 🔥\n\n"
            "👉 Kies een plan voor 2 of 5 apparaten tegelijk."
        ),
        "subscription_duration_prompt": "⏱️ Kies de duur van het abonnement:\n{options}",
        "subscription_duration_hint": "💡 Een langere periode betekent een lagere prijs per maand.",
        "subscription_payment_thanks": (
            "🫶 Bedankt voor je vertrouwen!\n\n"
            "Je bent nog één stap verwijderd van een veilig, stabiel en snel internet.\n"
            "We hebben het proces zo handig mogelijk gemaakt.\n\n"
            "👇 Kies een betaalmethode:"
        ),
        "subscription_payment_change": "🔁 Wil je het plan wijzigen? Gebruik de knoppen hieronder vóór het betalen.",
        "subscription_invalid_plan": "Kies een van de beschikbare plannen.",
        "subscription_invalid_duration": "Kies alsjeblieft een van de voorgestelde looptijden.",
        "subscription_payment_created": "Betaling aangemaakt (test)",
        "plan_devices_2_button": "💫 Apparaten: 2 - 99₽/mnd",
        "plan_devices_5_button": "✨ Apparaten: 5 - 169₽/mnd",
        "plan_devices_2_title": "2 apparaten",
        "plan_devices_5_title": "5 apparaten",
        "plan_devices_2_duration_1m": "1 maand - 99₽",
        "plan_devices_2_duration_3m": "🔹3 maanden - 249₽",
        "plan_devices_2_duration_6m": "🔸6 maanden - 399₽",
        "plan_devices_5_duration_1m": "1 maand - 169₽",
        "plan_devices_5_duration_3m": "🔹3 maanden - 449₽",
        "plan_devices_5_duration_6m": "🔸6 maanden - 749₽",
        "faq_title": "❓ Vragen",
        "faq_body": (
            "❓ Hoe, wat en waarom?\n"
            "We verzamelden de meest gestelde vragen in één artikel.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Je support-ID: {tg_id}\n\n"
            "🗺 Hulp nodig? Schrijf naar @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Nodig vrienden uit — krijg extra dagen.\n\n"
            "Iedere vriend die via jouw link verbindt, geeft +7 dagen aan je abonnement.\n\n"
            "Deel de link en surf langer gratis."
        ),
        "referral_reward_notification": "🎉 Je vriend heeft zich aangesloten!\nJe hebt +7 dagen aan je abonnement gekregen ✨",
        "plan_title_trial": "Proefperiode",
        "plan_title_device2": "2 apparaten",
        "plan_title_device5": "5 apparaten",
    },
    "fi": {
        "start_pitch": "🚀 Nopea ja helppo pääsy suoraan Telegramissa.\nPidä yksityisyys ja vakaus missä tahansa oletkin.",
        "start_trial_granted": "🎁 Bonuksesi: 7 päivää ilmaiseksi!\nNauti nopeasta ja turvallisesta yhteydestä ilman rajoituksia.",
        "status_header": (
            "👋 Laitteesi ja tilauksesi tila\n\n"
            "Täältä näet, mitkä laitteet ovat yhdistettynä ja mikä paketti sinulla on."
        ),
        "status_plan_line": "📦 Pakettisi: {plan_title}",
        "status_devices_counter": "(Laitteet: {connected} / {limit})",
        "status_connections_header": "📟 Yhteydet:",
        "status_connections_empty": "Ei vielä yhdistettyjä laitteita",
        "status_active_line": "🕒 Tilauksesi on aktiivinen: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 päivää jokaisesta kutsutusta ystävästä",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 sekuntia",
        "time_day_forms": "päivä|päivää|päivää",
        "time_hour_forms": "tunti|tuntia|tuntia",
        "time_minute_forms": "minuutti|minuuttia|minuuttia",
        "time_second_forms": "sekunti|sekuntia|sekuntia",
        "btn_intro_continue": "🚀 Aloitetaan!",
        "btn_devices": "📱 Laitteet",
        "btn_subscription": "💎 Tilauksen tiedot",
        "btn_invite_friend": "🤝 Kutsu ystävä",
        "btn_questions": "❓ Kysymykset",
        "btn_main_menu": "🏠 Päävalikko",
        "btn_back": "⬅️ Takaisin",
        "btn_phone": "📱 Puhelin",
        "btn_computer": "💻 Tietokone",
        "btn_my_devices": "🔌 Omat laitteet",
        "btn_android": "🔴 Ohje Androidille",
        "btn_ios": "🟢 Ohje iPhonelle",
        "btn_windows_instructions": "🔴 Ohje Windowsille",
        "btn_macos_instructions": "🟢 Ohje macOS:lle",
        "btn_share_link": "Jaa linkki",
        "btn_pay_card": "💳 Pankkikortti",
        "devices_choose": (
            "📲 Valitse laite, jonka haluat yhdistää.\n"
            "(Se vie vain pari minuuttia — todella helppoa!)"
        ),
        "devices_generation_in_progress": "⏳ Määritystä luodaan jo. Odota tiedostoa tai QR-koodia.",
        "devices_limit_reached": "⚠️ Tämän paketin laiteraja on saavutettu",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Yhteys on melkein valmis!\n\n"
            "Valitse sinulle sopiva tapa:\n"
            "1. Lataa profiilitiedosto ja tuo se AmneziaWG / WireGuard -sovellukseen\n"
            "2. Skannaa QR-koodi suoraan sovelluksessa\n\n"
            "📚 Valitse sopiva ohje ja yhdistä muutamassa vaiheessa.\n\n"
            "⚠️ Jokainen profiili on tarkoitettu vain yhdelle laitteelle!"
        ),
        "devices_pick_guide": "📖 Alta löydät ohjeet eri järjestelmille — valitse omasi ja seuraa vaiheita.",
        "devices_none": "Sinulla ei vielä ole yhdistettyjä laitteita.",
        "devices_list_intro": "👇 Yhdistetyt laitteesi:",
        "devices_select_prompt": "Valitse laite listalta.",
        "device_default_name": "Laite {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Ohje Androidille</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Ohje iPhonelle</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Ohje Windowsille</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Ohje macOS:lle</a>",
        "subscription_intro": (
            "💎 Tilauksen tiedot\n"
            "✨ Mitä tilaus tarjoaa:\n"
            "• Nopea ja turvallinen pääsy palveluihisi\n"
            "• Ei mainoksia tai häiriötekijöitä\n"
            "• Paras hinta — vain 99₽ kuukaudessa! 🔥\n\n"
            "👉 Valitse paketti kahdelle tai viidelle laitteelle kerralla."
        ),
        "subscription_duration_prompt": "⏱️ Valitse tilauksen kesto:\n{options}",
        "subscription_duration_hint": "💡 Pidemmät jaksot laskevat kuukausihintaa.",
        "subscription_payment_thanks": (
            "🫶 Kiitos luottamuksesta!\n\n"
            "Olet askeleen päässä turvallisesta, vakaasta ja nopeasta internetistä.\n"
            "Teimme prosessista mahdollisimman vaivattoman.\n\n"
            "👇 Valitse maksutapa:"
        ),
        "subscription_payment_change": "🔁 Haluatko vaihtaa pakettia? Käytä alla olevia painikkeita ennen maksua.",
        "subscription_invalid_plan": "Valitse jokin saatavilla olevista paketeista.",
        "subscription_invalid_duration": "Valitse jokin ehdotetuista kestovaihtoehdoista.",
        "subscription_payment_created": "Maksu luotu (testi)",
        "plan_devices_2_button": "💫 Laitteet: 2 - 99₽/kk",
        "plan_devices_5_button": "✨ Laitteet: 5 - 169₽/kk",
        "plan_devices_2_title": "2 laitetta",
        "plan_devices_5_title": "5 laitetta",
        "plan_devices_2_duration_1m": "1 kuukausi - 99₽",
        "plan_devices_2_duration_3m": "🔹3 kuukautta - 249₽",
        "plan_devices_2_duration_6m": "🔸6 kuukautta - 399₽",
        "plan_devices_5_duration_1m": "1 kuukausi - 169₽",
        "plan_devices_5_duration_3m": "🔹3 kuukautta - 449₽",
        "plan_devices_5_duration_6m": "🔸6 kuukautta - 749₽",
        "faq_title": "❓ Kysymykset",
        "faq_body": (
            "❓ Miten, mitä ja miksi?\n"
            "Olemme koonneet suosituimmat kysymykset yhteen artikkeliin.\n"
            "📖 UKK: {faq_url}\n\n"
            "Tukitunnuksesi: {tg_id}\n\n"
            "🗺 Tarvitsetko apua? Kirjoita @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Kutsu ystäviä — ansaitse lisäpäiviä.\n\n"
            "Jokainen, joka liittyy linkkisi kautta, lisää +7 päivää tilaukseesi.\n\n"
            "Jaa linkki ja surffaa pidempään ilmaiseksi."
        ),
        "referral_reward_notification": "🎉 Ystäväsi liittyi!\nSait +7 päivää tilaukseesi ✨",
        "plan_title_trial": "Kokeilujakso",
        "plan_title_device2": "2 laitetta",
        "plan_title_device5": "5 laitetta",
    },
    "fr": {
        "start_pitch": "🚀 Accès rapide et simple directement dans Telegram.\nReste privé et stable où que tu sois.",
        "start_trial_granted": "🎁 Ton bonus : 7 jours offerts !\nProfite d’un accès rapide et sécurisé sans limites.",
        "status_header": (
            "👋 Tes appareils et l’état de ton abonnement\n\n"
            "Ici, tu vois quels appareils sont connectés et quel plan est actif."
        ),
        "status_plan_line": "📦 Ton plan : {plan_title}",
        "status_devices_counter": "(Appareils : {connected} / {limit})",
        "status_connections_header": "📟 Connexions :",
        "status_connections_empty": "Aucune connexion pour le moment",
        "status_active_line": "🕒 Abonnement actif : {duration}",
        "status_bonus_line": "🎁 Bonus : +7 jours pour chaque ami invité",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 seconde",
        "time_day_forms": "jour|jours|jours",
        "time_hour_forms": "heure|heures|heures",
        "time_minute_forms": "minute|minutes|minutes",
        "time_second_forms": "seconde|secondes|secondes",
        "btn_intro_continue": "🚀 C’est parti !",
        "btn_devices": "📱 Appareils",
        "btn_subscription": "💎 Abonnement",
        "btn_invite_friend": "🤝 Inviter un ami",
        "btn_questions": "❓ Questions",
        "btn_main_menu": "🏠 Menu principal",
        "btn_back": "⬅️ Retour",
        "btn_phone": "📱 Téléphone",
        "btn_computer": "💻 Ordinateur",
        "btn_my_devices": "🔌 Mes appareils",
        "btn_android": "🔴 Guide Android",
        "btn_ios": "🟢 Guide iPhone",
        "btn_windows_instructions": "🔴 Guide Windows",
        "btn_macos_instructions": "🟢 Guide macOS",
        "btn_share_link": "Partager le lien",
        "btn_pay_card": "💳 Carte bancaire",
        "devices_choose": (
            "📲 Choisis l’appareil que tu veux connecter.\n"
            "(Cela prend à peine quelques minutes — super simple !)"
        ),
        "devices_generation_in_progress": "⏳ La configuration est en cours de génération. Attends le fichier ou le QR code.",
        "devices_limit_reached": "⚠️ Limite d’appareils atteinte pour ce plan",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 La connexion est presque prête !\n\n"
            "Choisis la méthode qui te convient :\n"
            "1. Télécharge le fichier de profil et importe-le dans AmneziaWG / WireGuard\n"
            "2. Scanne le QR code directement dans l’appli\n\n"
            "📚 Choisis le bon guide et connecte-toi en quelques étapes.\n\n"
            "⚠️ Chaque profil ne peut être utilisé que sur un seul appareil !"
        ),
        "devices_pick_guide": "📖 Tu trouveras ci-dessous des guides pour différents systèmes — choisis le tien et suis les étapes.",
        "devices_none": "Tu n’as pas encore d’appareil connecté.",
        "devices_list_intro": "👇 Tes appareils connectés :",
        "devices_select_prompt": "Sélectionne un appareil dans la liste.",
        "device_default_name": "Appareil {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide macOS</a>",
        "subscription_intro": (
            "💎 Abonnement\n"
            "✨ Ce que tu obtiens :\n"
            "• Accès rapide et sécurisé à tes services\n"
            "• Pas de pubs ni de distractions\n"
            "• Meilleur prix — seulement 99₽ par mois ! 🔥\n\n"
            "👉 Choisis un plan pour 2 ou 5 appareils en même temps."
        ),
        "subscription_duration_prompt": "⏱️ Choisis la durée de l’abonnement :\n{options}",
        "subscription_duration_hint": "💡 Plus la période est longue, plus le prix mensuel diminue.",
        "subscription_payment_thanks": (
            "🫶 Merci pour ta confiance !\n\n"
            "Tu es à un pas d’un internet sécurisé, stable et rapide.\n"
            "Nous avons rendu le processus le plus confortable possible.\n\n"
            "👇 Choisis un mode de paiement :"
        ),
        "subscription_payment_change": "🔁 Besoin de changer de plan ? Utilise les boutons ci-dessous avant de payer.",
        "subscription_invalid_plan": "Choisis l’un des plans disponibles.",
        "subscription_invalid_duration": "Choisis l’une des durées proposées.",
        "subscription_payment_created": "Paiement créé (test)",
        "plan_devices_2_button": "💫 Appareils : 2 - 99₽/mois",
        "plan_devices_5_button": "✨ Appareils : 5 - 169₽/mois",
        "plan_devices_2_title": "2 appareils",
        "plan_devices_5_title": "5 appareils",
        "plan_devices_2_duration_1m": "1 mois - 99₽",
        "plan_devices_2_duration_3m": "🔹3 mois - 249₽",
        "plan_devices_2_duration_6m": "🔸6 mois - 399₽",
        "plan_devices_5_duration_1m": "1 mois - 169₽",
        "plan_devices_5_duration_3m": "🔹3 mois - 449₽",
        "plan_devices_5_duration_6m": "🔸6 mois - 749₽",
        "faq_title": "❓ Questions",
        "faq_body": (
            "❓ Comment, quoi et pourquoi ?\n"
            "Nous avons regroupé les questions les plus fréquentes dans un article.\n"
            "📖 FAQ : {faq_url}\n\n"
            "Ton ID support : {tg_id}\n\n"
            "🗺 Besoin d’aide ? Écris à @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Invite tes amis — gagne des jours bonus.\n\n"
            "Chaque ami qui se connecte via ton lien ajoute +7 jours à ton abonnement.\n\n"
            "Partage le lien et profite plus longtemps gratuitement."
        ),
        "referral_reward_notification": "🎉 Ton ami nous a rejoints !\nTu as reçu +7 jours d’abonnement ✨",
        "plan_title_trial": "Période d’essai",
        "plan_title_device2": "2 appareils",
        "plan_title_device5": "5 appareils",
    },
    "de": {
        "start_pitch": "🚀 Schneller und einfacher Zugriff direkt in Telegram.\nBleib privat, stabil und schnell – überall.",
        "start_trial_granted": "🎁 Dein Bonus: 7 Tage gratis!\nGenieße schnellen und sicheren Zugang ohne Limits.",
        "status_header": (
            "👋 Deine Geräte und dein Abo-Status\n\n"
            "Hier siehst du, welche Geräte verbunden sind und welchen Plan du hast."
        ),
        "status_plan_line": "📦 Dein Plan: {plan_title}",
        "status_devices_counter": "(Geräte: {connected} / {limit})",
        "status_connections_header": "📟 Verbindungen:",
        "status_connections_empty": "Noch keine Verbindungen",
        "status_active_line": "🕒 Abo aktiv: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 Tage für jeden eingeladenen Freund",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 Sekunden",
        "time_day_forms": "Tag|Tage|Tage",
        "time_hour_forms": "Stunde|Stunden|Stunden",
        "time_minute_forms": "Minute|Minuten|Minuten",
        "time_second_forms": "Sekunde|Sekunden|Sekunden",
        "btn_intro_continue": "🚀 Los geht’s!",
        "btn_devices": "📱 Geräte",
        "btn_subscription": "💎 Abonnement",
        "btn_invite_friend": "🤝 Freund einladen",
        "btn_questions": "❓ Fragen",
        "btn_main_menu": "🏠 Hauptmenü",
        "btn_back": "⬅️ Zurück",
        "btn_phone": "📱 Telefon",
        "btn_computer": "💻 Computer",
        "btn_my_devices": "🔌 Meine Geräte",
        "btn_android": "🔴 Anleitung für Android",
        "btn_ios": "🟢 Anleitung für iPhone",
        "btn_windows_instructions": "🔴 Anleitung für Windows",
        "btn_macos_instructions": "🟢 Anleitung für macOS",
        "btn_share_link": "Link teilen",
        "btn_pay_card": "💳 Bankkarte",
        "devices_choose": (
            "📲 Wähle das Gerät, das du verbinden möchtest.\n"
            "(Das dauert nur ein paar Minuten – ganz einfach!)"
        ),
        "devices_generation_in_progress": "⏳ Die Konfiguration wird bereits erstellt. Warte auf die Datei oder den QR-Code.",
        "devices_limit_reached": "⚠️ Gerätegrenze für diesen Tarif erreicht",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Die Einrichtung ist fast fertig!\n\n"
            "Wähle, wie du verbinden möchtest:\n"
            "1. Lade die Profildatei herunter und importiere sie in AmneziaWG / WireGuard\n"
            "2. Scanne den QR-Code direkt in der App\n\n"
            "📚 Wähle die passende Anleitung und verbinde dich in wenigen Schritten.\n\n"
            "⚠️ Jedes Profil darf nur auf einem Gerät genutzt werden!"
        ),
        "devices_pick_guide": "📖 Unten findest du Anleitungen für verschiedene Systeme – wähle deine und folge den Schritten.",
        "devices_none": "Du hast noch keine verbundenen Geräte.",
        "devices_list_intro": "👇 Deine verbundenen Geräte:",
        "devices_select_prompt": "Bitte wähle ein Gerät aus der Liste.",
        "device_default_name": "Gerät {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Anleitung für Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Anleitung für iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Anleitung für Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Anleitung für macOS</a>",
        "subscription_intro": (
            "💎 Abonnement\n"
            "✨ Das bietet dein Abo:\n"
            "• Schneller und sicherer Zugang zu deinen Diensten\n"
            "• Keine Werbung und keine Ablenkung\n"
            "• Bester Preis – nur 99₽ im Monat! 🔥\n\n"
            "👉 Wähle einen Plan für 2 oder 5 Geräte zugleich."
        ),
        "subscription_duration_prompt": "⏱️ Wähle die Laufzeit des Abos:\n{options}",
        "subscription_duration_hint": "💡 Längere Laufzeiten senken den Monats­preis.",
        "subscription_payment_thanks": (
            "🫶 Danke für dein Vertrauen!\n\n"
            "Du bist nur einen Schritt von sicherem, stabilem und schnellem Internet entfernt.\n"
            "Wir haben den Ablauf so bequem wie möglich gemacht.\n\n"
            "👇 Wähle eine Zahlungsmethode:"
        ),
        "subscription_payment_change": "🔁 Du möchtest den Plan ändern? Nutze die Buttons unten vor der Zahlung.",
        "subscription_invalid_plan": "Bitte wähle einen der verfügbaren Pläne.",
        "subscription_invalid_duration": "Bitte wähle eine der vorgeschlagenen Laufzeiten.",
        "subscription_payment_created": "Zahlung erstellt (Test)",
        "plan_devices_2_button": "💫 Geräte: 2 - 99₽/Monat",
        "plan_devices_5_button": "✨ Geräte: 5 - 169₽/Monat",
        "plan_devices_2_title": "2 Geräte",
        "plan_devices_5_title": "5 Geräte",
        "plan_devices_2_duration_1m": "1 Monat - 99₽",
        "plan_devices_2_duration_3m": "🔹3 Monate - 249₽",
        "plan_devices_2_duration_6m": "🔸6 Monate - 399₽",
        "plan_devices_5_duration_1m": "1 Monat - 169₽",
        "plan_devices_5_duration_3m": "🔹3 Monate - 449₽",
        "plan_devices_5_duration_6m": "🔸6 Monate - 749₽",
        "faq_title": "❓ Fragen",
        "faq_body": (
            "❓ Wie, was und warum?\n"
            "Die häufigsten Fragen haben wir in einem Artikel gesammelt.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Deine Support-ID: {tg_id}\n\n"
            "🗺 Hilfe nötig? Schreib an @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Lade Freunde ein – erhalte Bonus-Tage.\n\n"
            "Jeder Freund, der über deinen Link beitritt, bringt dir +7 Tage zu deinem Abo.\n\n"
            "Teile den Link und surfe länger gratis."
        ),
        "referral_reward_notification": "🎉 Dein Freund ist dabei!\nWir haben dir +7 Tage gutgeschrieben ✨",
        "plan_title_trial": "Testzeitraum",
        "plan_title_device2": "2 Geräte",
        "plan_title_device5": "5 Geräte",
    },
    "he": {
        "start_pitch": "🚀 גישה מהירה וקלה ישירות בטלגרם.\nשמור על פרטיות ויציבות בכל מקום.",
        "start_trial_granted": "🎁 הבונוס שלך: 7 ימים בחינם!\nתיהנה מגישה מהירה ומאובטחת בלי הגבלות.",
        "status_header": (
            "👋 המכשירים והמנוי שלך\n\n"
            "כאן תראה אילו מכשירים מחוברים ומה מצב החבילה שלך."
        ),
        "status_plan_line": "📦 התוכנית שלך: {plan_title}",
        "status_devices_counter": "(מכשירים: {connected} / {limit})",
        "status_connections_header": "📟 חיבורים:",
        "status_connections_empty": "עדיין אין חיבורים",
        "status_active_line": "🕒 המנוי פעיל למשך: {duration}",
        "status_bonus_line": "🎁 בונוס: ‎+7 ימים על כל חבר שמצטרף",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 שניות",
        "time_day_forms": "יום|יומיים|ימים",
        "time_hour_forms": "שעה|שעתיים|שעות",
        "time_minute_forms": "דקה|דקות|דקות",
        "time_second_forms": "שנייה|שניות|שניות",
        "btn_intro_continue": "🚀 קדימה!",
        "btn_devices": "📱 מכשירים",
        "btn_subscription": "💎 מנוי",
        "btn_invite_friend": "🤝 להזמין חבר",
        "btn_questions": "❓ שאלות",
        "btn_main_menu": "🏠 תפריט ראשי",
        "btn_back": "⬅️ חזרה",
        "btn_phone": "📱 טלפון",
        "btn_computer": "💻 מחשב",
        "btn_my_devices": "🔌 המכשירים שלי",
        "btn_android": "🔴 מדריך ל-Android",
        "btn_ios": "🟢 מדריך ל-iPhone",
        "btn_windows_instructions": "🔴 מדריך ל-Windows",
        "btn_macos_instructions": "🟢 מדריך ל-macOS",
        "btn_share_link": "לשתף קישור",
        "btn_pay_card": "💳 כרטיס בנקאי",
        "devices_choose": (
            "📲 בחר את המכשיר שתרצה לחבר.\n"
            "(זה לוקח רק כמה דקות — ממש פשוט!)"
        ),
        "devices_generation_in_progress": "⏳ הקובץ כבר נוצר. חכה לקובץ או לקוד ה-QR.",
        "devices_limit_reached": "⚠️ הגעת למגבלת המכשירים בחבילה הזו",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 ההגדרה כמעט מוכנה!\n\n"
            "בחר את הדרך הנוחה לך:\n"
            "1. הורד את קובץ הפרופיל וייבא אותו ל-AmneziaWG / WireGuard\n"
            "2. סרוק את קוד ה-QR ישירות באפליקציה\n\n"
            "📚 בחר במדריך המתאים והתחבר בכמה צעדים.\n\n"
            "⚠️ כל פרופיל מיועד למכשיר אחד בלבד!"
        ),
        "devices_pick_guide": "📖 כאן תמצא מדריכים למערכות שונות — בחר את שלך ופעל לפי ההוראות.",
        "devices_none": "עדיין אין לך מכשירים מחוברים.",
        "devices_list_intro": "👇 המכשירים המחוברים שלך:",
        "devices_select_prompt": "בחר מכשיר מהרשימה.",
        "device_default_name": "מכשיר {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 מדריך ל-Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 מדריך ל-iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 מדריך ל-Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 מדריך ל-macOS</a>",
        "subscription_intro": (
            "💎 מנוי\n"
            "✨ מה מקבלים במנוי:\n"
            "• גישה מהירה ובטוחה לשירותים שלך\n"
            "• בלי פרסומות והסחות דעת\n"
            "• מחיר מעולה — רק 99₽ בחודש! 🔥\n\n"
            "👉 בחר חבילה ל-2 או 5 מכשירים ביחד."
        ),
        "subscription_duration_prompt": "⏱️ בחר את משך המנוי:\n{options}",
        "subscription_duration_hint": "💡 ככל שהתקופה ארוכה יותר, המחיר החודשי נמוך יותר.",
        "subscription_payment_thanks": (
            "🫶 תודה על האמון!\n\n"
            "עוד צעד אחד ואתה באינטרנט בטוח, יציב ומהיר.\n"
            "הפכנו את התהליך לנוח ככל האפשר.\n\n"
            "👇 בחר אמצעי תשלום:"
        ),
        "subscription_payment_change": "🔁 רוצה לשנות חבילה? השתמש בכפתורים למטה לפני התשלום.",
        "subscription_invalid_plan": "בחר אחת מהחבילות הזמינות.",
        "subscription_invalid_duration": "בחר אחת מתקופות הזמן המוצעות.",
        "subscription_payment_created": "התשלום נוצר (בדיקה)",
        "plan_devices_2_button": "💫 מכשירים: 2 - 99₽/חודש",
        "plan_devices_5_button": "✨ מכשירים: 5 - 169₽/חודש",
        "plan_devices_2_title": "2 מכשירים",
        "plan_devices_5_title": "5 מכשירים",
        "plan_devices_2_duration_1m": "חודש 1 - 99₽",
        "plan_devices_2_duration_3m": "🔹3 חודשים - 249₽",
        "plan_devices_2_duration_6m": "🔸6 חודשים - 399₽",
        "plan_devices_5_duration_1m": "חודש 1 - 169₽",
        "plan_devices_5_duration_3m": "🔹3 חודשים - 449₽",
        "plan_devices_5_duration_6m": "🔸6 חודשים - 749₽",
        "faq_title": "❓ שאלות",
        "faq_body": (
            "❓ איך, מה ולמה?\n"
            "ריכזנו את השאלות הפופולריות ביותר במאמר אחד.\n"
            "📖 שאלות נפוצות: {faq_url}\n\n"
            "מזהה התמיכה שלך: {tg_id}\n\n"
            "🗺 צריך עזרה? כתוב ל-@{support_handle}"
        ),
        "referral_intro": (
            "🤝 הזמן חברים — וקבל ימי בונוס.\n\n"
            "כל חבר שמצטרף דרך הקישור שלך מוסיף ‎+7 ימים למנוי.\n\n"
            "שתף את הקישור וגלוש יותר בחינם."
        ),
        "referral_reward_notification": "🎉 חבר שלך הצטרף!\nקיבלת ‎+7 ימים למנוי ✨",
        "plan_title_trial": "תקופת ניסיון",
        "plan_title_device2": "2 מכשירים",
        "plan_title_device5": "5 מכשירים",
    },
    "hu": {
        "start_pitch": "🚀 Gyors és egyszerű hozzáférés közvetlenül a Telegramban.\nMaradj privát és stabil bárhol is vagy.",
        "start_trial_granted": "🎁 A bónuszod: 7 nap ingyen!\nÉlvezd a gyors és biztonságos elérést korlátok nélkül.",
        "status_header": (
            "👋 A készülékeid és az előfizetésed állapota\n\n"
            "Itt láthatod, mely eszközök vannak csatlakoztatva és milyen csomagod van."
        ),
        "status_plan_line": "📦 Csomagod: {plan_title}",
        "status_devices_counter": "(Eszközök: {connected} / {limit})",
        "status_connections_header": "📟 Kapcsolatok:",
        "status_connections_empty": "Még nincs csatlakoztatott eszköz",
        "status_active_line": "🕒 Előfizetés aktív: {duration}",
        "status_bonus_line": "🎁 Bónusz: +7 nap minden meghívott barát után",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 másodperc",
        "time_day_forms": "nap|nap|nap",
        "time_hour_forms": "óra|óra|óra",
        "time_minute_forms": "perc|perc|perc",
        "time_second_forms": "másodperc|másodperc|másodperc",
        "btn_intro_continue": "🚀 Indulhatunk!",
        "btn_devices": "📱 Eszközök",
        "btn_subscription": "💎 Előfizetés",
        "btn_invite_friend": "🤝 Barát meghívása",
        "btn_questions": "❓ Kérdések",
        "btn_main_menu": "🏠 Főmenü",
        "btn_back": "⬅️ Vissza",
        "btn_phone": "📱 Telefon",
        "btn_computer": "💻 Számítógép",
        "btn_my_devices": "🔌 Saját eszközeim",
        "btn_android": "🔴 Útmutató Androidhoz",
        "btn_ios": "🟢 Útmutató iPhone-hoz",
        "btn_windows_instructions": "🔴 Útmutató Windows-hoz",
        "btn_macos_instructions": "🟢 Útmutató macOS-hez",
        "btn_share_link": "Hivatkozás megosztása",
        "btn_pay_card": "💳 Bankkártya",
        "devices_choose": (
            "📲 Válaszd ki a csatlakoztatni kívánt eszközt.\n"
            "(Csak néhány perc — nagyon egyszerű!)"
        ),
        "devices_generation_in_progress": "⏳ A konfiguráció már készül. Várd meg a fájlt vagy a QR-kódot.",
        "devices_limit_reached": "⚠️ Elérted az eszközlimitet ebben a csomagban",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 A csatlakozás majdnem kész!\n\n"
            "Válaszd ki a számodra megfelelő módot:\n"
            "1. Töltsd le a profilfájlt, és importáld az AmneziaWG / WireGuard alkalmazásba\n"
            "2. Olvasd be a QR-kódot közvetlenül az appban\n\n"
            "📚 Válassz útmutatót, és csatlakozz néhány lépésben.\n\n"
            "⚠️ Minden profil csak egy eszközön használható!"
        ),
        "devices_pick_guide": "📖 Lent különböző rendszerekhez találsz útmutatókat — válaszd ki a sajátodat és kövesd a lépéseket.",
        "devices_none": "Még nincs csatlakoztatott eszközöd.",
        "devices_list_intro": "👇 Csatlakoztatott eszközeid:",
        "devices_select_prompt": "Válassz egy eszközt a listából.",
        "device_default_name": "Eszköz {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Útmutató Androidhoz</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Útmutató iPhone-hoz</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Útmutató Windows-hoz</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Útmutató macOS-hez</a>",
        "subscription_intro": (
            "💎 Előfizetés\n"
            "✨ Mit kapsz az előfizetéssel:\n"
            "• Gyors és biztonságos hozzáférés a szolgáltatásaidhoz\n"
            "• Nincsenek hirdetések és zavaró elemek\n"
            "• A legjobb ár — mindössze 99₽ havonta! 🔥\n\n"
            "👉 Válassz csomagot 2 vagy 5 eszközre egyszerre."
        ),
        "subscription_duration_prompt": "⏱️ Válaszd ki az előfizetés hosszát:\n{options}",
        "subscription_duration_hint": "💡 Hosszabb időszak esetén alacsonyabb a havi ár.",
        "subscription_payment_thanks": (
            "🫶 Köszönjük a bizalmat!\n\n"
            "Egy lépésre vagy a biztonságos, stabil és gyors internettől.\n"
            "A folyamatot a lehető legkényelmesebbé tettük.\n\n"
            "👇 Válassz fizetési módot:"
        ),
        "subscription_payment_change": "🔁 Módosítanál csomagot? Használd a gombokat fizetés előtt.",
        "subscription_invalid_plan": "Válassz a rendelkezésre álló csomagok közül.",
        "subscription_invalid_duration": "Kérjük, válassz az ajánlott időtartamok közül.",
        "subscription_payment_created": "Fizetés létrehozva (teszt)",
        "plan_devices_2_button": "💫 Eszközök: 2 - 99₽/hó",
        "plan_devices_5_button": "✨ Eszközök: 5 - 169₽/hó",
        "plan_devices_2_title": "2 eszköz",
        "plan_devices_5_title": "5 eszköz",
        "plan_devices_2_duration_1m": "1 hónap - 99₽",
        "plan_devices_2_duration_3m": "🔹3 hónap - 249₽",
        "plan_devices_2_duration_6m": "🔸6 hónap - 399₽",
        "plan_devices_5_duration_1m": "1 hónap - 169₽",
        "plan_devices_5_duration_3m": "🔹3 hónap - 449₽",
        "plan_devices_5_duration_6m": "🔸6 hónap - 749₽",
        "faq_title": "❓ Kérdések",
        "faq_body": (
            "❓ Hogyan, mit és miért?\n"
            "A leggyakoribb kérdéseket egy cikkben gyűjtöttük össze.\n"
            "📖 GYIK: {faq_url}\n\n"
            "Támogatási azonosítód: {tg_id}\n\n"
            "🗺 Segítségre van szükséged? Írj @{support_handle} címre"
        ),
        "referral_intro": (
            "🤝 Hívd meg a barátaidat — szerezz bónusz napokat.\n\n"
            "Minden barát, aki a hivatkozásoddal csatlakozik, +7 napot ad az előfizetésedhez.\n\n"
            "Oszd meg a linket, és böngéssz tovább ingyen."
        ),
        "referral_reward_notification": "🎉 A barátod csatlakozott!\n+7 napot kaptál az előfizetésedhez ✨",
        "plan_title_trial": "Próbaidőszak",
        "plan_title_device2": "2 eszköz",
        "plan_title_device5": "5 eszköz",
    },
    "id": {
        "start_pitch": "🚀 Akses cepat dan mudah langsung di Telegram.\nTetap pribadi dan stabil di mana pun kamu berada.",
        "start_trial_granted": "🎁 Bonusmu: 7 hari gratis!\nNikmati akses cepat dan aman tanpa batas.",
        "status_header": (
            "👋 Perangkatmu dan status langganan\n\n"
            "Di sini kamu bisa melihat perangkat yang terhubung dan paket yang aktif."
        ),
        "status_plan_line": "📦 Paketmu: {plan_title}",
        "status_devices_counter": "(Perangkat: {connected} / {limit})",
        "status_connections_header": "📟 Koneksi:",
        "status_connections_empty": "Belum ada perangkat yang terhubung",
        "status_active_line": "🕒 Langganan aktif: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 hari untuk setiap teman yang diundang",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 detik",
        "time_day_forms": "hari|hari|hari",
        "time_hour_forms": "jam|jam|jam",
        "time_minute_forms": "menit|menit|menit",
        "time_second_forms": "detik|detik|detik",
        "btn_intro_continue": "🚀 Mulai sekarang!",
        "btn_devices": "📱 Perangkat",
        "btn_subscription": "💎 Langganan",
        "btn_invite_friend": "🤝 Ajak teman",
        "btn_questions": "❓ Pertanyaan",
        "btn_main_menu": "🏠 Menu utama",
        "btn_back": "⬅️ Kembali",
        "btn_phone": "📱 Ponsel",
        "btn_computer": "💻 Komputer",
        "btn_my_devices": "🔌 Perangkatku",
        "btn_android": "🔴 Panduan Android",
        "btn_ios": "🟢 Panduan iPhone",
        "btn_windows_instructions": "🔴 Panduan Windows",
        "btn_macos_instructions": "🟢 Panduan macOS",
        "btn_share_link": "Bagikan tautan",
        "btn_pay_card": "💳 Kartu bank",
        "devices_choose": (
            "📲 Pilih perangkat yang ingin kamu hubungkan.\n"
            "(Hanya butuh beberapa menit — super mudah!)"
        ),
        "devices_generation_in_progress": "⏳ Konfigurasi sedang dibuat. Tunggu file atau kode QR.",
        "devices_limit_reached": "⚠️ Batas perangkat untuk paket ini tercapai",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Pengaturan hampir selesai!\n\n"
            "Pilih cara yang kamu mau:\n"
            "1. Unduh file profil dan impor ke AmneziaWG / WireGuard\n"
            "2. Pindai kode QR langsung di aplikasi\n\n"
            "📚 Pilih panduan yang sesuai dan hubungkan dalam beberapa langkah.\n\n"
            "⚠️ Setiap profil hanya bisa dipakai di satu perangkat!"
        ),
        "devices_pick_guide": "📖 Di bawah ini ada panduan untuk berbagai sistem — pilih punyamu dan ikuti langkahnya.",
        "devices_none": "Kamu belum punya perangkat yang terhubung.",
        "devices_list_intro": "👇 Perangkat yang terhubung:",
        "devices_select_prompt": "Silakan pilih perangkat dari daftar.",
        "device_default_name": "Perangkat {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Panduan Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Panduan iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Panduan Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Panduan macOS</a>",
        "subscription_intro": (
            "💎 Langganan\n"
            "✨ Keuntungan langganan:\n"
            "• Akses cepat dan aman ke layananmu\n"
            "• Tanpa iklan dan gangguan\n"
            "• Harga terbaik — hanya 99₽ per bulan! 🔥\n\n"
            "👉 Pilih paket untuk 2 atau 5 perangkat sekaligus."
        ),
        "subscription_duration_prompt": "⏱️ Pilih durasi langganan:\n{options}",
        "subscription_duration_hint": "💡 Periode yang lebih lama berarti harga bulanan lebih murah.",
        "subscription_payment_thanks": (
            "🫶 Terima kasih atas kepercayaanmu!\n\n"
            "Kamu selangkah lagi menuju internet yang aman, stabil, dan cepat.\n"
            "Kami membuat prosesnya senyaman mungkin.\n\n"
            "👇 Pilih metode pembayaran:"
        ),
        "subscription_payment_change": "🔁 Mau ganti paket? Gunakan tombol di bawah sebelum membayar.",
        "subscription_invalid_plan": "Pilih salah satu paket yang tersedia.",
        "subscription_invalid_duration": "Silakan pilih salah satu durasi yang ditawarkan.",
        "subscription_payment_created": "Pembayaran dibuat (uji)",
        "plan_devices_2_button": "💫 Perangkat: 2 - 99₽/bulan",
        "plan_devices_5_button": "✨ Perangkat: 5 - 169₽/bulan",
        "plan_devices_2_title": "2 perangkat",
        "plan_devices_5_title": "5 perangkat",
        "plan_devices_2_duration_1m": "1 bulan - 99₽",
        "plan_devices_2_duration_3m": "🔹3 bulan - 249₽",
        "plan_devices_2_duration_6m": "🔸6 bulan - 399₽",
        "plan_devices_5_duration_1m": "1 bulan - 169₽",
        "plan_devices_5_duration_3m": "🔹3 bulan - 449₽",
        "plan_devices_5_duration_6m": "🔸6 bulan - 749₽",
        "faq_title": "❓ Pertanyaan",
        "faq_body": (
            "❓ Bagaimana, apa, dan mengapa?\n"
            "Kami mengumpulkan pertanyaan paling populer dalam satu artikel.\n"
            "📖 FAQ: {faq_url}\n\n"
            "ID dukunganmu: {tg_id}\n\n"
            "🗺 Butuh bantuan? Hubungi @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Ajak teman — dapatkan hari bonus.\n\n"
            "Setiap teman yang bergabung lewat tautanmu menambah +7 hari langganan.\n\n"
            "Bagikan tautan dan nikmati internet lebih lama secara gratis."
        ),
        "referral_reward_notification": "🎉 Temanmu bergabung!\nKamu mendapat +7 hari langganan ✨",
        "plan_title_trial": "Masa percobaan",
        "plan_title_device2": "2 perangkat",
        "plan_title_device5": "5 perangkat",
    },
    "it": {
        "start_pitch": "🚀 Accesso rapido e semplice direttamente su Telegram.\nResta privato e stabile ovunque ti trovi.",
        "start_trial_granted": "🎁 Il tuo bonus: 7 giorni gratis!\nGoditi un accesso veloce e sicuro senza limiti.",
        "status_header": (
            "👋 I tuoi dispositivi e lo stato dell’abbonamento\n\n"
            "Qui puoi vedere quali dispositivi sono collegati e quale piano hai attivo."
        ),
        "status_plan_line": "📦 Il tuo piano: {plan_title}",
        "status_devices_counter": "(Dispositivi: {connected} / {limit})",
        "status_connections_header": "📟 Connessioni:",
        "status_connections_empty": "Ancora nessuna connessione",
        "status_active_line": "🕒 Abbonamento attivo: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 giorni per ogni amico invitato",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 secondi",
        "time_day_forms": "giorno|giorni|giorni",
        "time_hour_forms": "ora|ore|ore",
        "time_minute_forms": "minuto|minuti|minuti",
        "time_second_forms": "secondo|secondi|secondi",
        "btn_intro_continue": "🚀 Andiamo!",
        "btn_devices": "📱 Dispositivi",
        "btn_subscription": "💎 Abbonamento",
        "btn_invite_friend": "🤝 Invita un amico",
        "btn_questions": "❓ Domande",
        "btn_main_menu": "🏠 Menu principale",
        "btn_back": "⬅️ Indietro",
        "btn_phone": "📱 Telefono",
        "btn_computer": "💻 Computer",
        "btn_my_devices": "🔌 I miei dispositivi",
        "btn_android": "🔴 Guida Android",
        "btn_ios": "🟢 Guida iPhone",
        "btn_windows_instructions": "🔴 Guida Windows",
        "btn_macos_instructions": "🟢 Guida macOS",
        "btn_share_link": "Condividi il link",
        "btn_pay_card": "💳 Carta bancaria",
        "devices_choose": (
            "📲 Scegli il dispositivo che vuoi collegare.\n"
            "(Bastano pochi minuti — è davvero semplice!)"
        ),
        "devices_generation_in_progress": "⏳ La configurazione è in fase di generazione. Attendi il file o il QR code.",
        "devices_limit_reached": "⚠️ Limite di dispositivi raggiunto per questo piano",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 La configurazione è quasi pronta!\n\n"
            "Scegli il metodo che preferisci:\n"
            "1. Scarica il file del profilo e importalo in AmneziaWG / WireGuard\n"
            "2. Scansiona il QR code direttamente nell’app\n\n"
            "📚 Seleziona la guida giusta e collegati in pochi passaggi.\n\n"
            "⚠️ Ogni profilo può essere usato su un solo dispositivo!"
        ),
        "devices_pick_guide": "📖 Qui sotto trovi le guide per i vari sistemi — scegli la tua e segui i passaggi.",
        "devices_none": "Non hai ancora dispositivi collegati.",
        "devices_list_intro": "👇 I tuoi dispositivi collegati:",
        "devices_select_prompt": "Scegli un dispositivo dall’elenco.",
        "device_default_name": "Dispositivo {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guida Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guida iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guida Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guida macOS</a>",
        "subscription_intro": (
            "💎 Abbonamento\n"
            "✨ Cosa include l’abbonamento:\n"
            "• Accesso rapido e sicuro ai tuoi servizi\n"
            "• Nessuna pubblicità o distrazione\n"
            "• Il prezzo migliore — solo 99₽ al mese! 🔥\n\n"
            "👉 Scegli un piano per 2 o 5 dispositivi contemporaneamente."
        ),
        "subscription_duration_prompt": "⏱️ Scegli la durata dell’abbonamento:\n{options}",
        "subscription_duration_hint": "💡 Più lunga è la durata, minore è il costo mensile.",
        "subscription_payment_thanks": (
            "🫶 Grazie per la fiducia!\n\n"
            "Sei a un passo da un internet sicuro, stabile e veloce.\n"
            "Abbiamo reso il processo il più comodo possibile.\n\n"
            "👇 Scegli un metodo di pagamento:"
        ),
        "subscription_payment_change": "🔁 Vuoi cambiare piano? Usa i pulsanti qui sotto prima del pagamento.",
        "subscription_invalid_plan": "Scegli uno dei piani disponibili.",
        "subscription_invalid_duration": "Seleziona una delle durate proposte.",
        "subscription_payment_created": "Pagamento creato (test)",
        "plan_devices_2_button": "💫 Dispositivi: 2 - 99₽/mese",
        "plan_devices_5_button": "✨ Dispositivi: 5 - 169₽/mese",
        "plan_devices_2_title": "2 dispositivi",
        "plan_devices_5_title": "5 dispositivi",
        "plan_devices_2_duration_1m": "1 mese - 99₽",
        "plan_devices_2_duration_3m": "🔹3 mesi - 249₽",
        "plan_devices_2_duration_6m": "🔸6 mesi - 399₽",
        "plan_devices_5_duration_1m": "1 mese - 169₽",
        "plan_devices_5_duration_3m": "🔹3 mesi - 449₽",
        "plan_devices_5_duration_6m": "🔸6 mesi - 749₽",
        "faq_title": "❓ Domande",
        "faq_body": (
            "❓ Come, cosa e perché?\n"
            "Abbiamo raccolto le domande più frequenti in un unico articolo.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Il tuo ID di supporto: {tg_id}\n\n"
            "🗺 Hai bisogno di aiuto? Scrivi a @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Invita gli amici — ottieni giorni bonus.\n\n"
            "Ogni amico che si collega con il tuo link aggiunge +7 giorni all’abbonamento.\n\n"
            "Condividi il link e naviga più a lungo gratis."
        ),
        "referral_reward_notification": "🎉 Il tuo amico si è unito!\nHai ricevuto +7 giorni di abbonamento ✨",
        "plan_title_trial": "Periodo di prova",
        "plan_title_device2": "2 dispositivi",
        "plan_title_device5": "5 dispositivi",
    },
    "kk": {
        "start_pitch": "🚀 Telegram-да жылдам әрі оңай қолжетімділік.\nҚай жерде болсаң да, құпиялылығың мен тұрақтылығыңды сақта.",
        "start_trial_granted": "🎁 Бонусың: 7 күн тегін!\nШектеусіз жылдам әрі қауіпсіз қолжетімділікті байқап көр.",
        "status_header": (
            "👋 Құрылғыларың және жазылым күйі\n\n"
            "Мұнда қай құрылғылар қосылғанын және қандай тариф қолданатыныңды көре аласың."
        ),
        "status_plan_line": "📦 Сенің тарифің: {plan_title}",
        "status_devices_counter": "(Құрылғылар: {connected} / {limit})",
        "status_connections_header": "📟 Қосылулар:",
        "status_connections_empty": "Әзірге қосылған құрылғылар жоқ",
        "status_active_line": "🕒 Жазылым белсенді: {duration}",
        "status_bonus_line": "🎁 Бонус: әр шақырылған дос үшін +7 күн",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 секунд",
        "time_day_forms": "күн|күн|күн",
        "time_hour_forms": "сағат|сағат|сағат",
        "time_minute_forms": "минут|минут|минут",
        "time_second_forms": "секунд|секунд|секунд",
        "btn_intro_continue": "🚀 Бастайық!",
        "btn_devices": "📱 Құрылғылар",
        "btn_subscription": "💎 Жазылым",
        "btn_invite_friend": "🤝 Дос шақыру",
        "btn_questions": "❓ Сұрақтар",
        "btn_main_menu": "🏠 Негізгі мәзір",
        "btn_back": "⬅️ Артқа",
        "btn_phone": "📱 Телефон",
        "btn_computer": "💻 Компьютер",
        "btn_my_devices": "🔌 Менің құрылғыларым",
        "btn_android": "🔴 Android нұсқаулығы",
        "btn_ios": "🟢 iPhone нұсқаулығы",
        "btn_windows_instructions": "🔴 Windows нұсқаулығы",
        "btn_macos_instructions": "🟢 macOS нұсқаулығы",
        "btn_share_link": "Сілтемемен бөлісу",
        "btn_pay_card": "💳 Банктік карта",
        "devices_choose": (
            "📲 Қосқың келетін құрылғыны таңда.\n"
            "(Бәрі бірнеше минут ішінде — өте оңай!)"
        ),
        "devices_generation_in_progress": "⏳ Конфигурация жасалып жатыр. Файл немесе QR-кодты күт.",
        "devices_limit_reached": "⚠️ Бұл тариф үшін құрылғы лимиті орындалды",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Қосылу дерлік дайын!\n\n"
            "Өзіңе ыңғайлы тәсілді таңда:\n"
            "1. Профиль файлын жүктеп алып, AmneziaWG / WireGuard-қа импортта\n"
            "2. Қолданбада QR-кодты сканерле\n\n"
            "📚 Дұрыс нұсқаулықты таңдап, бірнеше қадаммен қосыл.\n\n"
            "⚠️ Әр профиль тек бір құрылғыда қолданылады!"
        ),
        "devices_pick_guide": "📖 Төменде әртүрлі жүйелерге арналған нұсқаулықтар бар — өзіңдікін таңдап, қадамдарды орында.",
        "devices_none": "Әзірге қосылған құрылғылар жоқ.",
        "devices_list_intro": "👇 Қосылған құрылғыларың:",
        "devices_select_prompt": "Тізімнен құрылғыны таңда.",
        "device_default_name": "Құрылғы {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Android нұсқаулығы</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 iPhone нұсқаулығы</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Windows нұсқаулығы</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 macOS нұсқаулығы</a>",
        "subscription_intro": (
            "💎 Жазылым\n"
            "✨ Жазылым не береді:\n"
            "• Қызметтеріңе жылдам әрі қауіпсіз қолжетімділік\n"
            "• Жарнама мен артық алаңдатулар жоқ\n"
            "• Ең тиімді баға — айына бар болғаны 99₽! 🔥\n\n"
            "👉 Бірден 2 немесе 5 құрылғыға арналған тарифті таңда."
        ),
        "subscription_duration_prompt": "⏱️ Жазылым мерзімін таңда:\n{options}",
        "subscription_duration_hint": "💡 Ұзақ мерзім — ай сайынғы баға төмен.",
        "subscription_payment_thanks": (
            "🫶 Сенімің үшін рақмет!\n\n"
            "Қауіпсіз, тұрақты және жылдам интернетке бір қадам қалды.\n"
            "Біз процесті барынша ыңғайлы еттік.\n\n"
            "👇 Төлем тәсілін таңда:"
        ),
        "subscription_payment_change": "🔁 Тарифті өзгерткің келе ме? Төлемге дейін төмендегі батырмаларды қолдан.",
        "subscription_invalid_plan": "Қолжетімді тарифтердің бірін таңда.",
        "subscription_invalid_duration": "Ұсынылған мерзімдердің бірін таңда.",
        "subscription_payment_created": "Төлем жасалды (сынақ)",
        "plan_devices_2_button": "💫 Құрылғылар: 2 - 99₽/ай",
        "plan_devices_5_button": "✨ Құрылғылар: 5 - 169₽/ай",
        "plan_devices_2_title": "2 құрылғы",
        "plan_devices_5_title": "5 құрылғы",
        "plan_devices_2_duration_1m": "1 ай - 99₽",
        "plan_devices_2_duration_3m": "🔹3 ай - 249₽",
        "plan_devices_2_duration_6m": "🔸6 ай - 399₽",
        "plan_devices_5_duration_1m": "1 ай - 169₽",
        "plan_devices_5_duration_3m": "🔹3 ай - 449₽",
        "plan_devices_5_duration_6m": "🔸6 ай - 749₽",
        "faq_title": "❓ Сұрақтар",
        "faq_body": (
            "❓ Қалай, не және не үшін?\n"
            "Ең танымал сұрақтарды бір мақаладан табасың.\n"
            "📖 Жиі қойылатын сұрақтар: {faq_url}\n\n"
            "Қолдау ID-ің: {tg_id}\n\n"
            "🗺 Көмек керек пе? @{support_handle} жаз."
        ),
        "referral_intro": (
            "🤝 Достарыңды шақыр — бонус күндер ал.\n\n"
            "Сілтемең арқылы қосылған әр досқа +7 күн қосылады.\n\n"
            "Сілтемені бөлісіп, интернетті ұзағырақ тегін қолдан."
        ),
        "referral_reward_notification": "🎉 Досың қосылды!\nЖазылымыңа +7 күн қосылды ✨",
        "plan_title_trial": "Сынақ мерзімі",
        "plan_title_device2": "2 құрылғы",
        "plan_title_device5": "5 құрылғы",
    },
    "ko": {
        "start_pitch": "🚀 텔레그램에서 빠르고 간편하게 이용하세요.\n어디서든 프라이버시와 안정성을 지켜드립니다.",
        "start_trial_granted": "🎁 보너스: 7일 무료!\n제한 없이 빠르고 안전한 접속을 경험해 보세요.",
        "status_header": (
            "👋 내 기기와 구독 상태\n\n"
            "연결된 기기와 사용 중인 요금을 여기에서 확인할 수 있어요."
        ),
        "status_plan_line": "📦 내 요금제: {plan_title}",
        "status_devices_counter": "(기기: {connected} / {limit})",
        "status_connections_header": "📟 연결 목록:",
        "status_connections_empty": "아직 연결된 기기가 없어요",
        "status_active_line": "🕒 구독 활성화 기간: {duration}",
        "status_bonus_line": "🎁 보너스: 친구를 초대할 때마다 +7일",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0초",
        "time_day_forms": "일|일|일",
        "time_hour_forms": "시간|시간|시간",
        "time_minute_forms": "분|분|분",
        "time_second_forms": "초|초|초",
        "btn_intro_continue": "🚀 시작하기",
        "btn_devices": "📱 기기",
        "btn_subscription": "💎 구독",
        "btn_invite_friend": "🤝 친구 초대",
        "btn_questions": "❓ 질문",
        "btn_main_menu": "🏠 메인 메뉴",
        "btn_back": "⬅️ 뒤로",
        "btn_phone": "📱 휴대폰",
        "btn_computer": "💻 컴퓨터",
        "btn_my_devices": "🔌 내 기기",
        "btn_android": "🔴 Android 가이드",
        "btn_ios": "🟢 iPhone 가이드",
        "btn_windows_instructions": "🔴 Windows 가이드",
        "btn_macos_instructions": "🟢 macOS 가이드",
        "btn_share_link": "링크 공유",
        "btn_pay_card": "💳 카드 결제",
        "devices_choose": (
            "📲 연결할 기기를 선택하세요.\n"
            "(몇 분이면 끝나는 아주 간단한 과정이에요!)"
        ),
        "devices_generation_in_progress": "⏳ 구성 파일을 생성 중입니다. 파일이나 QR 코드를 기다려 주세요.",
        "devices_limit_reached": "⚠️ 이 요금제의 기기 한도에 도달했습니다",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 거의 완료되었습니다!\n\n"
            "원하는 연결 방법을 선택하세요:\n"
            "1. 프로필 파일을 다운로드해 AmneziaWG / WireGuard에 가져오기\n"
            "2. 앱에서 바로 QR 코드를 스캔하기\n\n"
            "📚 알맞은 가이드를 선택하고 몇 단계만 따라 하면 연결돼요.\n\n"
            "⚠️ 하나의 프로필은 한 기기에서만 사용할 수 있어요!"
        ),
        "devices_pick_guide": "📖 아래에서 운영체제별 가이드를 확인하고 순서를 따라 진행하세요.",
        "devices_none": "아직 연결된 기기가 없습니다.",
        "devices_list_intro": "👇 연결된 기기 목록:",
        "devices_select_prompt": "목록에서 기기를 선택해 주세요.",
        "device_default_name": "기기 {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Android 가이드</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 iPhone 가이드</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Windows 가이드</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 macOS 가이드</a>",
        "subscription_intro": (
            "💎 구독\n"
            "✨ 구독 시 제공되는 혜택:\n"
            "• 서비스에 빠르고 안전하게 접속\n"
            "• 광고나 방해 요소 없음\n"
            "• 최고의 가격 — 월 99₽! 🔥\n\n"
            "👉 한 번에 2대 또는 5대용 요금제를 선택하세요."
        ),
        "subscription_duration_prompt": "⏱️ 구독 기간을 선택하세요:\n{options}",
        "subscription_duration_hint": "💡 기간이 길수록 월 이용료가 더 저렴해집니다.",
        "subscription_payment_thanks": (
            "🫶 믿어 주셔서 감사합니다!\n\n"
            "안전하고 안정적이며 빠른 인터넷까지 한 걸음 남았습니다.\n"
            "과정을 최대한 편리하게 준비했어요.\n\n"
            "👇 결제 방법을 선택해 주세요:"
        ),
        "subscription_payment_change": "🔁 요금제를 바꾸고 싶다면 결제 전에 아래 버튼을 이용하세요.",
        "subscription_invalid_plan": "사용 가능한 요금제를 선택해 주세요.",
        "subscription_invalid_duration": "제안된 기간 중 하나를 선택해 주세요.",
        "subscription_payment_created": "결제가 생성되었습니다 (테스트)",
        "plan_devices_2_button": "💫 기기: 2대 - 99₽/월",
        "plan_devices_5_button": "✨ 기기: 5대 - 169₽/월",
        "plan_devices_2_title": "기기 2대",
        "plan_devices_5_title": "기기 5대",
        "plan_devices_2_duration_1m": "1개월 - 99₽",
        "plan_devices_2_duration_3m": "🔹3개월 - 249₽",
        "plan_devices_2_duration_6m": "🔸6개월 - 399₽",
        "plan_devices_5_duration_1m": "1개월 - 169₽",
        "plan_devices_5_duration_3m": "🔹3개월 - 449₽",
        "plan_devices_5_duration_6m": "🔸6개월 - 749₽",
        "faq_title": "❓ 질문",
        "faq_body": (
            "❓ 어떻게 사용하나요?\n"
            "가장 자주 묻는 질문을 한 기사에 모았습니다.\n"
            "📖 FAQ: {faq_url}\n\n"
            "지원 ID: {tg_id}\n\n"
            "🗺 도움이 필요하면 @{support_handle} 에게 메시지를 보내 주세요"
        ),
        "referral_intro": (
            "🤝 친구를 초대하고 보너스 일수를 받으세요.\n\n"
            "링크를 통해 가입한 친구마다 구독에 +7일이 추가됩니다.\n\n"
            "링크를 공유하고 더 오래 무료로 이용하세요."
        ),
        "referral_reward_notification": "🎉 친구가 가입했습니다!\n구독에 +7일이 추가되었어요 ✨",
        "plan_title_trial": "체험 기간",
        "plan_title_device2": "기기 2대",
        "plan_title_device5": "기기 5대",
    },
    "ms": {
        "start_pitch": "🚀 Akses pantas dan mudah terus di Telegram.\nKekalkan privasi dan kestabilan di mana sahaja anda berada.",
        "start_trial_granted": "🎁 Bonus anda: 7 hari percuma!\nNikmati akses pantas dan selamat tanpa had.",
        "status_header": (
            "👋 Peranti anda dan status langganan\n\n"
            "Di sini anda boleh lihat peranti yang disambungkan dan pelan yang sedang aktif."
        ),
        "status_plan_line": "📦 Pelan anda: {plan_title}",
        "status_devices_counter": "(Peranti: {connected} / {limit})",
        "status_connections_header": "📟 Sambungan:",
        "status_connections_empty": "Belum ada peranti disambungkan",
        "status_active_line": "🕒 Langganan aktif: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 hari untuk setiap rakan yang dijemput",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 saat",
        "time_day_forms": "hari|hari|hari",
        "time_hour_forms": "jam|jam|jam",
        "time_minute_forms": "minit|minit|minit",
        "time_second_forms": "saat|saat|saat",
        "btn_intro_continue": "🚀 Jom mula!",
        "btn_devices": "📱 Peranti",
        "btn_subscription": "💎 Langganan",
        "btn_invite_friend": "🤝 Jemput rakan",
        "btn_questions": "❓ Soalan",
        "btn_main_menu": "🏠 Menu utama",
        "btn_back": "⬅️ Kembali",
        "btn_phone": "📱 Telefon",
        "btn_computer": "💻 Komputer",
        "btn_my_devices": "🔌 Peranti saya",
        "btn_android": "🔴 Panduan Android",
        "btn_ios": "🟢 Panduan iPhone",
        "btn_windows_instructions": "🔴 Panduan Windows",
        "btn_macos_instructions": "🟢 Panduan macOS",
        "btn_share_link": "Kongsi pautan",
        "btn_pay_card": "💳 Kad bank",
        "devices_choose": (
            "📲 Pilih peranti yang ingin disambungkan.\n"
            "(Hanya mengambil beberapa minit — sangat mudah!)"
        ),
        "devices_generation_in_progress": "⏳ Konfigurasi sedang dijana. Tunggu fail atau kod QR.",
        "devices_limit_reached": "⚠️ Had peranti untuk pelan ini telah dicapai",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Sambungan hampir siap!\n\n"
            "Pilih cara yang anda suka:\n"
            "1. Muat turun fail profil dan import ke AmneziaWG / WireGuard\n"
            "2. Imbas kod QR terus dalam aplikasi\n\n"
            "📚 Pilih panduan yang sesuai dan sambung dalam beberapa langkah.\n\n"
            "⚠️ Setiap profil hanya boleh digunakan pada satu peranti!"
        ),
        "devices_pick_guide": "📖 Di bawah terdapat panduan untuk sistem berbeza — pilih sistem anda dan ikut langkahnya.",
        "devices_none": "Anda belum mempunyai peranti yang disambungkan.",
        "devices_list_intro": "👇 Peranti yang disambungkan:",
        "devices_select_prompt": "Sila pilih peranti daripada senarai.",
        "device_default_name": "Peranti {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Panduan Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Panduan iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Panduan Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Panduan macOS</a>",
        "subscription_intro": (
            "💎 Langganan\n"
            "✨ Apa yang anda dapat:\n"
            "• Akses pantas dan selamat ke perkhidmatan anda\n"
            "• Tiada iklan atau gangguan\n"
            "• Harga terbaik — hanya 99₽ sebulan! 🔥\n\n"
            "👉 Pilih pelan untuk 2 atau 5 peranti serentak."
        ),
        "subscription_duration_prompt": "⏱️ Pilih tempoh langganan:\n{options}",
        "subscription_duration_hint": "💡 Tempoh yang lebih panjang menjadikan harga bulanan lebih rendah.",
        "subscription_payment_thanks": (
            "🫶 Terima kasih atas kepercayaan anda!\n\n"
            "Anda selangkah lagi ke internet yang selamat, stabil dan pantas.\n"
            "Kami menjadikan proses ini senyaman mungkin.\n\n"
            "👇 Pilih kaedah pembayaran:"
        ),
        "subscription_payment_change": "🔁 Mahu tukar pelan? Gunakan butang di bawah sebelum membuat pembayaran.",
        "subscription_invalid_plan": "Sila pilih salah satu pelan yang tersedia.",
        "subscription_invalid_duration": "Sila pilih salah satu tempoh yang dicadangkan.",
        "subscription_payment_created": "Pembayaran dibuat (ujian)",
        "plan_devices_2_button": "💫 Peranti: 2 - 99₽/bulan",
        "plan_devices_5_button": "✨ Peranti: 5 - 169₽/bulan",
        "plan_devices_2_title": "2 peranti",
        "plan_devices_5_title": "5 peranti",
        "plan_devices_2_duration_1m": "1 bulan - 99₽",
        "plan_devices_2_duration_3m": "🔹3 bulan - 249₽",
        "plan_devices_2_duration_6m": "🔸6 bulan - 399₽",
        "plan_devices_5_duration_1m": "1 bulan - 169₽",
        "plan_devices_5_duration_3m": "🔹3 bulan - 449₽",
        "plan_devices_5_duration_6m": "🔸6 bulan - 749₽",
        "faq_title": "❓ Soalan",
        "faq_body": (
            "❓ Bagaimana, apa dan mengapa?\n"
            "Kami kumpulkan soalan paling popular dalam satu artikel.\n"
            "📖 Soalan Lazim: {faq_url}\n\n"
            "ID sokongan anda: {tg_id}\n\n"
            "🗺 Perlukan bantuan? Hubungi @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Jemput rakan — dapatkan hari bonus.\n\n"
            "Setiap rakan yang sambung melalui pautan anda menambah +7 hari pada langganan.\n\n"
            "Kongsi pautan dan nikmati internet lebih lama secara percuma."
        ),
        "referral_reward_notification": "🎉 Rakan anda telah menyertai!\nAnda menerima +7 hari langganan ✨",
        "plan_title_trial": "Tempoh percubaan",
        "plan_title_device2": "2 peranti",
        "plan_title_device5": "5 peranti",
    },
    "no": {
        "start_pitch": "🚀 Rask og enkel tilgang direkte i Telegram.\nBehold personvernet og stabiliteten uansett hvor du er.",
        "start_trial_granted": "🎁 Din bonus: 7 dager gratis!\nOpplev rask og sikker tilgang uten begrensninger.",
        "status_header": (
            "👋 Enhetene dine og abonnementet ditt\n\n"
            "Her ser du hvilke enheter som er tilkoblet og hvilket abonnement du har."
        ),
        "status_plan_line": "📦 Planen din: {plan_title}",
        "status_devices_counter": "(Enheter: {connected} / {limit})",
        "status_connections_header": "📟 Tilkoblinger:",
        "status_connections_empty": "Ingen tilkoblinger ennå",
        "status_active_line": "🕒 Abonnement aktivt: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 dager for hver venn du inviterer",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 sekunder",
        "time_day_forms": "dag|dager|dager",
        "time_hour_forms": "time|timer|timer",
        "time_minute_forms": "minutt|minutter|minutter",
        "time_second_forms": "sekund|sekunder|sekunder",
        "btn_intro_continue": "🚀 La oss starte!",
        "btn_devices": "📱 Enheter",
        "btn_subscription": "💎 Abonnement",
        "btn_invite_friend": "🤝 Inviter en venn",
        "btn_questions": "❓ Spørsmål",
        "btn_main_menu": "🏠 Hovedmeny",
        "btn_back": "⬅️ Tilbake",
        "btn_phone": "📱 Telefon",
        "btn_computer": "💻 Datamaskin",
        "btn_my_devices": "🔌 Mine enheter",
        "btn_android": "🔴 Veiledning for Android",
        "btn_ios": "🟢 Veiledning for iPhone",
        "btn_windows_instructions": "🔴 Veiledning for Windows",
        "btn_macos_instructions": "🟢 Veiledning for macOS",
        "btn_share_link": "Del lenke",
        "btn_pay_card": "💳 Bankkort",
        "devices_choose": (
            "📲 Velg enheten du vil koble til.\n"
            "(Det tar bare noen minutter — superenkelt!)"
        ),
        "devices_generation_in_progress": "⏳ Konfigurasjonen genereres. Vent på filen eller QR-koden.",
        "devices_limit_reached": "⚠️ Du har nådd enhetsgrensen for denne planen",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Tilkoblingen er nesten klar!\n\n"
            "Velg metoden som passer deg:\n"
            "1. Last ned profilfilen og importer den i AmneziaWG / WireGuard\n"
            "2. Skann QR-koden direkte i appen\n\n"
            "📚 Velg riktig veiledning og koble til på få trinn.\n\n"
            "⚠️ Hver profil kan bare brukes på én enhet!"
        ),
        "devices_pick_guide": "📖 Nedenfor finner du veiledninger for ulike systemer — velg din og følg trinnene.",
        "devices_none": "Du har ingen tilkoblede enheter ennå.",
        "devices_list_intro": "👇 Tilkoblede enheter:",
        "devices_select_prompt": "Velg en enhet fra listen.",
        "device_default_name": "Enhet {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Veiledning for Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Veiledning for iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Veiledning for Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Veiledning for macOS</a>",
        "subscription_intro": (
            "💎 Abonnement\n"
            "✨ Dette får du:\n"
            "• Rask og sikker tilgang til tjenestene dine\n"
            "• Ingen reklame eller forstyrrelser\n"
            "• Beste pris — kun 99₽ per måned! 🔥\n\n"
            "👉 Velg en plan for 2 eller 5 enheter samtidig."
        ),
        "subscription_duration_prompt": "⏱️ Velg varigheten på abonnementet:\n{options}",
        "subscription_duration_hint": "💡 Lengre perioder gir lavere månedspris.",
        "subscription_payment_thanks": (
            "🫶 Takk for tilliten!\n\n"
            "Du er ett steg unna sikker, stabil og rask internett.\n"
            "Vi har gjort prosessen så enkel som mulig.\n\n"
            "👇 Velg betalingsmetode:"
        ),
        "subscription_payment_change": "🔁 Vil du endre plan? Bruk knappene under før du betaler.",
        "subscription_invalid_plan": "Velg en av de tilgjengelige planene.",
        "subscription_invalid_duration": "Velg en av de foreslåtte varighetene.",
        "subscription_payment_created": "Betaling opprettet (test)",
        "plan_devices_2_button": "💫 Enheter: 2 - 99₽/mnd",
        "plan_devices_5_button": "✨ Enheter: 5 - 169₽/mnd",
        "plan_devices_2_title": "2 enheter",
        "plan_devices_5_title": "5 enheter",
        "plan_devices_2_duration_1m": "1 måned - 99₽",
        "plan_devices_2_duration_3m": "🔹3 måneder - 249₽",
        "plan_devices_2_duration_6m": "🔸6 måneder - 399₽",
        "plan_devices_5_duration_1m": "1 måned - 169₽",
        "plan_devices_5_duration_3m": "🔹3 måneder - 449₽",
        "plan_devices_5_duration_6m": "🔸6 måneder - 749₽",
        "faq_title": "❓ Spørsmål",
        "faq_body": (
            "❓ Hvordan, hva og hvorfor?\n"
            "Vi har samlet de vanligste spørsmålene i én artikkel.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Din støtte-ID: {tg_id}\n\n"
            "🗺 Trenger du hjelp? Kontakt @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Inviter venner — få bonusdager.\n\n"
            "Hver venn som kobler seg til via lenken din gir +7 dager på abonnementet.\n\n"
            "Del lenken og surf lenger gratis."
        ),
        "referral_reward_notification": "🎉 Vennen din har blitt med!\nDu fikk +7 dager i abonnementet ✨",
        "plan_title_trial": "Prøveperiode",
        "plan_title_device2": "2 enheter",
        "plan_title_device5": "5 enheter",
    },
    "fa": {
        "start_pitch": "🚀 دسترسی سریع و آسان مستقیماً در تلگرام.\nدر هر جایی که هستی حریم خصوصی و پایداری را حفظ کن.",
        "start_trial_granted": "🎁 هدیه‌ات: ۷ روز رایگان!\nاز دسترسی سریع و امن بدون محدودیت لذت ببر.",
        "status_header": (
            "👋 دستگاه‌ها و وضعیت اشتراک تو\n\n"
            "اینجا می‌توانی ببینی چه دستگاه‌هایی متصل هستند و چه طرحی داری."
        ),
        "status_plan_line": "📦 طرح تو: {plan_title}",
        "status_devices_counter": "(دستگاه‌ها: {connected} / {limit})",
        "status_connections_header": "📟 اتصال‌ها:",
        "status_connections_empty": "هنوز دستگاهی متصل نشده است",
        "status_active_line": "🕒 اشتراک فعال است: {duration}",
        "status_bonus_line": "🎁 هدیه: برای هر دوست دعوت‌شده +۷ روز",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "۰ ثانیه",
        "time_day_forms": "روز|روز|روز",
        "time_hour_forms": "ساعت|ساعت|ساعت",
        "time_minute_forms": "دقیقه|دقیقه|دقیقه",
        "time_second_forms": "ثانیه|ثانیه|ثانیه",
        "btn_intro_continue": "🚀 بزن بریم!",
        "btn_devices": "📱 دستگاه‌ها",
        "btn_subscription": "💎 اشتراک",
        "btn_invite_friend": "🤝 دعوت از دوست",
        "btn_questions": "❓ سوالات",
        "btn_main_menu": "🏠 منوی اصلی",
        "btn_back": "⬅️ بازگشت",
        "btn_phone": "📱 تلفن",
        "btn_computer": "💻 کامپیوتر",
        "btn_my_devices": "🔌 دستگاه‌های من",
        "btn_android": "🔴 راهنمای Android",
        "btn_ios": "🟢 راهنمای iPhone",
        "btn_windows_instructions": "🔴 راهنمای Windows",
        "btn_macos_instructions": "🟢 راهنمای macOS",
        "btn_share_link": "اشتراک‌گذاری لینک",
        "btn_pay_card": "💳 کارت بانکی",
        "devices_choose": (
            "📲 دستگاهی را که می‌خواهی وصل کنی انتخاب کن.\n"
            "(فقط چند دقیقه زمان می‌برد — خیلی ساده است!)"
        ),
        "devices_generation_in_progress": "⏳ پیکربندی در حال آماده‌سازی است. منتظر فایل یا کد QR بمان.",
        "devices_limit_reached": "⚠️ محدودیت دستگاه در این طرح پر شده است",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 اتصال تقریباً آماده است!\n\n"
            "روش مناسب را انتخاب کن:\n"
            "1. فایل پروفایل را دانلود کن و در AmneziaWG / WireGuard وارد کن\n"
            "2. کد QR را مستقیماً در اپلیکیشن اسکن کن\n\n"
            "📚 راهنمای مناسب را انتخاب کن و در چند مرحله وصل شو.\n\n"
            "⚠️ هر پروفایل فقط روی یک دستگاه قابل استفاده است!"
        ),
        "devices_pick_guide": "📖 در ادامه راهنماهای سیستم‌های مختلف را می‌بینی — سیستم خودت را انتخاب کن و مراحل را دنبال کن.",
        "devices_none": "هنوز دستگاه متصل نداری.",
        "devices_list_intro": "👇 دستگاه‌های متصل تو:",
        "devices_select_prompt": "لطفاً دستگاهی را از فهرست انتخاب کن.",
        "device_default_name": "دستگاه {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 راهنمای Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 راهنمای iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 راهنمای Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 راهنمای macOS</a>",
        "subscription_intro": (
            "💎 اشتراک\n"
            "✨ با اشتراک چه دریافت می‌کنی:\n"
            "• دسترسی سریع و امن به سرویس‌هایت\n"
            "• بدون تبلیغ و حواس‌پرتی\n"
            "• بهترین قیمت — فقط 99₽ در ماه! 🔥\n\n"
            "👉 طرحی برای ۲ یا ۵ دستگاه به صورت همزمان انتخاب کن."
        ),
        "subscription_duration_prompt": "⏱️ مدت اشتراک را انتخاب کن:\n{options}",
        "subscription_duration_hint": "💡 هرچه مدت طولانی‌تر باشد، هزینه ماهانه کمتر می‌شود.",
        "subscription_payment_thanks": (
            "🫶 ممنون از اعتمادت!\n\n"
            "یک قدم تا اینترنت امن، پایدار و سریع فاصله داری.\n"
            "ما فرایند را تا حد ممکن راحت کرده‌ایم.\n\n"
            "👇 روش پرداخت را انتخاب کن:"
        ),
        "subscription_payment_change": "🔁 می‌خواهی طرح را تغییر دهی؟ قبل از پرداخت از دکمه‌های زیر استفاده کن.",
        "subscription_invalid_plan": "یکی از طرح‌های موجود را انتخاب کن.",
        "subscription_invalid_duration": "لطفاً یکی از مدت‌های پیشنهاد شده را انتخاب کن.",
        "subscription_payment_created": "پرداخت ایجاد شد (آزمایشی)",
        "plan_devices_2_button": "💫 دستگاه‌ها: 2 - 99₽/ماه",
        "plan_devices_5_button": "✨ دستگاه‌ها: 5 - 169₽/ماه",
        "plan_devices_2_title": "۲ دستگاه",
        "plan_devices_5_title": "۵ دستگاه",
        "plan_devices_2_duration_1m": "۱ ماه - 99₽",
        "plan_devices_2_duration_3m": "🔹۳ ماه - 249₽",
        "plan_devices_2_duration_6m": "🔸۶ ماه - 399₽",
        "plan_devices_5_duration_1m": "۱ ماه - 169₽",
        "plan_devices_5_duration_3m": "🔹۳ ماه - 449₽",
        "plan_devices_5_duration_6m": "🔸۶ ماه - 749₽",
        "faq_title": "❓ سوالات",
        "faq_body": (
            "❓ چطور، چه و چرا؟\n"
            "پر تکرارترین سوال‌ها را در یک مقاله جمع کرده‌ایم.\n"
            "📖 سوالات متداول: {faq_url}\n\n"
            "شناسه پشتیبانی تو: {tg_id}\n\n"
            "🗺 نیاز به کمک داری؟ به @{support_handle} پیام بده"
        ),
        "referral_intro": (
            "🤝 دوستانت را دعوت کن — روزهای هدیه بگیر.\n\n"
            "هر دوستی که با لینک تو وصل شود، +۷ روز به اشتراکت اضافه می‌کند.\n\n"
            "لینک را به اشتراک بگذار و مدت بیشتری رایگان استفاده کن."
        ),
        "referral_reward_notification": "🎉 دوستت پیوست!\n+۷ روز به اشتراکت اضافه شد ✨",
        "plan_title_trial": "دوره آزمایشی",
        "plan_title_device2": "۲ دستگاه",
        "plan_title_device5": "۵ دستگاه",
    },
    "pl": {
        "start_pitch": "🚀 Szybki i prosty dostęp prosto w Telegramie.\nZachowaj prywatność i stabilność gdziekolwiek jesteś.",
        "start_trial_granted": "🎁 Twój bonus: 7 dni za darmo!\nKorzystaj z szybkiego i bezpiecznego dostępu bez ograniczeń.",
        "status_header": (
            "👋 Twoje urządzenia i status subskrypcji\n\n"
            "Tutaj sprawdzisz, które urządzenia są podłączone i jaki masz plan."
        ),
        "status_plan_line": "📦 Twój plan: {plan_title}",
        "status_devices_counter": "(Urządzenia: {connected} / {limit})",
        "status_connections_header": "📟 Połączenia:",
        "status_connections_empty": "Brak połączonych urządzeń",
        "status_active_line": "🕒 Subskrypcja aktywna: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 dni za każdego zaproszonego znajomego",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 sekund",
        "time_day_forms": "dzień|dni|dni",
        "time_hour_forms": "godzina|godziny|godzin",
        "time_minute_forms": "minuta|minuty|minut",
        "time_second_forms": "sekunda|sekundy|sekund",
        "btn_intro_continue": "🚀 Zaczynamy!",
        "btn_devices": "📱 Urządzenia",
        "btn_subscription": "💎 Subskrypcja",
        "btn_invite_friend": "🤝 Zaproś znajomego",
        "btn_questions": "❓ Pytania",
        "btn_main_menu": "🏠 Menu główne",
        "btn_back": "⬅️ Wstecz",
        "btn_phone": "📱 Telefon",
        "btn_computer": "💻 Komputer",
        "btn_my_devices": "🔌 Moje urządzenia",
        "btn_android": "🔴 Instrukcja Android",
        "btn_ios": "🟢 Instrukcja iPhone",
        "btn_windows_instructions": "🔴 Instrukcja Windows",
        "btn_macos_instructions": "🟢 Instrukcja macOS",
        "btn_share_link": "Udostępnij link",
        "btn_pay_card": "💳 Karta płatnicza",
        "devices_choose": (
            "📲 Wybierz urządzenie, które chcesz podłączyć.\n"
            "(To zajmie tylko kilka minut — bardzo proste!)"
        ),
        "devices_generation_in_progress": "⏳ Konfiguracja jest już tworzona. Poczekaj na plik lub kod QR.",
        "devices_limit_reached": "⚠️ Osiągnięto limit urządzeń w tym planie",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Połączenie prawie gotowe!\n\n"
            "Wybierz dogodną metodę:\n"
            "1. Pobierz plik profilu i zaimportuj do AmneziaWG / WireGuard\n"
            "2. Zeskanuj kod QR bezpośrednio w aplikacji\n\n"
            "📚 Wybierz odpowiednią instrukcję i połącz się w kilku krokach.\n\n"
            "⚠️ Każdy profil można używać tylko na jednym urządzeniu!"
        ),
        "devices_pick_guide": "📖 Poniżej znajdziesz instrukcje dla różnych systemów — wybierz swoją i postępuj według kroków.",
        "devices_none": "Nie masz jeszcze żadnych podłączonych urządzeń.",
        "devices_list_intro": "👇 Lista podłączonych urządzeń:",
        "devices_select_prompt": "Wybierz urządzenie z listy.",
        "device_default_name": "Urządzenie {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Instrukcja Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Instrukcja iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Instrukcja Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Instrukcja macOS</a>",
        "subscription_intro": (
            "💎 Subskrypcja\n"
            "✨ Co zyskujesz:\n"
            "• Szybki i bezpieczny dostęp do swoich usług\n"
            "• Zero reklam i rozpraszaczy\n"
            "• Najlepsza cena — tylko 99₽ miesięcznie! 🔥\n\n"
            "👉 Wybierz plan dla 2 lub 5 urządzeń jednocześnie."
        ),
        "subscription_duration_prompt": "⏱️ Wybierz czas trwania subskrypcji:\n{options}",
        "subscription_duration_hint": "💡 Im dłuższy okres, tym niższa cena miesięczna.",
        "subscription_payment_thanks": (
            "🫶 Dziękujemy za zaufanie!\n\n"
            "Jesteś o krok od bezpiecznego, stabilnego i szybkiego internetu.\n"
            "Zadbaliśmy o maksymalną wygodę procesu.\n\n"
            "👇 Wybierz metodę płatności:"
        ),
        "subscription_payment_change": "🔁 Chcesz zmienić plan? Użyj przycisków poniżej przed płatnością.",
        "subscription_invalid_plan": "Wybierz jeden z dostępnych planów.",
        "subscription_invalid_duration": "Wybierz jedną z proponowanych opcji.",
        "subscription_payment_created": "Płatność utworzona (test)",
        "plan_devices_2_button": "💫 Urządzenia: 2 - 99₽/msc",
        "plan_devices_5_button": "✨ Urządzenia: 5 - 169₽/msc",
        "plan_devices_2_title": "2 urządzenia",
        "plan_devices_5_title": "5 urządzeń",
        "plan_devices_2_duration_1m": "1 miesiąc - 99₽",
        "plan_devices_2_duration_3m": "🔹3 miesiące - 249₽",
        "plan_devices_2_duration_6m": "🔸6 miesięcy - 399₽",
        "plan_devices_5_duration_1m": "1 miesiąc - 169₽",
        "plan_devices_5_duration_3m": "🔹3 miesiące - 449₽",
        "plan_devices_5_duration_6m": "🔸6 miesięcy - 749₽",
        "faq_title": "❓ Pytania",
        "faq_body": (
            "❓ Jak, co i dlaczego?\n"
            "Najczęstsze pytania zebraliśmy w jednym artykule.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Twój identyfikator wsparcia: {tg_id}\n\n"
            "🗺 Potrzebujesz pomocy? Napisz do @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Zaproś znajomych — zyskaj dodatkowe dni.\n\n"
            "Każdy, kto dołączy z Twojego linku, dodaje +7 dni do subskrypcji.\n\n"
            "Udostępnij link i korzystaj dłużej za darmo."
        ),
        "referral_reward_notification": "🎉 Twój znajomy dołączył!\nOtrzymałeś +7 dni subskrypcji ✨",
        "plan_title_trial": "Okres próbny",
        "plan_title_device2": "2 urządzenia",
        "plan_title_device5": "5 urządzeń",
    },
    "pt-br": {
        "start_pitch": "🚀 Acesso rápido e fácil direto no Telegram.\nMantenha a privacidade e a estabilidade onde estiver.",
        "start_trial_granted": "🎁 Seu bônus: 7 dias grátis!\nAproveite acesso rápido e seguro sem limites.",
        "status_header": (
            "👋 Seus dispositivos e o status da assinatura\n\n"
            "Aqui você confere quais dispositivos estão conectados e qual plano está ativo."
        ),
        "status_plan_line": "📦 Seu plano: {plan_title}",
        "status_devices_counter": "(Dispositivos: {connected} / {limit})",
        "status_connections_header": "📟 Conexões:",
        "status_connections_empty": "Ainda não há conexões",
        "status_active_line": "🕒 Assinatura ativa: {duration}",
        "status_bonus_line": "🎁 Bônus: +7 dias para cada amigo convidado",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 segundos",
        "time_day_forms": "dia|dias|dias",
        "time_hour_forms": "hora|horas|horas",
        "time_minute_forms": "minuto|minutos|minutos",
        "time_second_forms": "segundo|segundos|segundos",
        "btn_intro_continue": "🚀 Vamos lá!",
        "btn_devices": "📱 Dispositivos",
        "btn_subscription": "💎 Assinatura",
        "btn_invite_friend": "🤝 Convidar amigo",
        "btn_questions": "❓ Dúvidas",
        "btn_main_menu": "🏠 Menu principal",
        "btn_back": "⬅️ Voltar",
        "btn_phone": "📱 Celular",
        "btn_computer": "💻 Computador",
        "btn_my_devices": "🔌 Meus dispositivos",
        "btn_android": "🔴 Guia Android",
        "btn_ios": "🟢 Guia iPhone",
        "btn_windows_instructions": "🔴 Guia Windows",
        "btn_macos_instructions": "🟢 Guia macOS",
        "btn_share_link": "Compartilhar link",
        "btn_pay_card": "💳 Cartão bancário",
        "devices_choose": (
            "📲 Escolha o dispositivo que deseja conectar.\n"
            "(Leva só alguns minutos — super simples!)"
        ),
        "devices_generation_in_progress": "⏳ A configuração já está sendo gerada. Aguarde o arquivo ou o QR code.",
        "devices_limit_reached": "⚠️ Limite de dispositivos atingido neste plano",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 A conexão está quase pronta!\n\n"
            "Escolha o melhor jeito para você:\n"
            "1. Baixe o arquivo de perfil e importe no AmneziaWG / WireGuard\n"
            "2. Escaneie o QR code direto no app\n\n"
            "📚 Selecione o guia ideal e conecte-se em poucos passos.\n\n"
            "⚠️ Cada perfil pode ser usado em apenas um dispositivo!"
        ),
        "devices_pick_guide": "📖 Abaixo estão guias para vários sistemas — escolha o seu e siga o passo a passo.",
        "devices_none": "Você ainda não tem dispositivos conectados.",
        "devices_list_intro": "👇 Seus dispositivos conectados:",
        "devices_select_prompt": "Escolha um dispositivo da lista.",
        "device_default_name": "Dispositivo {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guia Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guia iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guia Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guia macOS</a>",
        "subscription_intro": (
            "💎 Assinatura\n"
            "✨ O que você recebe:\n"
            "• Acesso rápido e seguro aos seus serviços\n"
            "• Sem anúncios ou distrações\n"
            "• Melhor preço — apenas 99₽ por mês! 🔥\n\n"
            "👉 Escolha um plano para 2 ou 5 dispositivos de uma vez."
        ),
        "subscription_duration_prompt": "⏱️ Escolha o período da assinatura:\n{options}",
        "subscription_duration_hint": "💡 Períodos mais longos reduzem o valor mensal.",
        "subscription_payment_thanks": (
            "🫶 Obrigado pela confiança!\n\n"
            "Você está a um passo de uma internet segura, estável e rápida.\n"
            "Deixamos tudo o mais prático possível.\n\n"
            "👇 Escolha a forma de pagamento:"
        ),
        "subscription_payment_change": "🔁 Quer trocar o plano? Use os botões abaixo antes de pagar.",
        "subscription_invalid_plan": "Selecione um dos planos disponíveis.",
        "subscription_invalid_duration": "Escolha um dos períodos sugeridos.",
        "subscription_payment_created": "Pagamento criado (teste)",
        "plan_devices_2_button": "💫 Dispositivos: 2 - 99₽/mês",
        "plan_devices_5_button": "✨ Dispositivos: 5 - 169₽/mês",
        "plan_devices_2_title": "2 dispositivos",
        "plan_devices_5_title": "5 dispositivos",
        "plan_devices_2_duration_1m": "1 mês - 99₽",
        "plan_devices_2_duration_3m": "🔹3 meses - 249₽",
        "plan_devices_2_duration_6m": "🔸6 meses - 399₽",
        "plan_devices_5_duration_1m": "1 mês - 169₽",
        "plan_devices_5_duration_3m": "🔹3 meses - 449₽",
        "plan_devices_5_duration_6m": "🔸6 meses - 749₽",
        "faq_title": "❓ Dúvidas",
        "faq_body": (
            "❓ Como, o quê e por quê?\n"
            "Reunimos as perguntas mais frequentes em um único artigo.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Seu ID de suporte: {tg_id}\n\n"
            "🗺 Precisa de ajuda? Fale com @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Convide amigos — ganhe dias extra.\n\n"
            "Cada amigo que se conecta pelo seu link adiciona +7 dias à assinatura.\n\n"
            "Compartilhe o link e navegue mais tempo de graça."
        ),
        "referral_reward_notification": "🎉 Seu amigo entrou!\nVocê ganhou +7 dias de assinatura ✨",
        "plan_title_trial": "Período de teste",
        "plan_title_device2": "2 dispositivos",
        "plan_title_device5": "5 dispositivos",
    },
    "ro": {
        "start_pitch": "🚀 Acces rapid și ușor direct în Telegram.\nPăstrează-ți confidențialitatea și stabilitatea oriunde te-ai afla.",
        "start_trial_granted": "🎁 Bonusul tău: 7 zile gratuit!\nBucură-te de un acces rapid și sigur fără limite.",
        "status_header": (
            "👋 Dispozitivele și starea abonamentului tău\n\n"
            "Aici vezi ce dispozitive sunt conectate și ce plan ai activ."
        ),
        "status_plan_line": "📦 Planul tău: {plan_title}",
        "status_devices_counter": "(Dispozitive: {connected} / {limit})",
        "status_connections_header": "📟 Conexiuni:",
        "status_connections_empty": "Încă nu ai conexiuni",
        "status_active_line": "🕒 Abonament activ: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 zile pentru fiecare prieten invitat",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 secunde",
        "time_day_forms": "zi|zile|zile",
        "time_hour_forms": "oră|ore|ore",
        "time_minute_forms": "minut|minute|minute",
        "time_second_forms": "secundă|secunde|secunde",
        "btn_intro_continue": "🚀 Să începem!",
        "btn_devices": "📱 Dispozitive",
        "btn_subscription": "💎 Abonament",
        "btn_invite_friend": "🤝 Invită un prieten",
        "btn_questions": "❓ Întrebări",
        "btn_main_menu": "🏠 Meniu principal",
        "btn_back": "⬅️ Înapoi",
        "btn_phone": "📱 Telefon",
        "btn_computer": "💻 Calculator",
        "btn_my_devices": "🔌 Dispozitivele mele",
        "btn_android": "🔴 Ghid Android",
        "btn_ios": "🟢 Ghid iPhone",
        "btn_windows_instructions": "🔴 Ghid Windows",
        "btn_macos_instructions": "🟢 Ghid macOS",
        "btn_share_link": "Distribuie linkul",
        "btn_pay_card": "💳 Card bancar",
        "devices_choose": (
            "📲 Alege dispozitivul pe care vrei să-l conectezi.\n"
            "(Durează doar câteva minute — foarte simplu!)"
        ),
        "devices_generation_in_progress": "⏳ Configurația este deja generată. Așteaptă fișierul sau codul QR.",
        "devices_limit_reached": "⚠️ Ai atins limita de dispozitive pentru acest plan",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Conexiunea este aproape gata!\n\n"
            "Alege metoda preferată:\n"
            "1. Descarcă fișierul profil și importă-l în AmneziaWG / WireGuard\n"
            "2. Scanează codul QR direct în aplicație\n\n"
            "📚 Alege ghidul potrivit și conectează-te în câțiva pași.\n\n"
            "⚠️ Fiecare profil poate fi folosit doar pe un singur dispozitiv!"
        ),
        "devices_pick_guide": "📖 Mai jos găsești ghiduri pentru diferite sisteme — alege-l pe al tău și urmează pașii.",
        "devices_none": "Nu ai încă dispozitive conectate.",
        "devices_list_intro": "👇 Dispozitivele tale conectate:",
        "devices_select_prompt": "Alege un dispozitiv din listă.",
        "device_default_name": "Dispozitiv {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Ghid Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Ghid iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Ghid Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Ghid macOS</a>",
        "subscription_intro": (
            "💎 Abonament\n"
            "✨ Ce îți oferă abonamentul:\n"
            "• Acces rapid și sigur la serviciile tale\n"
            "• Fără reclame sau distrageri\n"
            "• Cel mai bun preț — doar 99₽ pe lună! 🔥\n\n"
            "👉 Alege un plan pentru 2 sau 5 dispozitive dintr-o dată."
        ),
        "subscription_duration_prompt": "⏱️ Alege durata abonamentului:\n{options}",
        "subscription_duration_hint": "💡 Cu cât perioada este mai lungă, cu atât costul lunar scade.",
        "subscription_payment_thanks": (
            "🫶 Îți mulțumim pentru încredere!\n\n"
            "Ești la un pas de un internet sigur, stabil și rapid.\n"
            "Am făcut procesul cât mai comod.\n\n"
            "👇 Alege metoda de plată:"
        ),
        "subscription_payment_change": "🔁 Vrei să schimbi planul? Folosește butoanele de mai jos înainte de plată.",
        "subscription_invalid_plan": "Selectează unul dintre planurile disponibile.",
        "subscription_invalid_duration": "Te rugăm să alegi una dintre duratele propuse.",
        "subscription_payment_created": "Plata creată (test)",
        "plan_devices_2_button": "💫 Dispozitive: 2 - 99₽/lună",
        "plan_devices_5_button": "✨ Dispozitive: 5 - 169₽/lună",
        "plan_devices_2_title": "2 dispozitive",
        "plan_devices_5_title": "5 dispozitive",
        "plan_devices_2_duration_1m": "1 lună - 99₽",
        "plan_devices_2_duration_3m": "🔹3 luni - 249₽",
        "plan_devices_2_duration_6m": "🔸6 luni - 399₽",
        "plan_devices_5_duration_1m": "1 lună - 169₽",
        "plan_devices_5_duration_3m": "🔹3 luni - 449₽",
        "plan_devices_5_duration_6m": "🔸6 luni - 749₽",
        "faq_title": "❓ Întrebări",
        "faq_body": (
            "❓ Cum, ce și de ce?\n"
            "Am adunat cele mai frecvente întrebări într-un singur articol.\n"
            "📖 FAQ: {faq_url}\n\n"
            "ID-ul tău de suport: {tg_id}\n\n"
            "🗺 Ai nevoie de ajutor? Scrie la @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Invită prieteni — primești zile bonus.\n\n"
            "Fiecare prieten care se conectează cu linkul tău adaugă +7 zile abonamentului.\n\n"
            "Distribuie linkul și navighează mai mult gratis."
        ),
        "referral_reward_notification": "🎉 Prietenul tău s-a alăturat!\nAi primit +7 zile de abonament ✨",
        "plan_title_trial": "Perioadă de probă",
        "plan_title_device2": "2 dispozitive",
        "plan_title_device5": "5 dispozitive",
    },
    "sr": {
        "start_pitch": "🚀 Брз и једноставан приступ директно у Телеграму.\nСачувај приватност и стабилност где год да си.",
        "start_trial_granted": "🎁 Твој бонус: 7 дана бесплатно!\nУживај у брзом и безбедном приступу без ограничења.",
        "status_header": (
            "👋 Твоји уређаји и статус претплате\n\n"
            "Овде видиш који су уређаји повезани и који пакет користиш."
        ),
        "status_plan_line": "📦 Твој план: {plan_title}",
        "status_devices_counter": "(Уређаји: {connected} / {limit})",
        "status_connections_header": "📟 Везе:",
        "status_connections_empty": "Још нема повезаних уређаја",
        "status_active_line": "🕒 Претплата активна: {duration}",
        "status_bonus_line": "🎁 Бонус: +7 дана за сваког позваног пријатеља",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 секунди",
        "time_day_forms": "дан|дана|дана",
        "time_hour_forms": "сат|сата|сати",
        "time_minute_forms": "минут|минута|минута",
        "time_second_forms": "секунда|секунде|секунди",
        "btn_intro_continue": "🚀 Крећемо!",
        "btn_devices": "📱 Уређаји",
        "btn_subscription": "💎 Претплата",
        "btn_invite_friend": "🤝 Позови пријатеља",
        "btn_questions": "❓ Питања",
        "btn_main_menu": "🏠 Главни мени",
        "btn_back": "⬅️ Назад",
        "btn_phone": "📱 Телефон",
        "btn_computer": "💻 Рачунар",
        "btn_my_devices": "🔌 Моји уређаји",
        "btn_android": "🔴 Упутство за Android",
        "btn_ios": "🟢 Упутство за iPhone",
        "btn_windows_instructions": "🔴 Упутство за Windows",
        "btn_macos_instructions": "🟢 Упутство за macOS",
        "btn_share_link": "Подели линк",
        "btn_pay_card": "💳 Платна картица",
        "devices_choose": (
            "📲 Изабери уређај који желиш да повежеш.\n"
            "(Потребно је само пар минута — врло једноставно!)"
        ),
        "devices_generation_in_progress": "⏳ Конфигурација се већ креира. Сачекај датотеку или QR код.",
        "devices_limit_reached": "⚠️ Достигнут је лимит уређаја за овај план",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Повезивање је скоро готово!\n\n"
            "Изабери начин који ти највише одговара:\n"
            "1. Преузми профил и увези га у AmneziaWG / WireGuard\n"
            "2. Скенирaj QR код директно у апликацији\n\n"
            "📚 Изабери одговарајуће упутство и повежи се за неколико корака.\n\n"
            "⚠️ Сваки профил може да се користи само на једном уређају!"
        ),
        "devices_pick_guide": "📖 Испод се налазе упутства за различите системе — изабери своје и прати кораке.",
        "devices_none": "Још немаш повезаних уређаја.",
        "devices_list_intro": "👇 Твоји повезани уређаји:",
        "devices_select_prompt": "Изабери уређај са листе.",
        "device_default_name": "Уређај {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Упутство за Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Упутство за iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Упутство за Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Упутство за macOS</a>",
        "subscription_intro": (
            "💎 Претплата\n"
            "✨ Шта добијаш:\n"
            "• Брз и безбедан приступ сервисима\n"
            "• Без реклама и ометања\n"
            "• Најбоља цена — само 99₽ месечно! 🔥\n\n"
            "👉 Изабери план за 2 или 5 уређаја одједном."
        ),
        "subscription_duration_prompt": "⏱️ Изабери трајање претплате:\n{options}",
        "subscription_duration_hint": "💡 Дужи период значи мању месечну цену.",
        "subscription_payment_thanks": (
            "🫶 Хвала на поверењу!\n\n"
            "Само си корак од безбедног, стабилног и брзог интернета.\n"
            "Процес смо учинили што је могуће удобнијим.\n\n"
            "👇 Изабери начин плаћања:"
        ),
        "subscription_payment_change": "🔁 Желиш да промениш план? Користи дугмад испод пре плаћања.",
        "subscription_invalid_plan": "Изабери један од доступних планова.",
        "subscription_invalid_duration": "Молимо те изабери једну од понуђених опција.",
        "subscription_payment_created": "Плаћање креирано (тест)",
        "plan_devices_2_button": "💫 Уређаји: 2 - 99₽/мес",
        "plan_devices_5_button": "✨ Уређаји: 5 - 169₽/мес",
        "plan_devices_2_title": "2 уређаја",
        "plan_devices_5_title": "5 уређаја",
        "plan_devices_2_duration_1m": "1 месец - 99₽",
        "plan_devices_2_duration_3m": "🔹3 месеца - 249₽",
        "plan_devices_2_duration_6m": "🔸6 месеци - 399₽",
        "plan_devices_5_duration_1m": "1 месец - 169₽",
        "plan_devices_5_duration_3m": "🔹3 месеца - 449₽",
        "plan_devices_5_duration_6m": "🔸6 месеци - 749₽",
        "faq_title": "❓ Питања",
        "faq_body": (
            "❓ Како, шта и зашто?\n"
            "Најчешћа питања смо окупили у једном тексту.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Твој ID подршке: {tg_id}\n\n"
            "🗺 Треба ти помоћ? Пиши @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Позови пријатеље — добиј додатне дане.\n\n"
            "За сваког ко се прикључи преко твог линка добијаш +7 дана претплате.\n\n"
            "Подели линк и сурфуј дуже бесплатно."
        ),
        "referral_reward_notification": "🎉 Твој пријатељ се придружио!\nДодали смо ти +7 дана претплате ✨",
        "plan_title_trial": "Пробни период",
        "plan_title_device2": "2 уређаја",
        "plan_title_device5": "5 уређаја",
    },
    "sk": {
        "start_pitch": "🚀 Rýchly a jednoduchý prístup priamo v Telegrame.\nZachovaj si súkromie a stabilitu, nech si kdekoľvek.",
        "start_trial_granted": "🎁 Tvoj bonus: 7 dní zadarmo!\nVyskúšaj rýchly a bezpečný prístup bez obmedzení.",
        "status_header": (
            "👋 Tvoje zariadenia a stav predplatného\n\n"
            "Tu zistíš, ktoré zariadenia sú pripojené a aký plán používaš."
        ),
        "status_plan_line": "📦 Tvoj plán: {plan_title}",
        "status_devices_counter": "(Zariadenia: {connected} / {limit})",
        "status_connections_header": "📟 Pripojenia:",
        "status_connections_empty": "Zatiaľ žiadne pripojenia",
        "status_active_line": "🕒 Predplatné aktívne: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 dní za každého pozvaného priateľa",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 sekúnd",
        "time_day_forms": "deň|dni|dní",
        "time_hour_forms": "hodina|hodiny|hodín",
        "time_minute_forms": "minúta|minúty|minút",
        "time_second_forms": "sekunda|sekundy|sekúnd",
        "btn_intro_continue": "🚀 Poďme na to!",
        "btn_devices": "📱 Zariadenia",
        "btn_subscription": "💎 Predplatné",
        "btn_invite_friend": "🤝 Pozvi priateľa",
        "btn_questions": "❓ Otázky",
        "btn_main_menu": "🏠 Hlavné menu",
        "btn_back": "⬅️ Späť",
        "btn_phone": "📱 Telefón",
        "btn_computer": "💻 Počítač",
        "btn_my_devices": "🔌 Moje zariadenia",
        "btn_android": "🔴 Návod pre Android",
        "btn_ios": "🟢 Návod pre iPhone",
        "btn_windows_instructions": "🔴 Návod pre Windows",
        "btn_macos_instructions": "🟢 Návod pre macOS",
        "btn_share_link": "Zdieľať odkaz",
        "btn_pay_card": "💳 Platobná karta",
        "devices_choose": (
            "📲 Vyber zariadenie, ktoré chceš pripojiť.\n"
            "(Zaberie to len pár minút — je to veľmi jednoduché!)"
        ),
        "devices_generation_in_progress": "⏳ Konfigurácia sa už pripravuje. Počkaj na súbor alebo QR kód.",
        "devices_limit_reached": "⚠️ Dosiahol si limit zariadení pre tento plán",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Pripojenie je takmer hotové!\n\n"
            "Vyber si spôsob, ktorý ti vyhovuje:\n"
            "1. Stiahni súbor profilu a importuj ho do AmneziaWG / WireGuard\n"
            "2. Naskenuj QR kód priamo v aplikácii\n\n"
            "📚 Vyber si správny návod a pripoj sa v pár krokoch.\n\n"
            "⚠️ Každý profil je určený len pre jedno zariadenie!"
        ),
        "devices_pick_guide": "📖 Nižšie nájdeš návody pre rôzne systémy — vyber si svoj a postupuj podľa krokov.",
        "devices_none": "Zatiaľ nemáš pripojené žiadne zariadenia.",
        "devices_list_intro": "👇 Zoznam tvojich pripojených zariadení:",
        "devices_select_prompt": "Vyber zariadenie zo zoznamu.",
        "device_default_name": "Zariadenie {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Návod pre Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Návod pre iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Návod pre Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Návod pre macOS</a>",
        "subscription_intro": (
            "💎 Predplatné\n"
            "✨ Čo získaš:\n"
            "• Rýchly a bezpečný prístup k svojim službám\n"
            "• Žiadne reklamy ani rušenie\n"
            "• Najlepšia cena — len 99₽ mesačne! 🔥\n\n"
            "👉 Vyber si plán pre 2 alebo 5 zariadení naraz."
        ),
        "subscription_duration_prompt": "⏱️ Vyber dĺžku predplatného:\n{options}",
        "subscription_duration_hint": "💡 Dlhšie obdobie znamená nižšiu cenu za mesiac.",
        "subscription_payment_thanks": (
            "🫶 Ďakujeme za dôveru!\n\n"
            "Si o krok bližšie k bezpečnému, stabilnému a rýchlemu internetu.\n"
            "Proces sme spravili čo najkomfortnejší.\n\n"
            "👇 Vyber si spôsob platby:"
        ),
        "subscription_payment_change": "🔁 Chceš zmeniť plán? Použi tlačidlá nižšie pred zaplatením.",
        "subscription_invalid_plan": "Vyber jeden z dostupných plánov.",
        "subscription_invalid_duration": "Prosím, vyber jednu z ponúkaných možností.",
        "subscription_payment_created": "Platba vytvorená (test)",
        "plan_devices_2_button": "💫 Zariadenia: 2 - 99₽/mes.",
        "plan_devices_5_button": "✨ Zariadenia: 5 - 169₽/mes.",
        "plan_devices_2_title": "2 zariadenia",
        "plan_devices_5_title": "5 zariadení",
        "plan_devices_2_duration_1m": "1 mesiac - 99₽",
        "plan_devices_2_duration_3m": "🔹3 mesiace - 249₽",
        "plan_devices_2_duration_6m": "🔸6 mesiacov - 399₽",
        "plan_devices_5_duration_1m": "1 mesiac - 169₽",
        "plan_devices_5_duration_3m": "🔹3 mesiace - 449₽",
        "plan_devices_5_duration_6m": "🔸6 mesiacov - 749₽",
        "faq_title": "❓ Otázky",
        "faq_body": (
            "❓ Ako, čo a prečo?\n"
            "Najčastejšie otázky sme dali do jedného článku.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Tvoje ID podpory: {tg_id}\n\n"
            "🗺 Potrebuješ pomoc? Napíš @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Pozvi priateľov — získaj bonusové dni.\n\n"
            "Každý, kto sa pripojí cez tvoj odkaz, pridá +7 dní k predplatnému.\n\n"
            "Zdieľaj odkaz a surfuj dlhšie zadarmo."
        ),
        "referral_reward_notification": "🎉 Tvoj priateľ sa pridal!\nPridali sme ti +7 dní k predplatnému ✨",
        "plan_title_trial": "Skúšobné obdobie",
        "plan_title_device2": "2 zariadenia",
        "plan_title_device5": "5 zariadení",
    },
    "es": {
        "start_pitch": "🚀 Acceso rápido y sencillo directamente en Telegram.\nMantén tu privacidad y estabilidad estés donde estés.",
        "start_trial_granted": "🎁 Tu bono: ¡7 días gratis!\nDisfruta de acceso rápido y seguro sin límites.",
        "status_header": (
            "👋 Tus dispositivos y el estado de tu suscripción\n\n"
            "Aquí puedes ver qué dispositivos están conectados y qué plan tienes."
        ),
        "status_plan_line": "📦 Tu plan: {plan_title}",
        "status_devices_counter": "(Dispositivos: {connected} / {limit})",
        "status_connections_header": "📟 Conexiones:",
        "status_connections_empty": "Aún no hay dispositivos conectados",
        "status_active_line": "🕒 Suscripción activa: {duration}",
        "status_bonus_line": "🎁 Bono: +7 días por cada amigo invitado",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 segundos",
        "time_day_forms": "día|días|días",
        "time_hour_forms": "hora|horas|horas",
        "time_minute_forms": "minuto|minutos|minutos",
        "time_second_forms": "segundo|segundos|segundos",
        "btn_intro_continue": "🚀 ¡Vamos allá!",
        "btn_devices": "📱 Dispositivos",
        "btn_subscription": "💎 Suscripción",
        "btn_invite_friend": "🤝 Invitar a un amigo",
        "btn_questions": "❓ Preguntas",
        "btn_main_menu": "🏠 Menú principal",
        "btn_back": "⬅️ Atrás",
        "btn_phone": "📱 Teléfono",
        "btn_computer": "💻 Computadora",
        "btn_my_devices": "🔌 Mis dispositivos",
        "btn_android": "🔴 Guía Android",
        "btn_ios": "🟢 Guía iPhone",
        "btn_windows_instructions": "🔴 Guía Windows",
        "btn_macos_instructions": "🟢 Guía macOS",
        "btn_share_link": "Compartir enlace",
        "btn_pay_card": "💳 Tarjeta bancaria",
        "devices_choose": (
            "📲 Elige el dispositivo que quieres conectar.\n"
            "(Solo tardarás unos minutos — ¡muy fácil!)"
        ),
        "devices_generation_in_progress": "⏳ La configuración ya se está generando. Espera el archivo o el código QR.",
        "devices_limit_reached": "⚠️ Has alcanzado el límite de dispositivos de este plan",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 ¡La conexión está casi lista!\n\n"
            "Elige cómo prefieres conectarte:\n"
            "1. Descarga el archivo de perfil e impórtalo en AmneziaWG / WireGuard\n"
            "2. Escanea el código QR directamente en la app\n\n"
            "📚 Selecciona la guía adecuada y conéctate en pocos pasos.\n\n"
            "⚠️ Cada perfil solo puede usarse en un dispositivo."
        ),
        "devices_pick_guide": "📖 Abajo encontrarás guías para distintos sistemas — elige la tuya y sigue los pasos.",
        "devices_none": "Todavía no tienes dispositivos conectados.",
        "devices_list_intro": "👇 Tus dispositivos conectados:",
        "devices_select_prompt": "Selecciona un dispositivo de la lista.",
        "device_default_name": "Dispositivo {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guía Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guía iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guía Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guía macOS</a>",
        "subscription_intro": (
            "💎 Suscripción\n"
            "✨ Qué incluye:\n"
            "• Acceso rápido y seguro a tus servicios\n"
            "• Sin anuncios ni distracciones\n"
            "• El mejor precio — ¡solo 99₽ al mes! 🔥\n\n"
            "👉 Elige un plan para 2 o 5 dispositivos a la vez."
        ),
        "subscription_duration_prompt": "⏱️ Elige la duración de la suscripción:\n{options}",
        "subscription_duration_hint": "💡 Cuanto más largo sea el periodo, menor será el precio mensual.",
        "subscription_payment_thanks": (
            "🫶 ¡Gracias por confiar en nosotros!\n\n"
            "Estás a un paso de un internet seguro, estable y rápido.\n"
            "Hicimos el proceso lo más cómodo posible.\n\n"
            "👇 Elige el método de pago:"
        ),
        "subscription_payment_change": "🔁 ¿Quieres cambiar el plan? Usa los botones de abajo antes de pagar.",
        "subscription_invalid_plan": "Selecciona uno de los planes disponibles.",
        "subscription_invalid_duration": "Elige una de las duraciones sugeridas.",
        "subscription_payment_created": "Pago creado (prueba)",
        "plan_devices_2_button": "💫 Dispositivos: 2 - 99₽/mes",
        "plan_devices_5_button": "✨ Dispositivos: 5 - 169₽/mes",
        "plan_devices_2_title": "2 dispositivos",
        "plan_devices_5_title": "5 dispositivos",
        "plan_devices_2_duration_1m": "1 mes - 99₽",
        "plan_devices_2_duration_3m": "🔹3 meses - 249₽",
        "plan_devices_2_duration_6m": "🔸6 meses - 399₽",
        "plan_devices_5_duration_1m": "1 mes - 169₽",
        "plan_devices_5_duration_3m": "🔹3 meses - 449₽",
        "plan_devices_5_duration_6m": "🔸6 meses - 749₽",
        "faq_title": "❓ Preguntas",
        "faq_body": (
            "❓ ¿Cómo, qué y por qué?\n"
            "Reunimos las preguntas más frecuentes en un solo artículo.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Tu ID de soporte: {tg_id}\n\n"
            "🗺 ¿Necesitas ayuda? Escribe a @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Invita a tus amigos — obtén días extra.\n\n"
            "Cada amigo que se conecta con tu enlace suma +7 días a tu suscripción.\n\n"
            "Comparte el enlace y navega más tiempo gratis."
        ),
        "referral_reward_notification": "🎉 ¡Tu amigo se unió!\nRecibiste +7 días de suscripción ✨",
        "plan_title_trial": "Periodo de prueba",
        "plan_title_device2": "2 dispositivos",
        "plan_title_device5": "5 dispositivos",
    },
    "sv": {
        "start_pitch": "🚀 Snabb och enkel åtkomst direkt i Telegram.\nBehåll integritet och stabilitet var du än är.",
        "start_trial_granted": "🎁 Din bonus: 7 dagar gratis!\nNjut av snabb och säker åtkomst utan gränser.",
        "status_header": (
            "👋 Dina enheter och din abonnemangsstatus\n\n"
            "Här ser du vilka enheter som är anslutna och vilket abonnemang du har."
        ),
        "status_plan_line": "📦 Ditt paket: {plan_title}",
        "status_devices_counter": "(Enheter: {connected} / {limit})",
        "status_connections_header": "📟 Anslutningar:",
        "status_connections_empty": "Inga anslutningar ännu",
        "status_active_line": "🕒 Abonnemang aktivt: {duration}",
        "status_bonus_line": "🎁 Bonus: +7 dagar för varje inbjuden vän",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 sekunder",
        "time_day_forms": "dag|dagar|dagar",
        "time_hour_forms": "timme|timmar|timmar",
        "time_minute_forms": "minut|minuter|minuter",
        "time_second_forms": "sekund|sekunder|sekunder",
        "btn_intro_continue": "🚀 Vi kör!",
        "btn_devices": "📱 Enheter",
        "btn_subscription": "💎 Abonnemang",
        "btn_invite_friend": "🤝 Bjud in en vän",
        "btn_questions": "❓ Frågor",
        "btn_main_menu": "🏠 Huvudmeny",
        "btn_back": "⬅️ Tillbaka",
        "btn_phone": "📱 Telefon",
        "btn_computer": "💻 Dator",
        "btn_my_devices": "🔌 Mina enheter",
        "btn_android": "🔴 Guide för Android",
        "btn_ios": "🟢 Guide för iPhone",
        "btn_windows_instructions": "🔴 Guide för Windows",
        "btn_macos_instructions": "🟢 Guide för macOS",
        "btn_share_link": "Dela länk",
        "btn_pay_card": "💳 Bankkort",
        "devices_choose": (
            "📲 Välj enheten du vill ansluta.\n"
            "(Det tar bara några minuter — superenkelt!)"
        ),
        "devices_generation_in_progress": "⏳ Konfigurationen genereras. Vänta på filen eller QR-koden.",
        "devices_limit_reached": "⚠️ Du har nått gränsen för detta paket",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Anslutningen är nästan klar!\n\n"
            "Välj det sätt som passar dig:\n"
            "1. Ladda ner profilfilen och importera den i AmneziaWG / WireGuard\n"
            "2. Skanna QR-koden direkt i appen\n\n"
            "📚 Välj rätt guide och anslut på några få steg.\n\n"
            "⚠️ Varje profil kan bara användas på en enhet!"
        ),
        "devices_pick_guide": "📖 Nedan finns guider för olika system — välj din och följ stegen.",
        "devices_none": "Du har inga anslutna enheter ännu.",
        "devices_list_intro": "👇 Dina anslutna enheter:",
        "devices_select_prompt": "Välj en enhet från listan.",
        "device_default_name": "Enhet {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide för Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide för iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide för Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Guide för macOS</a>",
        "subscription_intro": (
            "💎 Abonnemang\n"
            "✨ Det här får du:\n"
            "• Snabb och säker åtkomst till dina tjänster\n"
            "• Inga annonser eller störningar\n"
            "• Bästa priset — endast 99₽ per månad! 🔥\n\n"
            "👉 Välj ett paket för 2 eller 5 enheter på en gång."
        ),
        "subscription_duration_prompt": "⏱️ Välj abonnemangets längd:\n{options}",
        "subscription_duration_hint": "💡 Längre period ger lägre månadspris.",
        "subscription_payment_thanks": (
            "🫶 Tack för förtroendet!\n\n"
            "Du är ett steg från ett säkert, stabilt och snabbt internet.\n"
            "Vi har gjort processen så smidig som möjligt.\n\n"
            "👇 Välj betalningsmetod:"
        ),
        "subscription_payment_change": "🔁 Vill du byta paket? Använd knapparna nedan innan du betalar.",
        "subscription_invalid_plan": "Välj ett av de tillgängliga paketen.",
        "subscription_invalid_duration": "Välj en av de föreslagna perioderna.",
        "subscription_payment_created": "Betalning skapad (test)",
        "plan_devices_2_button": "💫 Enheter: 2 - 99₽/månad",
        "plan_devices_5_button": "✨ Enheter: 5 - 169₽/månad",
        "plan_devices_2_title": "2 enheter",
        "plan_devices_5_title": "5 enheter",
        "plan_devices_2_duration_1m": "1 månad - 99₽",
        "plan_devices_2_duration_3m": "🔹3 månader - 249₽",
        "plan_devices_2_duration_6m": "🔸6 månader - 399₽",
        "plan_devices_5_duration_1m": "1 månad - 169₽",
        "plan_devices_5_duration_3m": "🔹3 månader - 449₽",
        "plan_devices_5_duration_6m": "🔸6 månader - 749₽",
        "faq_title": "❓ Frågor",
        "faq_body": (
            "❓ Hur, vad och varför?\n"
            "Vi har samlat de vanligaste frågorna i en artikel.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Ditt support-ID: {tg_id}\n\n"
            "🗺 Behöver du hjälp? Kontakta @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Bjud in vänner — få bonusdagar.\n\n"
            "Varje vän som ansluter via din länk ger +7 dagar på ditt abonnemang.\n\n"
            "Dela länken och surfa längre gratis."
        ),
        "referral_reward_notification": "🎉 Din vän gick med!\nDu fick +7 dagar på abonnemanget ✨",
        "plan_title_trial": "Provtid",
        "plan_title_device2": "2 enheter",
        "plan_title_device5": "5 enheter",
    },
    "tr": {
        "start_pitch": "🚀 Telegram’da hızlı ve kolay erişim.\nNerede olursan ol gizliliğini ve stabiliteyi koru.",
        "start_trial_granted": "🎁 Bonusun: 7 gün ücretsiz!\nSınırsız hızlı ve güvenli erişimin tadını çıkar.",
        "status_header": (
            "👋 Cihazların ve abonelik durumun\n\n"
            "Buradan hangi cihazların bağlı olduğunu ve hangi planı kullandığını görebilirsin."
        ),
        "status_plan_line": "📦 Planın: {plan_title}",
        "status_devices_counter": "(Cihazlar: {connected} / {limit})",
        "status_connections_header": "📟 Bağlantılar:",
        "status_connections_empty": "Henüz bağlı cihaz yok",
        "status_active_line": "🕒 Abonelik aktif: {duration}",
        "status_bonus_line": "🎁 Bonus: Her davet edilen arkadaş için +7 gün",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 saniye",
        "time_day_forms": "gün|gün|gün",
        "time_hour_forms": "saat|saat|saat",
        "time_minute_forms": "dakika|dakika|dakika",
        "time_second_forms": "saniye|saniye|saniye",
        "btn_intro_continue": "🚀 Hadi başlayalım!",
        "btn_devices": "📱 Cihazlar",
        "btn_subscription": "💎 Abonelik",
        "btn_invite_friend": "🤝 Arkadaş davet et",
        "btn_questions": "❓ Sorular",
        "btn_main_menu": "🏠 Ana menü",
        "btn_back": "⬅️ Geri",
        "btn_phone": "📱 Telefon",
        "btn_computer": "💻 Bilgisayar",
        "btn_my_devices": "🔌 Cihazlarım",
        "btn_android": "🔴 Android rehberi",
        "btn_ios": "🟢 iPhone rehberi",
        "btn_windows_instructions": "🔴 Windows rehberi",
        "btn_macos_instructions": "🟢 macOS rehberi",
        "btn_share_link": "Bağlantıyı paylaş",
        "btn_pay_card": "💳 Banka kartı",
        "devices_choose": (
            "📲 Bağlamak istediğin cihazı seç.\n"
            "(Sadece birkaç dakika sürer — çok kolay!)"
        ),
        "devices_generation_in_progress": "⏳ Yapılandırma hazırlanıyor. Dosya veya QR kodu bekleyin.",
        "devices_limit_reached": "⚠️ Bu plan için cihaz sınırına ulaşıldı",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Bağlantı neredeyse hazır!\n\n"
            "Senin için en uygun yöntemi seç:\n"
            "1. Profil dosyasını indirip AmneziaWG / WireGuard’a aktar\n"
            "2. QR kodunu uygulama içinde tara\n\n"
            "📚 Doğru rehberi seç ve birkaç adımda bağlan.\n\n"
            "⚠️ Her profil yalnızca tek bir cihazda kullanılabilir!"
        ),
        "devices_pick_guide": "📖 Aşağıda farklı sistemler için rehberler var — kendi sistemini seç ve adımları izle.",
        "devices_none": "Henüz bağlı cihazın yok.",
        "devices_list_intro": "👇 Bağlı cihazların:",
        "devices_select_prompt": "Listeden bir cihaz seç.",
        "device_default_name": "Cihaz {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Android rehberi</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 iPhone rehberi</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Windows rehberi</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 macOS rehberi</a>",
        "subscription_intro": (
            "💎 Abonelik\n"
            "✨ Abonelikle neler kazanırsın:\n"
            "• Servislerine hızlı ve güvenli erişim\n"
            "• Reklam ve dikkat dağıtıcı yok\n"
            "• En iyi fiyat — ayda sadece 99₽! 🔥\n\n"
            "👉 Aynı anda 2 veya 5 cihazlık plan seç."
        ),
        "subscription_duration_prompt": "⏱️ Abonelik süresini seç:\n{options}",
        "subscription_duration_hint": "💡 Süre uzadıkça aylık fiyat düşer.",
        "subscription_payment_thanks": (
            "🫶 Güvenin için teşekkürler!\n\n"
            "Güvenli, stabil ve hızlı internete bir adım kaldı.\n"
            "Süreci olabildiğince pratik hale getirdik.\n\n"
            "👇 Ödeme yöntemini seç:"
        ),
        "subscription_payment_change": "🔁 Planı değiştirmek mi istiyorsun? Ödeme öncesinde aşağıdaki butonları kullan.",
        "subscription_invalid_plan": "Lütfen mevcut planlardan birini seç.",
        "subscription_invalid_duration": "Lütfen sunulan sürelerden birini seç.",
        "subscription_payment_created": "Ödeme oluşturuldu (test)",
        "plan_devices_2_button": "💫 Cihaz: 2 - 99₽/ay",
        "plan_devices_5_button": "✨ Cihaz: 5 - 169₽/ay",
        "plan_devices_2_title": "2 cihaz",
        "plan_devices_5_title": "5 cihaz",
        "plan_devices_2_duration_1m": "1 ay - 99₽",
        "plan_devices_2_duration_3m": "🔹3 ay - 249₽",
        "plan_devices_2_duration_6m": "🔸6 ay - 399₽",
        "plan_devices_5_duration_1m": "1 ay - 169₽",
        "plan_devices_5_duration_3m": "🔹3 ay - 449₽",
        "plan_devices_5_duration_6m": "🔸6 ay - 749₽",
        "faq_title": "❓ Sorular",
        "faq_body": (
            "❓ Nasıl, ne ve neden?\n"
            "En sık sorulan soruları tek bir yazıda topladık.\n"
            "📖 SSS: {faq_url}\n\n"
            "Destek ID’n: {tg_id}\n\n"
            "🗺 Yardım mı lazım? @{support_handle} hesabına yaz."
        ),
        "referral_intro": (
            "🤝 Arkadaşlarını davet et — bonus günler kazan.\n\n"
            "Linkinden katılan her arkadaş aboneliğine +7 gün ekler.\n\n"
            "Linki paylaş ve daha uzun süre ücretsiz kullan."
        ),
        "referral_reward_notification": "🎉 Arkadaşın katıldı!\nAboneliğine +7 gün eklendi ✨",
        "plan_title_trial": "Deneme süresi",
        "plan_title_device2": "2 cihaz",
        "plan_title_device5": "5 cihaz",
    },
    "uk": {
        "start_pitch": "🚀 Швидкий і зручний доступ просто в Telegram.\nЗберігай приватність і стабільність будь-де.",
        "start_trial_granted": "🎁 Твій бонус: 7 днів безкоштовно!\nСпробуй швидкий та безпечний доступ без обмежень.",
        "status_header": (
            "👋 Твої пристрої та статус підписки\n\n"
            "Тут можна побачити, які пристрої підключені та який план активний."
        ),
        "status_plan_line": "📦 Твій план: {plan_title}",
        "status_devices_counter": "(Пристрої: {connected} / {limit})",
        "status_connections_header": "📟 Підключення:",
        "status_connections_empty": "Поки що немає підключень",
        "status_active_line": "🕒 Підписка активна: {duration}",
        "status_bonus_line": "🎁 Бонус: +7 днів за кожного запрошеного друга",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 секунд",
        "time_day_forms": "день|дні|днів",
        "time_hour_forms": "година|години|годин",
        "time_minute_forms": "хвилина|хвилини|хвилин",
        "time_second_forms": "секунда|секунди|секунд",
        "btn_intro_continue": "🚀 Поїхали!",
        "btn_devices": "📱 Пристрої",
        "btn_subscription": "💎 Підписка",
        "btn_invite_friend": "🤝 Запросити друга",
        "btn_questions": "❓ Питання",
        "btn_main_menu": "🏠 Головне меню",
        "btn_back": "⬅️ Назад",
        "btn_phone": "📱 Телефон",
        "btn_computer": "💻 Комп’ютер",
        "btn_my_devices": "🔌 Мої пристрої",
        "btn_android": "🔴 Інструкція для Android",
        "btn_ios": "🟢 Інструкція для iPhone",
        "btn_windows_instructions": "🔴 Інструкція для Windows",
        "btn_macos_instructions": "🟢 Інструкція для macOS",
        "btn_share_link": "Поділитися посиланням",
        "btn_pay_card": "💳 Банківська карта",
        "devices_choose": (
            "📲 Обери пристрій, який хочеш підключити.\n"
            "(Це займе лише кілька хвилин — дуже просто!)"
        ),
        "devices_generation_in_progress": "⏳ Конфігурацію вже створюємо. Зачекай файл або QR-код.",
        "devices_limit_reached": "⚠️ Досягнуто ліміт пристроїв у цьому плані",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Підключення майже готове!\n\n"
            "Обери зручний спосіб:\n"
            "1. Завантаж файл профілю та імпортуй в AmneziaWG / WireGuard\n"
            "2. Відскануй QR-код прямо в застосунку\n\n"
            "📚 Обери відповідну інструкцію та підключись у кілька кроків.\n\n"
            "⚠️ Один профіль можна використовувати лише на одному пристрої!"
        ),
        "devices_pick_guide": "📖 Нижче інструкції для різних систем — обери свою й дотримуйся кроків.",
        "devices_none": "У тебе ще немає підключених пристроїв.",
        "devices_list_intro": "👇 Список підключених пристроїв:",
        "devices_select_prompt": "Будь ласка, обери пристрій зі списку.",
        "device_default_name": "Пристрій {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Інструкція для Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Інструкція для iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Інструкція для Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Інструкція для macOS</a>",
        "subscription_intro": (
            "💎 Підписка\n"
            "✨ Що дає підписка:\n"
            "• Швидкий і безпечний доступ до сервісів\n"
            "• Жодної реклами та зайвих відволікань\n"
            "• Найкраща ціна — лише 99₽ на місяць! 🔥\n\n"
            "👉 Обирай план на 2 чи 5 пристроїв одразу."
        ),
        "subscription_duration_prompt": "⏱️ Обери тривалість підписки:\n{options}",
        "subscription_duration_hint": "💡 Чим довший період, тим нижча ціна за місяць.",
        "subscription_payment_thanks": (
            "🫶 Дякуємо за довіру!\n\n"
            "Ти за крок до безпечного, стабільного й швидкого інтернету.\n"
            "Ми зробили процес максимально зручним.\n\n"
            "👇 Обери спосіб оплати:"
        ),
        "subscription_payment_change": "🔁 Хочеш змінити план? Скористайся кнопками нижче до оплати.",
        "subscription_invalid_plan": "Обери один із доступних планів.",
        "subscription_invalid_duration": "Будь ласка, обери одну з запропонованих тривалостей.",
        "subscription_payment_created": "Платіж створено (тест)",
        "plan_devices_2_button": "💫 Пристрої: 2 - 99₽/міс",
        "plan_devices_5_button": "✨ Пристрої: 5 - 169₽/міс",
        "plan_devices_2_title": "2 пристрої",
        "plan_devices_5_title": "5 пристроїв",
        "plan_devices_2_duration_1m": "1 місяць - 99₽",
        "plan_devices_2_duration_3m": "🔹3 місяці - 249₽",
        "plan_devices_2_duration_6m": "🔸6 місяців - 399₽",
        "plan_devices_5_duration_1m": "1 місяць - 169₽",
        "plan_devices_5_duration_3m": "🔹3 місяці - 449₽",
        "plan_devices_5_duration_6m": "🔸6 місяців - 749₽",
        "faq_title": "❓ Питання",
        "faq_body": (
            "❓ Як, що і чому?\n"
            "Ми зібрали найпопулярніші питання в одній статті.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Твій ID підтримки: {tg_id}\n\n"
            "🗺 Потрібна допомога? Напиши @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Запрошуй друзів — отримуй бонусні дні.\n\n"
            "Кожен, хто підключиться за твоїм посиланням, додає +7 днів до підписки.\n\n"
            "Поділися посиланням і користуйся довше безкоштовно."
        ),
        "referral_reward_notification": "🎉 Твій друг приєднався!\nДодано +7 днів до підписки ✨",
        "plan_title_trial": "Пробний період",
        "plan_title_device2": "2 пристрої",
        "plan_title_device5": "5 пристроїв",
    },
    "uz": {
        "start_pitch": "🚀 Telegram’da tez va oson ulanish.\nQaerda bo‘lsang ham maxfiylik va barqarorlikni saqla.",
        "start_trial_granted": "🎁 Bonusingiz: 7 kun bepul!\nCheklovsiz tez va xavfsiz ulanishdan bahramand bo‘ling.",
        "status_header": (
            "👋 Qurilmalar va obuna holati\n\n"
            "Bu yerda qaysi qurilmalar ulanganini va qaysi tarif faol ekanini ko‘rishingiz mumkin."
        ),
        "status_plan_line": "📦 Tarifingiz: {plan_title}",
        "status_devices_counter": "(Qurilmalar: {connected} / {limit})",
        "status_connections_header": "📟 Ulanishlar:",
        "status_connections_empty": "Hozircha ulangan qurilmalar yo‘q",
        "status_active_line": "🕒 Obuna faol: {duration}",
        "status_bonus_line": "🎁 Bonus: har taklif qilingan do‘st uchun +7 kun",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 soniya",
        "time_day_forms": "kun|kun|kun",
        "time_hour_forms": "soat|soat|soat",
        "time_minute_forms": "daqiqa|daqiqa|daqiqa",
        "time_second_forms": "soniya|soniya|soniya",
        "btn_intro_continue": "🚀 Boshladik!",
        "btn_devices": "📱 Qurilmalar",
        "btn_subscription": "💎 Obuna",
        "btn_invite_friend": "🤝 Do‘st chaqirish",
        "btn_questions": "❓ Savollar",
        "btn_main_menu": "🏠 Asosiy menyu",
        "btn_back": "⬅️ Orqaga",
        "btn_phone": "📱 Telefon",
        "btn_computer": "💻 Kompyuter",
        "btn_my_devices": "🔌 Qurilmalarim",
        "btn_android": "🔴 Android qo‘llanmasi",
        "btn_ios": "🟢 iPhone qo‘llanmasi",
        "btn_windows_instructions": "🔴 Windows qo‘llanmasi",
        "btn_macos_instructions": "🟢 macOS qo‘llanmasi",
        "btn_share_link": "Havolani ulashish",
        "btn_pay_card": "💳 Bank kartasi",
        "devices_choose": (
            "📲 Ulamoqchi bo‘lgan qurilmangizni tanlang.\n"
            "(Faqat bir necha daqiqa ketadi — juda oson!)"
        ),
        "devices_generation_in_progress": "⏳ Konfiguratsiya tayyorlanmoqda. Fayl yoki QR kodni kuting.",
        "devices_limit_reached": "⚠️ Bu tarif uchun qurilma limiti tugadi",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Ulanish deyarli tayyor!\n\n"
            "O‘zingizga qulay usulni tanlang:\n"
            "1. Profil faylini yuklab olib AmneziaWG / WireGuard dasturiga import qiling\n"
            "2. QR kodni ilova ichida skanerdan o‘tkazing\n\n"
            "📚 Mos qo‘llanmadan foydalanib, bir necha qadamda ulaning.\n\n"
            "⚠️ Har bir profil faqat bitta qurilmada ishlatiladi!"
        ),
        "devices_pick_guide": "📖 Quyida turli tizimlar uchun qo‘llanmalar bor — o‘zingiznikini tanlab, qadamlarga amal qiling.",
        "devices_none": "Sizda hali ulangan qurilmalar yo‘q.",
        "devices_list_intro": "👇 Ulangan qurilmalar ro‘yxati:",
        "devices_select_prompt": "Iltimos, ro‘yxatdan qurilmani tanlang.",
        "device_default_name": "Qurilma {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Android qo‘llanmasi</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 iPhone qo‘llanmasi</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Windows qo‘llanmasi</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 macOS qo‘llanmasi</a>",
        "subscription_intro": (
            "💎 Obuna\n"
            "✨ Obuna nimalarni beradi:\n"
            "• Servislaringizga tez va xavfsiz kirish\n"
            "• Reklamalar va chalg‘ituvchilar yo‘q\n"
            "• Eng yaxshi narx — oyiga atigi 99₽! 🔥\n\n"
            "👉 Bir vaqtning o‘zida 2 yoki 5 qurilma uchun rejani tanlang."
        ),
        "subscription_duration_prompt": "⏱️ Obuna muddatini tanlang:\n{options}",
        "subscription_duration_hint": "💡 Muddat uzoq bo‘lsa, oylik narx pastroq bo‘ladi.",
        "subscription_payment_thanks": (
            "🫶 Ishonchingiz uchun rahmat!\n\n"
            "Xavfsiz, barqaror va tez internetga bir qadam qoldi.\n"
            "Jarayonni iloji boricha qulay qildik.\n\n"
            "👇 To‘lov usulini tanlang:"
        ),
        "subscription_payment_change": "🔁 Tarifni o‘zgartirmoqchimisiz? To‘lovdan oldin pastdagi tugmalarni bosing.",
        "subscription_invalid_plan": "Iltimos, mavjud rejadan birini tanlang.",
        "subscription_invalid_duration": "Iltimos, taklif qilingan muddatlardan birini tanlang.",
        "subscription_payment_created": "To‘lov yaratildi (test)",
        "plan_devices_2_button": "💫 Qurilmalar: 2 - 99₽/oy",
        "plan_devices_5_button": "✨ Qurilmalar: 5 - 169₽/oy",
        "plan_devices_2_title": "2 qurilma",
        "plan_devices_5_title": "5 qurilma",
        "plan_devices_2_duration_1m": "1 oy - 99₽",
        "plan_devices_2_duration_3m": "🔹3 oy - 249₽",
        "plan_devices_2_duration_6m": "🔸6 oy - 399₽",
        "plan_devices_5_duration_1m": "1 oy - 169₽",
        "plan_devices_5_duration_3m": "🔹3 oy - 449₽",
        "plan_devices_5_duration_6m": "🔸6 oy - 749₽",
        "faq_title": "❓ Savollar",
        "faq_body": (
            "❓ Qanday, nima va nega?\n"
            "Eng ko‘p beriladigan savollarni bitta maqolada jamladik.\n"
            "📖 FAQ: {faq_url}\n\n"
            "Yordam ID’ingiz: {tg_id}\n\n"
            "🗺 Yordam kerakmi? @{support_handle} ga yozing"
        ),
        "referral_intro": (
            "🤝 Do‘stlarni taklif qiling — bonus kunlar oling.\n\n"
            "Havolangiz orqali ulanadigan har bir do‘st obunangizga +7 kun qo‘shadi.\n\n"
            "Havolani ulashing va uzoqroq bepul foydalaning."
        ),
        "referral_reward_notification": "🎉 Do‘stingiz qo‘shildi!\nObunangizga +7 kun qo‘shildi ✨",
        "plan_title_trial": "Sinov davri",
        "plan_title_device2": "2 qurilma",
        "plan_title_device5": "5 qurilma",
    },
    "vi": {
        "start_pitch": "🚀 Truy cập nhanh và dễ dàng ngay trong Telegram.\nGiữ sự riêng tư và ổn định ở bất cứ đâu.",
        "start_trial_granted": "🎁 Ưu đãi của bạn: 7 ngày miễn phí!\nTrải nghiệm kết nối nhanh và an toàn không giới hạn.",
        "status_header": (
            "👋 Thiết bị của bạn và trạng thái gói cước\n\n"
            "Tại đây bạn có thể xem thiết bị nào đang kết nối và gói nào đang hoạt động."
        ),
        "status_plan_line": "📦 Gói hiện tại: {plan_title}",
        "status_devices_counter": "(Thiết bị: {connected} / {limit})",
        "status_connections_header": "📟 Kết nối:",
        "status_connections_empty": "Chưa có thiết bị nào được kết nối",
        "status_active_line": "🕒 Gói còn hiệu lực: {duration}",
        "status_bonus_line": "🎁 Thưởng: +7 ngày cho mỗi người bạn mời",
        "status_connections_prefix": "- {device_name}",
        "time_zero": "0 giây",
        "time_day_forms": "ngày|ngày|ngày",
        "time_hour_forms": "giờ|giờ|giờ",
        "time_minute_forms": "phút|phút|phút",
        "time_second_forms": "giây|giây|giây",
        "btn_intro_continue": "🚀 Bắt đầu thôi!",
        "btn_devices": "📱 Thiết bị",
        "btn_subscription": "💎 Gói cước",
        "btn_invite_friend": "🤝 Mời bạn bè",
        "btn_questions": "❓ Câu hỏi",
        "btn_main_menu": "🏠 Menu chính",
        "btn_back": "⬅️ Quay lại",
        "btn_phone": "📱 Điện thoại",
        "btn_computer": "💻 Máy tính",
        "btn_my_devices": "🔌 Thiết bị của tôi",
        "btn_android": "🔴 Hướng dẫn Android",
        "btn_ios": "🟢 Hướng dẫn iPhone",
        "btn_windows_instructions": "🔴 Hướng dẫn Windows",
        "btn_macos_instructions": "🟢 Hướng dẫn macOS",
        "btn_share_link": "Chia sẻ liên kết",
        "btn_pay_card": "💳 Thẻ ngân hàng",
        "devices_choose": (
            "📲 Chọn thiết bị bạn muốn kết nối.\n"
            "(Chỉ mất vài phút — vô cùng đơn giản!)"
        ),
        "devices_generation_in_progress": "⏳ Tập tin cấu hình đang được tạo. Hãy chờ tệp hoặc mã QR.",
        "devices_limit_reached": "⚠️ Bạn đã đạt giới hạn thiết bị của gói này",
        "device_ready_title": "",
        "device_ready_body": (
            "🧩 Kết nối gần như hoàn tất!\n\n"
            "Chọn cách bạn muốn kết nối:\n"
            "1. Tải tệp cấu hình và nhập vào AmneziaWG / WireGuard\n"
            "2. Quét mã QR trực tiếp trong ứng dụng\n\n"
            "📚 Chọn hướng dẫn phù hợp và làm theo vài bước là xong.\n\n"
            "⚠️ Mỗi cấu hình chỉ dùng cho một thiết bị!"
        ),
        "devices_pick_guide": "📖 Bên dưới là hướng dẫn cho từng hệ thống — chọn hệ của bạn và làm theo.",
        "devices_none": "Bạn chưa có thiết bị nào được kết nối.",
        "devices_list_intro": "👇 Thiết bị đã kết nối:",
        "devices_select_prompt": "Vui lòng chọn một thiết bị trong danh sách.",
        "device_default_name": "Thiết bị {index}",
        "instruction_link_android": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Hướng dẫn Android</a>",
        "instruction_link_ios": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Hướng dẫn iPhone</a>",
        "instruction_link_windows": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Hướng dẫn Windows</a>",
        "instruction_link_macos": "<a href=\"https://telegra.ph/Android-Instr-06-25\">📚 Hướng dẫn macOS</a>",
        "subscription_intro": (
            "💎 Gói cước\n"
            "✨ Bạn nhận được:\n"
            "• Truy cập nhanh và an toàn tới các dịch vụ của bạn\n"
            "• Không quảng cáo, không phiền toái\n"
            "• Giá tốt nhất — chỉ 99₽/tháng! 🔥\n\n"
            "👉 Chọn gói cho 2 hoặc 5 thiết bị cùng lúc."
        ),
        "subscription_duration_prompt": "⏱️ Chọn thời hạn gói:\n{options}",
        "subscription_duration_hint": "💡 Thời hạn càng dài thì giá mỗi tháng càng thấp.",
        "subscription_payment_thanks": (
            "🫶 Cảm ơn vì đã tin tưởng!\n\n"
            "Bạn chỉ còn một bước để có internet an toàn, ổn định và nhanh chóng.\n"
            "Chúng tôi đã tối ưu quy trình để bạn thuận tiện nhất.\n\n"
            "👇 Chọn phương thức thanh toán:"
        ),
        "subscription_payment_change": "🔁 Muốn đổi gói? Hãy dùng các nút bên dưới trước khi thanh toán.",
        "subscription_invalid_plan": "Hãy chọn một trong các gói khả dụng.",
        "subscription_invalid_duration": "Vui lòng chọn một thời hạn được gợi ý.",
        "subscription_payment_created": "Thanh toán đã tạo (thử nghiệm)",
        "plan_devices_2_button": "💫 Thiết bị: 2 - 99₽/tháng",
        "plan_devices_5_button": "✨ Thiết bị: 5 - 169₽/tháng",
        "plan_devices_2_title": "2 thiết bị",
        "plan_devices_5_title": "5 thiết bị",
        "plan_devices_2_duration_1m": "1 tháng - 99₽",
        "plan_devices_2_duration_3m": "🔹3 tháng - 249₽",
        "plan_devices_2_duration_6m": "🔸6 tháng - 399₽",
        "plan_devices_5_duration_1m": "1 tháng - 169₽",
        "plan_devices_5_duration_3m": "🔹3 tháng - 449₽",
        "plan_devices_5_duration_6m": "🔸6 tháng - 749₽",
        "faq_title": "❓ Câu hỏi",
        "faq_body": (
            "❓ Làm thế nào, gì và vì sao?\n"
            "Chúng tôi tổng hợp các câu hỏi phổ biến nhất trong một bài viết.\n"
            "📖 FAQ: {faq_url}\n\n"
            "ID hỗ trợ của bạn: {tg_id}\n\n"
            "🗺 Cần trợ giúp? Liên hệ @{support_handle}"
        ),
        "referral_intro": (
            "🤝 Mời bạn bè — nhận thêm ngày sử dụng.\n\n"
            "Mỗi người bạn tham gia qua liên kết của bạn sẽ cộng +7 ngày vào gói.\n\n"
            "Chia sẻ liên kết và dùng lâu hơn miễn phí."
        ),
        "referral_reward_notification": "🎉 Bạn của bạn đã tham gia!\nBạn nhận được +7 ngày sử dụng ✨",
        "plan_title_trial": "Thời gian dùng thử",
        "plan_title_device2": "2 thiết bị",
        "plan_title_device5": "5 thiết bị",
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
