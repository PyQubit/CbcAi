"""
سیستم چندزبانه CbcAi — فارسی و انگلیسی
متن‌ها کوتاه، روان و یکدست
"""

from typing import Any

# ==============================
# دکمه‌های منو
# ==============================

BTN_CHAT_FA = "🩺 مشاوره پزشکی هوشمند"
BTN_LAB_FA = "🔬 تحلیل آزمایش"
BTN_DOCTORS_FA = "👨‍⚕️ معرفی پزشک"
BTN_PREMIUM_FA = "💎 اشتراک ویژه"
BTN_SETTINGS_FA = "⚙️ تنظیمات حساب"
BTN_BACK_FA = "⬅️ بازگشت به منوی اصلی"
BTN_LANG_FA = "🌐 انتخاب زبان"
BTN_LANG_PERSIAN = "🇮🇷 فارسی"
BTN_LANG_ENGLISH = "🇬🇧 English"

BTN_CHAT_EN = "🩺 Smart Medical Consultation"
BTN_LAB_EN = "🔬 Lab Analysis"
BTN_DOCTORS_EN = "👨‍⚕️ Find a Doctor"
BTN_PREMIUM_EN = "💎 Premium Subscription"
BTN_SETTINGS_EN = "⚙️ Account Settings"
BTN_BACK_EN = "⬅️ Back to Main Menu"
BTN_LANG_EN = "🌐 Language"

ALL_MAIN_BUTTONS = {
    BTN_CHAT_FA, BTN_LAB_FA, BTN_DOCTORS_FA, BTN_PREMIUM_FA, BTN_SETTINGS_FA,
    BTN_CHAT_EN, BTN_LAB_EN, BTN_DOCTORS_EN, BTN_PREMIUM_EN, BTN_SETTINGS_EN,
}

ALL_BACK_BUTTONS = {BTN_BACK_FA, BTN_BACK_EN}
ALL_LANG_BUTTONS = {BTN_LANG_FA, BTN_LANG_EN, BTN_LANG_PERSIAN, BTN_LANG_ENGLISH}

BUTTON_ACTIONS = {
    BTN_CHAT_FA: "chat", BTN_CHAT_EN: "chat",
    BTN_LAB_FA: "lab", BTN_LAB_EN: "lab",
    BTN_DOCTORS_FA: "doctors", BTN_DOCTORS_EN: "doctors",
    BTN_PREMIUM_FA: "premium", BTN_PREMIUM_EN: "premium",
    BTN_SETTINGS_FA: "settings", BTN_SETTINGS_EN: "settings",
    BTN_BACK_FA: "back", BTN_BACK_EN: "back",
    BTN_LANG_FA: "language", BTN_LANG_EN: "language",
    BTN_LANG_PERSIAN: "set_fa", BTN_LANG_ENGLISH: "set_en",
}


def get_btn(key: str, lang: str = "fa") -> str:
    mapping = {
        "chat": (BTN_CHAT_FA, BTN_CHAT_EN),
        "lab": (BTN_LAB_FA, BTN_LAB_EN),
        "doctors": (BTN_DOCTORS_FA, BTN_DOCTORS_EN),
        "premium": (BTN_PREMIUM_FA, BTN_PREMIUM_EN),
        "settings": (BTN_SETTINGS_FA, BTN_SETTINGS_EN),
        "back": (BTN_BACK_FA, BTN_BACK_EN),
        "language": (BTN_LANG_FA, BTN_LANG_EN),
    }
    fa, en = mapping.get(key, ("", ""))
    return en if lang == "en" else fa


# ==============================
# متن‌های رابط کاربری
# ==============================

