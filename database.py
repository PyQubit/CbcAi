from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy import text

from config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=False)
Session = async_sessionmaker(engine, expire_on_commit=False)


async def create_db() -> None:
    from models import Base

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # مهاجرت سبک برای افزودن ستون language در صورت نبودن
        try:
            await conn.execute(
                text(
                    "ALTER TABLE users ADD COLUMN IF NOT EXISTS language VARCHAR(5) DEFAULT 'fa'"
                )
            )
        except Exception:
            pass  # SQLite یا دیتابیس‌های قدیمی ممکن است پشتیبانی نکنند
