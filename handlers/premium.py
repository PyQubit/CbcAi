from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from i18n import BTN_PREMIUM_FA, BTN_PREMIUM_EN, t
from keyboards import back_keyboard
from utils.user import get_or_create_user

router = Router()


@router.message(F.text.in_({BTN_PREMIUM_FA, BTN_PREMIUM_EN}))
async def premium_section(message: Message, state: FSMContext) -> None:
    await state.clear()
    user, _ = await get_or_create_user(message)
    lang = user.language or "fa"
    await message.answer(t("premium", lang), reply_markup=back_keyboard(lang))
