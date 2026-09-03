from datetime import datetime, timedelta

from sqlalchemy import func, select

from config import DAILY_CHAT_LIMIT, DAILY_DOCTOR_LIMIT
from database import Session
from models import ChatMessage, DoctorMessage


async def count_chat_messages_today(user_db_id: int) -> int:
    """تعداد پیام‌های کاربر در بخش مشاوره (۲۴ ساعت گذشته)"""
    since = datetime.utcnow() - timedelta(hours=24)
    async with Session() as db:
        result = await db.execute(
            select(func.count(ChatMessage.id)).where(
                ChatMessage.user_id == user_db_id,
                ChatMessage.role == "user",
                ChatMessage.timestamp >= since,
            )
        )
        return result.scalar() or 0


async def check_chat_limit(user_db_id: int) -> tuple[bool, int]:
    """(آیا مجاز است؟, تعداد پیام باقی‌مانده امروز)"""
    used = await count_chat_messages_today(user_db_id)
    remaining = max(0, DAILY_CHAT_LIMIT - used)
    return used < DAILY_CHAT_LIMIT, remaining


async def count_doctor_messages_today(user_db_id: int) -> int:
    """تعداد پیام‌های کاربر در بخش راهنمای تخصص (۲۴ ساعت گذشته)"""
    since = datetime.utcnow() - timedelta(hours=24)
    async with Session() as db:
        result = await db.execute(
            select(func.count(DoctorMessage.id)).where(
                DoctorMessage.user_id == user_db_id,
                DoctorMessage.role == "user",
                DoctorMessage.timestamp >= since,
            )
        )
        return result.scalar() or 0


async def check_doctor_limit(user_db_id: int) -> tuple[bool, int]:
    """(آیا مجاز است؟, تعداد پیام باقی‌مانده امروز در راهنمای تخصص)"""
    used = await count_doctor_messages_today(user_db_id)
    remaining = max(0, DAILY_DOCTOR_LIMIT - used)
    return used < DAILY_DOCTOR_LIMIT, remaining
