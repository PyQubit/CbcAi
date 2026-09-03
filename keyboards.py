from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from i18n import (
    BTN_CHAT_FA,
    BTN_LAB_FA,
    BTN_DOCTORS_FA,
    BTN_PREMIUM_FA,
    BTN_SETTINGS_FA,
    BTN_BACK_FA,
    BTN_CHAT_EN,
    BTN_LAB_EN,
    BTN_DOCTORS_EN,
    BTN_PREMIUM_EN,
    BTN_SETTINGS_EN,
    BTN_BACK_EN,
    BTN_LANG_FA,
    BTN_LANG_EN,
    BTN_LANG_PERSIAN,
    BTN_LANG_ENGLISH,
    ALL_MAIN_BUTTONS,
    ALL_BACK_BUTTONS,
    get_btn,
)

# سازگاری با کد قدیمی
BTN_CHAT = BTN_CHAT_FA
BTN_LAB = BTN_LAB_FA
BTN_DOCTORS = BTN_DOCTORS_FA
BTN_PREMIUM = BTN_PREMIUM_FA
BTN_SETTINGS = BTN_SETTINGS_FA
BTN_BACK = BTN_BACK_FA

MAIN_BUTTONS = ALL_MAIN_BUTTONS


def main_keyboard(lang: str = "fa") -> ReplyKeyboardMarkup:
    """منوی اصلی بر اساس زبان کاربر"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=get_btn("chat", lang)),
                KeyboardButton(text=get_btn("lab", lang)),
            ],
            [
                KeyboardButton(text=get_btn("doctors", lang)),
                KeyboardButton(text=get_btn("premium", lang)),
            ],
            [
                KeyboardButton(text=get_btn("settings", lang)),
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder=(
            "Select a section to start 🩺"
            if lang == "en"
            else "یک بخش را برای شروع انتخاب کنید 🩺"
        ),
    )


def back_keyboard(lang: str = "fa") -> ReplyKeyboardMarkup:
    """کیبورد بازگشت"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_btn("back", lang))],
        ],
        resize_keyboard=True,
        input_field_placeholder=(
            "Back to main menu" if lang == "en" else "بازگشت به منوی اصلی"
        ),
    )


def settings_keyboard(lang: str = "fa") -> ReplyKeyboardMarkup:
    """کیبورد تنظیمات شامل انتخاب زبان"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_btn("language", lang))],
            [KeyboardButton(text=get_btn("back", lang))],
        ],
        resize_keyboard=True,
    )


def language_keyboard(*, with_back: bool = True) -> ReplyKeyboardMarkup:
    """کیبورد انتخاب زبان — برای کاربر جدید without back"""
    rows = [
        [
            KeyboardButton(text=BTN_LANG_PERSIAN),
            KeyboardButton(text=BTN_LANG_ENGLISH),
        ],
    ]
    if with_back:
        rows.append([KeyboardButton(text=BTN_BACK_FA)])
        rows.append([KeyboardButton(text=BTN_BACK_EN)])
    return ReplyKeyboardMarkup(
        keyboard=rows,
        resize_keyboard=True,
        input_field_placeholder="🇮🇷 فارسی  |  🇬🇧 English",
    )
