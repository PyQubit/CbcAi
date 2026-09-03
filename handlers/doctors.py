import logging
import time

from aiogram import Bot, F, Router
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import DAILY_DOCTOR_LIMIT
from i18n import (
    BTN_DOCTORS_FA,
    BTN_DOCTORS_EN,
    ALL_MAIN_BUTTONS,
    ALL_BACK_BUTTONS,
    t,
)
from keyboards import back_keyboard
from services.ai.doctors import ask_doctor_guide
from states import UserState
from utils.limits import check_doctor_limit
from utils.user import get_or_create_user

router = Router()
logger = logging.getLogger(__name__)

COOLDOWN_SECONDS = 3
_cooldowns: dict[int, float] = {}


@router.message(F.text.in_({BTN_DOCTORS_FA, BTN_DOCTORS_EN}))
async def enter_doctor_guide(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.doctor_guide)
    user, _ = await get_or_create_user(message)
    lang = user.language or "fa"

    await message.answer(
        t("enter_doctors", lang),
        reply_markup=back_keyboard(lang),
    )


@router.message(
    UserState.doctor_guide,
    F.text,
    ~F.text.in_(ALL_MAIN_BUTTONS),
    ~F.text.in_(ALL_BACK_BUTTONS),
)
async def doctor_guide_handler(message: Message, state: FSMContext, bot: Bot) -> None:
    text = message.text or ""
    user, _ = await get_or_create_user(message)
    lang = user.language or "fa"

    uid = message.from_user.id
    now = time.time()
    last = _cooldowns.get(uid, 0)
    if now - last < COOLDOWN_SECONDS:
        await message.answer(t("cooldown", lang))
        return
    _cooldowns[uid] = now

    allowed, remaining = await check_doctor_limit(user.id)
    if not allowed:
        await message.answer(
            t("limit_reached", lang, limit=DAILY_DOCTOR_LIMIT),
            reply_markup=back_keyboard(lang),
        )
        return

    await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    try:
        answer = await ask_doctor_guide(user.id, text, lang=lang)

        suffix = ""
        if remaining <= 3:
            if lang == "en":
                suffix = f"\n\n📩 <b>{remaining} free messages remaining today.</b>"
            else:
                suffix = f"\n\n📩 <b>{remaining} پیام رایگان باقی‌مانده امروز شما بود.</b>"

        await message.answer(answer + suffix, parse_mode="HTML")
    except Exception as e:
        logger.exception("Doctor guide error: %s", e)
        await message.answer(t("chat_error", lang))
