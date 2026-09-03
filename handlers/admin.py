from datetime import datetime, timedelta

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import func, select

from database import Session
from models import ChatMessage, LabMessage, User
from utils.admin import is_admin

router = Router()


@router.message(Command("admin"))
async def admin_panel(message: Message) -> None:
    """نمایش داشبورد مدیریت برای ادمین‌ها."""

    if not is_admin(message.from_user.id):
        await message.answer(
            "⛔ <b>دسترسی غیرمجاز</b>\n"
            "شما اجازه استفاده از پنل مدیریت را ندارید."
        )
        return

    since = datetime.utcnow() - timedelta(hours=24)

    async with Session() as db:
        total_users = (
            await db.execute(
                select(func.count(User.id))
            )
        ).scalar() or 0

        chat_today = (
            await db.execute(
                select(func.count(ChatMessage.id)).where(
                    ChatMessage.role == "user",
                    ChatMessage.timestamp >= since,
                )
            )
        ).scalar() or 0

        lab_today = (
            await db.execute(
                select(func.count(LabMessage.id)).where(
                    LabMessage.role == "user",
                    LabMessage.timestamp >= since,
                )
            )
        ).scalar() or 0

        total_chat = (
            await db.execute(
                select(func.count(ChatMessage.id)).where(
                    ChatMessage.role == "user"
                )
            )
        ).scalar() or 0

        total_lab = (
            await db.execute(
                select(func.count(LabMessage.id)).where(
                    LabMessage.role == "user"
                )
            )
        ).scalar() or 0

    await message.answer(
        f"""
🛡 <b>داشبورد مدیریت CbcAi</b>

━━━━━━━━━━━━━━━━━━

👥 <b>کاربران</b>
└ <b>{total_users}</b> کاربر ثبت‌نام کرده‌اند.

📅 <b>فعالیت ۲۴ ساعت گذشته</b>
├ 💬 مشاوره پزشکی: <b>{chat_today}</b> پیام
└ 🧪 تحلیل آزمایش: <b>{lab_today}</b> پیام

📊 <b>آمار کلی سامانه</b>
├ 💬 کل پیام‌های مشاوره: <b>{total_chat}</b>
└ 🧪 کل پیام‌های تحلیل آزمایش: <b>{total_lab}</b>

━━━━━━━━━━━━━━━━━━

🆔 <b>شناسه ادمین</b>
<code>{message.from_user.id}</code>

<i>✨ تمامی آمار به‌صورت لحظه‌ای از پایگاه داده دریافت شده‌اند.</i>
"""
    )