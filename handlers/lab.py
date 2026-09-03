from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from i18n import BTN_LAB_FA, BTN_LAB_EN, ALL_MAIN_BUTTONS, ALL_BACK_BUTTONS, t
from keyboards import back_keyboard
from states import UserState
from utils.user import get_or_create_user

router = Router()


@router.message(F.text.in_({BTN_LAB_FA, BTN_LAB_EN}))
async def enter_lab(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.lab_analysis)
    user, _ = await get_or_create_user(message)
    lang = user.language or "fa"

    await message.answer(
        t("lab_coming_soon", lang),
        reply_markup=back_keyboard(lang),
    )


@router.message(
    UserState.lab_analysis,
    ~F.text.in_(ALL_MAIN_BUTTONS),
    ~F.text.in_(ALL_BACK_BUTTONS),
)
async def lab_handler(message: Message, state: FSMContext) -> None:
    user, _ = await get_or_create_user(message)
    lang = user.language or "fa"
    await message.answer(
        t("lab_not_ready", lang),
        reply_markup=back_keyboard(lang),
    )
