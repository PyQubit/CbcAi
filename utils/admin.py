from config import ADMIN_IDS


def is_admin(telegram_id: int) -> bool:
    """فقط آیدی‌های موجود در ADMIN_IDS دسترسی دارند"""
    return telegram_id in ADMIN_IDS