from aiogram.types import Message
from sqlalchemy import select

from database import Session
from models import User


async def get_or_create_user(message: Message) -> tuple[User, bool]:
    """
    دریافت یا ساخت کاربر.
    خروجی: (user, is_new)
    """
    async with Session() as db:
        result = await db.execute(
            select(User).where(User.telegram_id == message.from_user.id)
        )
        user = result.scalar()

        if not user:
            user = User(
                telegram_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                language="fa",
            )
            db.add(user)
            await db.commit()
            await db.refresh(user)
            return user, True

        updated = False
        if user.username != message.from_user.username:
            user.username = message.from_user.username
            updated = True
        if user.first_name != message.from_user.first_name:
            user.first_name = message.from_user.first_name
            updated = True
        if not getattr(user, "language", None):
            user.language = "fa"
            updated = True
        if updated:
            await db.commit()
        return user, False


async def set_user_language(telegram_id: int, lang: str) -> User | None:
    """تغییر زبان کاربر (fa یا en)"""
    if lang not in ("fa", "en"):
        return None
    async with Session() as db:
        result = await db.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar()
        if not user:
            return None
        user.language = lang
        await db.commit()
        await db.refresh(user)
        return user


async def get_user_language(telegram_id: int) -> str:
    async with Session() as db:
        result = await db.execute(
            select(User.language).where(User.telegram_id == telegram_id)
        )
        lang = result.scalar()
        return lang if lang in ("fa", "en") else "fa"
