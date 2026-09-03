# 🩺 CbcAi

**دستیار هوشمند مشاوره پزشکی**

ربات تلگرام مبتنی بر هوش مصنوعی برای مشاوره اولیه پزشکی، راهنمای انتخاب تخصص و (به‌زودی) تحلیل آزمایش.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-blue.svg)](https://docs.aiogram.dev/)
[![Groq](https://img.shields.io/badge/AI-Groq-orange.svg)](https://groq.com/)

---

## ✨ امکانات

| قابلیت | توضیح |
|--------|--------|
| 🩺 **مشاوره پزشکی هوشمند** | چت متنی درباره علائم، بیماری‌ها و راهنمایی اولیه |
| 👨‍⚕️ **راهنمای انتخاب تخصص** | با چند سؤال مشخص می‌کند پیش چه نوع متخصصی بروید (بدون نام پزشک واقعی) |
| 🔬 **تحلیل آزمایش** | در حال توسعه |
| 🌐 **دوزبانه** | فارسی و انگلیسی — انتخاب زبان در اولین `/start` |
| ⚙️ **تنظیمات حساب** | وضعیت مصرف روزانه و تغییر زبان |
| 💎 **اشتراک ویژه** | به‌زودی |
| 🛡 **پنل ادمین** | آمار کاربران و پیام‌ها (`/admin`) |

---

## 🧠 مدل هوش مصنوعی

| کاربرد | مدل پیش‌فرض | ارائه‌دهنده |
|--------|-------------|-------------|
| مشاوره پزشکی | `openai/gpt-oss-120b` | Groq |
| راهنمای تخصص | `openai/gpt-oss-120b` | Groq |

---

## 📁 ساختار پروژه

```
cbcai/
├── main.py
├── config.py
├── database.py
├── models.py
├── states.py
├── i18n.py
├── keyboards.py
├── requirements.txt
├── .env.example
├── welcome.jpg
├── handlers/
│   ├── common.py      # /start, /help, /about, زبان
│   ├── chat.py        # مشاوره پزشکی
│   ├── doctors.py     # راهنمای تخصص
│   ├── lab.py         # تحلیل آزمایش (به‌زودی)
│   ├── settings.py
│   ├── premium.py
│   └── admin.py
├── services/ai/
│   ├── client.py
│   ├── chat.py
│   ├── doctors.py
│   └── lab.py
└── utils/
    ├── user.py
    ├── limits.py
    └── admin.py
```

---

## 📋 پیش‌نیازها

- Python **3.10+**
- PostgreSQL **14+**
- حساب [Groq](https://console.groq.com/) و API Key
- ربات تلگرام از [@BotFather](https://t.me/BotFather)

---

## 🚀 نصب و راه‌اندازی

### ۱. کلون

```bash
git clone https://github.com/PyQubit/CbcAi.git
cd CbcAi
```

### ۲. وابستگی‌ها

```bash
pip install -r requirements.txt
# یا:
pip3 install -r requirements.txt --break-system-packages
```

### ۳. دیتابیس

```sql
CREATE USER cbcai WITH PASSWORD 'your_strong_password';
CREATE DATABASE cbcai OWNER cbcai;
GRANT ALL PRIVILEGES ON DATABASE cbcai TO cbcai;
\c cbcai
GRANT ALL ON SCHEMA public TO cbcai;
ALTER SCHEMA public OWNER TO cbcai;
```

### ۴. محیط

```bash
cp .env.example .env
nano .env
```

```env
BOT_TOKEN=123456:ABC-DEF...
GROQ_API_KEY=gsk_...
DATABASE_URL=postgresql+asyncpg://cbcai:your_strong_password@localhost:5432/cbcai

MODEL_CHAT=openai/gpt-oss-120b
MODEL_LAB=openai/gpt-oss-120b

DAILY_CHAT_LIMIT=10
DAILY_DOCTOR_LIMIT=10
ADMIN_IDS=123456789
```

> ⚠️ هرگز `.env` را کامیت نکنید.

### ۵. اجرا

```bash
python3 main.py
```

جداول به‌صورت خودکار ساخته می‌شوند. برای کاربر جدید اول زبان پرسیده می‌شود، سپس پیام خوش‌آمدگویی با `welcome.jpg` ارسال می‌گردد.

---

## 🔄 systemd (اجرای دائمی)

```ini
[Unit]
Description=CbcAi Telegram Bot
After=network.target postgresql.service

[Service]
Type=simple
User=root
WorkingDirectory=/root/cbcai
ExecStart=/usr/bin/python3 /root/cbcai/main.py
Restart=always
RestartSec=5
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable cbcai
sudo systemctl start cbcai
sudo systemctl status cbcai
journalctl -u cbcai -f
```

---

## 🛠 دستورات ربات

| دستور | توضیح |
|--------|--------|
| `/start` | شروع و منوی اصلی |
| `/help` | راهنما |
| `/about` | درباره |
| `/language` | تغییر زبان |
| `/admin` | پنل آمار (فقط ادمین) |

---

## ⚠️ سلب مسئولیت

پاسخ‌های CbcAi صرفاً **آموزشی و اطلاع‌رسانی** هستند و جایگزین معاینه پزشک، تشخیص قطعی یا درمان نیستند. در علائم اورژانسی فوراً به اورژانس مراجعه کنید.

---

## 👤 توسعه‌دهنده

**محمد مهدی امیدوار** — [PyQubit](https://github.com/PyQubit)

- GitHub: [github.com/PyQubit](https://github.com/PyQubit)
- Portfolio: [pyqubit.github.io](https://pyqubit.github.io/)

---

## 📄 مجوز

MIT — استفاده، تغییر و انتشار آزاد است.
