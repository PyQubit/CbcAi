import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
CHANNEL = os.getenv("CHANNEL")

# مدل مشترک
MODEL_CHAT = os.getenv("MODEL_CHAT", "openai/gpt-oss-120b")
MODEL_LAB = os.getenv("MODEL_LAB", "openai/gpt-oss-120b")

# آیدی ادمین‌ها — با کاما جدا کنید
_raw_admins = os.getenv("ADMIN_IDS", "")
ADMIN_IDS: set[int] = {
    int(x.strip())
    for x in _raw_admins.split(",")
    if x.strip().isdigit()
}

# محدودیت روزانه
DAILY_CHAT_LIMIT = int(os.getenv("DAILY_CHAT_LIMIT", "10"))
DAILY_DOCTOR_LIMIT = int(os.getenv("DAILY_DOCTOR_LIMIT", "10"))
