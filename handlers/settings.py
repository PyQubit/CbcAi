from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, Message

from config import DAILY_CHAT_LIMIT
from i18n import (
    BTN_SETTINGS_FA,
    BTN_SETTINGS_EN,
    BTN_LANG_FA,
    BTN_LANG_EN,
    BTN_LANG_PERSIAN,
    BTN_LANG_ENGLISH,
    t,
    lang_label,
)
from keyboards import (
    settings_keyboard,
    language_keyboard,
    main_keyboard,
)
from states import UserState
from utils.limits import count_chat_messages_today
from utils.user import get_or_create_user, set_user_language

router = Router()


async def _send_welcome_after_lang(message: Message, lang: str) -> None:
    """پس از انتخاب زبان توسط کاربر جدید، پیام خوش‌آمدگویی ارسال شود"""
    photo = FSInputFile("welcome.jpg")
    await message.answer_photo(
        photo=photo,
        caption=t("welcome_caption", lang),
        reply_markup=main_keyboard(lang),
    )


@router.message(F.text.in_({BTN_SETTINGS_FA, BTN_SETTINGS_EN}))
async def settings_section(message: Message, state: FSMContext) -> None:
    await state.clear()

    user, _ = await get_or_create_user(message)
    lang = user.language or "fa"

    used = await count_chat_messages_today(user.id)
    remaining = max(0, DAILY_CHAT_LIMIT - used)

    await message.answer(
        t(
            "settings",
            lang,
            name=message.from_user.first_name or ("Not set" if lang == "en" else "ثبت نشده"),
            telegram_id=message.from_user.id,
            lang_label=lang_label(lang),
            used=used,
            limit=DAILY_CHAT_LIMIT,
            remaining=remaining,
        ),
        reply_markup=settings_keyboard(lang),
    )


@router.message(F.text.in_({BTN_LANG_FA, BTN_LANG_EN}))
async def choose_language(message: Message, state: FSMContext) -> None:
    user, _ = await get_or_create_user(message)
    lang = user.language or "fa"
    await message.answer(
        t("choose_language", lang),
        reply_markup=language_keyboard(with_back=True),
    )


@router.message(F.text == BTN_LANG_PERSIAN)
async def set_persian(message: Message, state: FSMContext) -> None:
    current = await state.get_state()
    is_onboarding = current == UserState.choose_language.state

    await state.clear()
    await set_user_language(message.from_user.id, "fa")

    if is_onboarding:
        # کاربر جدید: بعد از انتخاب زبان، خوش‌آمدگویی
        await _send_welcome_after_lang(message, "fa")
    else:
        await message.answer(
            t("language_changed", "fa"),
            reply_markup=main_keyboard("fa"),
        )


@router.message(F.text == BTN_LANG_ENGLISH)
async def set_english(message: Message, state: FSMContext) -> None:
    current = await state.get_state()
    is_onboarding = current == UserState.choose_language.state

    await state.clear()
    await set_user_language(message.from_user.id, "en")

    if is_onboarding:
        await _send_welcome_after_lang(message, "en")
    else:
        await message.answer(
            t("language_changed", "en"),
            reply_markup=main_keyboard("en"),
        )


@router.message(UserState.choose_language)
async def force_language_choice(message: Message, state: FSMContext) -> None:
    """اگر کاربر جدید هنوز زبان انتخاب نکرده، دوباره بپرس"""
    await message.answer(
        t("first_language_ask", "fa"),
        reply_markup=language_keyboard(with_back=False),
    )
