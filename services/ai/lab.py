"""
سرویس هوش مصنوعی تحلیل آزمایش
کاملاً جدا از مشاوره پزشکی — پرامپت، تاریخچه و مدل مستقل

نسخه فعلی: placeholder (به زودی)
نسخه آینده: OCR + تحلیل شاخص‌ها
"""

from sqlalchemy import desc, select

from config import MODEL_LAB
from database import Session
from models import LabMessage
from services.ai.client import groq_client

# پرامپت اختصاصی تحلیل آزمایش (برای نسخه آینده)
LAB_SYSTEM_PROMPT = """
تو یک دستیار هوشمند تحلیل نتایج آزمایش پزشکی به نام CbcAi هستی.

وظیفه تو توضیح ساده، علمی و قابل فهم شاخص‌های آزمایش خون و سایر آزمایش‌هاست.

قوانین:
- فقط به زبان فارسی پاسخ بده.
- هرگز تشخیص قطعی نده.
- فقط مجاز به تگ‌های HTML: <b></b> و <strong></strong>
- حداکثر ۱۰۰۰ کاراکتر.
"""


async def _save(user_id: int, role: str, content: str) -> None:
    async with Session() as db:
        db.add(LabMessage(user_id=user_id, role=role, content=content))
        await db.commit()


async def _history(user_id: int, limit: int = 6) -> list[dict]:
    async with Session() as db:
        result = await db.execute(
            select(LabMessage.role, LabMessage.content)
            .where(LabMessage.user_id == user_id)
            .order_by(desc(LabMessage.id))
            .limit(limit)
        )
        rows = result.all()
    rows.reverse()
    return [{"role": r, "content": c} for r, c in rows]


async def ask_lab(user_id: int, text: str) -> str:
    """
    تحلیل متن/نتیجه آزمایش.
    فعلاً قابلیت کامل فعال نیست؛ برای توسعه آینده آماده است.
    """
    # نسخه آینده:
    # messages = [{"role": "system", "content": LAB_SYSTEM_PROMPT}]
    # messages.extend(await _history(user_id))
    # messages.append({"role": "user", "content": text})
    # response = await groq_client.chat.completions.create(...)
    # answer = ...
    # await _save(...)
    # return answer

    raise NotImplementedError("تحلیل آزمایش هنوز پیاده‌سازی نشده است.")