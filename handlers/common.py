from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import BotCommand, FSInputFile, Message

from i18n import ALL_MAIN_BUTTONS, ALL_BACK_BUTTONS, t
from keyboards import main_keyboard, language_keyboard
from states import UserState
from utils.user import get_or_create_user

router = Router()


async def set_bot_commands(bot) -> None:
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Start / شروع و نمایش منوی اصلی"),
            BotCommand(command="help", description="Help / راهنمای استفاده"),
            BotCommand(command="about", description="About / درباره CbcAi"),
            BotCommand(command="language", description="Language / انتخاب زبان"),
        ]
    )


async def send_welcome(message: Message, lang: str) -> None:
    """ارسال پیام خوش‌آمدگویی با عکس"""
    photo = FSInputFile("welcome.jpg")
    await message.answer_photo(
        photo=photo,
        caption=t("welcome_caption", lang),
        reply_markup=main_keyboard(lang),
    )


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    user, is_new = await get_or_create_user(message)

    if is_new:
        # کاربر جدید → اول انتخاب زبان
        await state.set_state(UserState.choose_language)
        await message.answer(
            t("first_language_ask", "fa"),
            reply_markup=language_keyboard(with_back=False),
        )
        return

    # کاربر قدیمی → خوش‌آمدگویی مستقیم
    await state.clear()
    lang = user.language or "fa"
    await send_welcome(message, lang)


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    user, _ = await get_or_create_user(message)
    lang = user.language or "fa"
    await message.answer(t("help", lang), reply_markup=main_keyboard(lang))


@router.message(Command("about"))
async def cmd_about(message: Message) -> None:
    user, _ = await get_or_create_user(message)
    lang = user.language or "fa"
    await message.answer(t("about", lang), reply_markup=main_keyboard(lang))


@router.message(Command("language"))
async def cmd_language(message: Message, state: FSMContext) -> None:
    user, _ = await get_or_create_user(message)
    lang = user.language or "fa"
    await message.answer(
        t("choose_language", lang),
        reply_markup=language_keyboard(with_back=True),
    )


@router.message(F.text.in_(ALL_BACK_BUTTONS))
async def back_to_menu(message: Message, state: FSMContext) -> None:
    await state.clear()
    user, _ = await get_or_create_user(message)
    lang = user.language or "fa"

    await message.answer(
        t("back_to_menu", lang),
        reply_markup=main_keyboard(lang),
    )


# این روتر باید در انتها ثبت شود.
fallback_router = Router()


@fallback_router.message(
    F.text,
    ~F.text.in_(ALL_MAIN_BUTTONS),
    ~F.text.in_(ALL_BACK_BUTTONS),
)
async def fallback(message: Message, state: FSMContext) -> None:
    current = await state.get_state()

    if current:
        return

    user, _ = await get_or_create_user(message)
    lang = user.language or "fa"

    await message.answer(
        t("fallback", lang),
        reply_markup=main_keyboard(lang),
    )