TEXTS: dict[str, dict[str, str]] = {
    "welcome_caption": {
        "fa": """🩺 <b>به CbcAi خوش آمدید</b>

سلام 👋
CbcAi دستیار هوشمند سلامت شماست؛ اطلاعات پزشکی را ساده و قابل‌فهم در اختیارتان می‌گذارد.

━━━━━━━━━━━━━━━━━━

<b>امکانات</b>

🩺 مشاوره پزشکی هوشمند
🔬 تحلیل نتایج آزمایش
📚 آموزش سلامت

━━━━━━━━━━━━━━━━━━

🎁 <b>پلن رایگان:</b> ۱۰ پیام در هر ۲۴ ساعت

⚠️ CbcAi جایگزین پزشک نیست. در شرایط اورژانسی فوراً به مرکز درمانی مراجعه کنید.

💙 تیم CbcAi""",
        "en": """🩺 <b>Welcome to CbcAi</b>

Hello 👋
CbcAi is your smart health assistant — medical information, explained simply.

━━━━━━━━━━━━━━━━━━

<b>Features</b>

🩺 Smart medical consultation
🔬 Lab results analysis
📚 Health education

━━━━━━━━━━━━━━━━━━

🎁 <b>Free plan:</b> 10 messages every 24 hours

⚠️ CbcAi is not a substitute for a doctor. In an emergency, seek medical care right away.

💙 CbcAi Team""",
    },
    "back_to_menu": {
        "fa": """🏠 <b>منوی اصلی</b>

یکی از گزینه‌های زیر را انتخاب کنید.""",
        "en": """🏠 <b>Main Menu</b>

Choose one of the options below.""",
    },
    "settings": {
        "fa": """⚙️ <b>تنظیمات حساب</b>

👤 نام: <b>{name}</b>
🆔 شناسه: <code>{telegram_id}</code>
🌐 زبان: <b>{lang_label}</b>

━━━━━━━━━━━━━━━━━━

📊 <b>امروز</b>
💬 استفاده‌شده: <b>{used}</b> از <b>{limit}</b>
📩 باقی‌مانده: <b>{remaining}</b>

برای تغییر زبان، دکمه 🌐 را بزنید.""",
        "en": """⚙️ <b>Account Settings</b>

👤 Name: <b>{name}</b>
🆔 ID: <code>{telegram_id}</code>
🌐 Language: <b>{lang_label}</b>

━━━━━━━━━━━━━━━━━━

📊 <b>Today</b>
💬 Used: <b>{used}</b> of <b>{limit}</b>
📩 Remaining: <b>{remaining}</b>

Tap 🌐 to change language.""",
    },
    "choose_language": {
        "fa": """🌐 <b>انتخاب زبان</b>

زبان مورد نظر را انتخاب کنید:

🇮🇷 فارسی
🇬🇧 English

این انتخاب روی منوها و پاسخ‌های هوش مصنوعی اعمال می‌شود.""",
        "en": """🌐 <b>Language</b>

Choose your preferred language:

🇮🇷 فارسی
🇬🇧 English

This applies to menus and AI responses.""",
    },
    "first_language_ask": {
        "fa": """🌐 <b>به CbcAi خوش آمدید</b>

لطفاً زبان خود را انتخاب کنید:

🇮🇷 فارسی
🇬🇧 English""",
        "en": """🌐 <b>Welcome to CbcAi</b>

Please choose your language:

🇮🇷 فارسی
🇬🇧 English""",
    },
    "language_changed": {
        "fa": """✅ زبان به <b>فارسی 🇮🇷</b> تغییر کرد.

منوها و پاسخ‌های مدل از این پس به فارسی هستند.""",
        "en": """✅ Language set to <b>English 🇬🇧</b>.

Menus and AI responses will now be in English.""",
    },
    "enter_chat": {
        "fa": """🩺 <b>مشاوره پزشکی</b>

علائم یا سؤال پزشکی‌تان را بنویسید.

برای پاسخ دقیق‌تر این موارد را ذکر کنید:
• سن و جنسیت
• علائم و مدت آن‌ها
• شدت مشکل
• دارو یا بیماری زمینه‌ای (در صورت وجود)

⚠️ جایگزین پزشک نیست. در اورژانس به مرکز درمانی مراجعه کنید.""",
        "en": """🩺 <b>Medical Consultation</b>

Describe your symptoms or ask a medical question.

For a better answer, include:
• Age and gender
• Symptoms and how long
• Severity
• Medications or conditions (if any)

⚠️ Not a substitute for a doctor. In an emergency, seek care immediately.""",
    },
    "cooldown": {
        "fa": """⏳ لطفاً چند ثانیه صبر کنید و دوباره پیام بفرستید.""",
        "en": """⏳ Please wait a few seconds before sending another message.""",
    },
    "limit_reached": {
        "fa": """🚫 <b>سقف روزانه تمام شد</b>

امروز از هر <b>{limit} پیام رایگان</b> استفاده کرده‌اید.

🌅 فردا دوباره در دسترس است.
⭐ برای محدودیت کمتر، اشتراک ویژه را ببینید.""",
        "en": """🚫 <b>Daily limit reached</b>

You've used all <b>{limit} free messages</b> today.

🌅 Free access resets tomorrow.
⭐ For higher limits, check Premium.""",
    },
    "chat_error": {
        "fa": """⚠️ الان پاسخ آماده نشد. چند لحظه دیگر دوباره تلاش کنید.""",
        "en": """⚠️ Couldn't get a response right now. Please try again in a moment.""",
    },
    "fallback": {
        "fa": """🤖 لطفاً یکی از گزینه‌های منوی اصلی را انتخاب کنید.""",
        "en": """🤖 Please choose an option from the main menu.""",
    },
    "lab_coming_soon": {
        "fa": """🔬 <b>تحلیل آزمایش</b>

این بخش به‌زودی فعال می‌شود.

📷 ارسال تصویر برگه آزمایش
📄 توضیح ساده نتایج
📊 مقایسه با محدوده طبیعی

⚠️ صرفاً آموزشی است و جایگزین تفسیر پزشک نیست.""",
        "en": """🔬 <b>Lab Analysis</b>

Coming soon.

📷 Send a photo of your lab report
📄 Plain-language explanations
📊 Compare values with normal ranges

⚠️ For education only — not a doctor's interpretation.""",
    },
    "lab_not_ready": {
        "fa": """🚧 تحلیل آزمایش هنوز فعال نیست. به‌زودی در دسترس قرار می‌گیرد.""",
        "en": """🚧 Lab analysis isn't available yet. Coming soon.""",
    },
    "enter_doctors": {
        "fa": """👨‍⚕️ <b>راهنمای انتخاب تخصص</b>

علائم یا مشکل‌تان را بنویسید تا بگوییم بهتر است پیش <b>چه نوع متخصصی</b> بروید.

برای پیشنهاد دقیق‌تر این موارد را ذکر کنید:
• سن تقریبی
• علائم اصلی و محل مشکل
• مدت شروع و شدت

⚠️ نام هیچ پزشک یا مرکزی گفته نمی‌شود — فقط نوع تخصص.
این راهنما جایگزین ویزیت حضوری نیست.""",
        "en": """👨‍⚕️ <b>Specialty Guide</b>

Describe your symptoms or concern so we can suggest <b>which type of specialist</b> to see.

For a better suggestion, include:
• Approximate age
• Main symptoms and location
• Duration and severity

⚠️ No doctor or clinic names — specialty type only.
This is not a substitute for an in-person visit.""",
    },
    "doctors": {
        "fa": """👨‍⚕️ <b>راهنمای انتخاب تخصص</b>

برای شروع، علائم خود را ارسال کنید.""",
        "en": """👨‍⚕️ <b>Specialty Guide</b>

Send your symptoms to get started.""",
    },
    "premium": {
        "fa": """💎 <b>اشتراک ویژه</b>

به‌زودی با امکانات بیشتر:

♾️ پیام بیشتر یا نامحدود
⚡ اولویت در پاسخ
🔬 تحلیل پیشرفته‌تر آزمایش
📷 بررسی تصویر برگه آزمایش

🎁 پلن رایگان همچنان فعال است.""",
        "en": """💎 <b>Premium</b>

Coming soon with more access:

♾️ Higher or unlimited messages
⚡ Priority responses
🔬 Advanced lab analysis
📷 Lab report image review

🎁 The free plan stays available.""",
    },
    "help": {
        "fa": """📖 <b>راهنما</b>

از منوی اصلی یک بخش را انتخاب کنید.

🩺 <b>مشاوره پزشکی</b> — علائم یا سؤال خود را بفرستید. سن، جنسیت و مدت علائم را هم بنویسید.

👨‍⚕️ <b>راهنمای تخصص</b> — بگویید پیش چه متخصصی بروید.
🔬 <b>تحلیل آزمایش</b> — به‌زودی.

⚙️ <b>تنظیمات</b> — تغییر زبان و وضعیت حساب.

دستورها: /start /help /about /language""",
        "en": """📖 <b>Help</b>

Pick a section from the main menu.

🩺 <b>Medical consultation</b> — send symptoms or questions. Include age, gender, and duration when you can.

👨‍⚕️ <b>Specialty guide</b> — which type of specialist to see.
🔬 <b>Lab analysis</b> — coming soon.

⚙️ <b>Settings</b> — language and account status.

Commands: /start /help /about /language""",
    },
    "about": {
        "fa": """🧬 <b>درباره CbcAi</b>

دستیار هوشمند سلامت برای درک بهتر علائم، آزمایش‌ها و مفاهیم پزشکی به زبان ساده.

⚠️ پاسخ‌ها آموزشی‌اند و جایگزین معاینه یا تشخیص پزشک نیستند.
در اورژانس فوراً با اورژانس تماس بگیرید یا به مرکز درمانی بروید.

💙 تیم توسعه CbcAi""",
        "en": """🧬 <b>About CbcAi</b>

A smart health assistant that explains symptoms, lab results, and medical ideas in plain language.

⚠️ Answers are educational only — not a substitute for a doctor's exam or diagnosis.
In an emergency, call emergency services or go to the nearest clinic.

💙 CbcAi Development Team""",
    },
}


def t(key: str, lang: str = "fa", **kwargs: Any) -> str:
    entry = TEXTS.get(key, {})
    text = entry.get(lang) or entry.get("fa", key)
    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, ValueError):
            return text
    return text


def lang_label(lang: str) -> str:
    return "فارسی 🇮🇷" if lang == "fa" else "English 🇬🇧"
