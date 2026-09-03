# 🩺 CbcAi — AI-Powered Medical Assistant

**CbcAi** is an AI-powered conversational medical assistant built as a Telegram bot to provide general health information, initial medical guidance, specialty navigation, and AI-assisted laboratory analysis workflows.

The project combines **Large Language Models (LLMs), conversational AI, user profiles, usage management, safety-aware prompting, PostgreSQL, and a modular Telegram bot architecture**.

> ⚠️ **Medical Disclaimer:** CbcAi is an informational and educational AI assistant. It is not a medical professional and does not replace professional medical evaluation, diagnosis, treatment, or emergency care.

---

## ✨ Features

| Feature                        | Description                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------ |
| 🩺 **AI Medical Assistant**    | Conversational AI for general health and symptom-related questions             |
| 👨‍⚕️ **Specialty Guidance**   | Helps users identify the appropriate medical specialty based on their concerns |
| 🔬 **Laboratory Analysis**     | Dedicated laboratory-analysis architecture, currently under development        |
| 🧠 **User Context**            | Stores structured user information to support more contextual interactions     |
| 🌐 **Bilingual Support**       | Persian and English language support                                           |
| ⚙️ **Account Settings**        | Language preferences and usage information                                     |
| 🛡️ **Safety-Aware Responses** | Designed to avoid presenting AI responses as definitive medical diagnoses      |
| 👨‍💼 **Admin Panel**          | User and message statistics with admin-only access                             |
| 💎 **Premium Architecture**    | Foundation for usage limits and premium features                               |
| 🗄️ **Persistent Storage**     | PostgreSQL-backed application data                                             |
| ⚡ **Async Architecture**       | Asynchronous Python architecture for efficient bot operations                  |

---

## 🧠 AI Models

CbcAi is designed around a modular AI client, allowing the underlying model to be changed through configuration rather than tightly coupling the application to a single model.

The current configuration uses:

| Use Case             | Model                 | Provider |
| -------------------- | --------------------- | -------- |
| Medical Conversation | `openai/gpt-oss-120b` | Groq     |
| Specialty Guidance   | `openai/gpt-oss-120b` | Groq     |
| Laboratory Workflow  | `openai/gpt-oss-120b` | Groq     |

This architecture makes it possible to introduce additional models or providers in the future.

---

## 🏗️ Architecture

CbcAi follows a modular architecture that separates Telegram handlers, AI services, database access, configuration, and reusable utilities.

```text
                         ┌─────────────────────┐
                         │       Telegram      │
                         │        User         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Telegram Bot      │
                         │      Handlers       │
                         └──────────┬──────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
             ▼                      ▼                      ▼
       ┌───────────┐          ┌───────────┐          ┌───────────┐
       │   Chat    │          │    Lab    │          │  Doctors  │
       │  Handler  │          │  Handler  │          │  Handler  │
       └─────┬─────┘          └─────┬─────┘          └─────┬─────┘
             │                      │                      │
             └──────────────────────┼──────────────────────┘
                                    ▼
                         ┌─────────────────────┐
                         │     AI Services     │
                         ├─────────────────────┤
                         │ Chat                │
                         │ Laboratory          │
                         │ Doctors             │
                         │ AI Client           │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    LLM Provider     │
                         └─────────────────────┘

                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     PostgreSQL      │
                         │       Database      │
                         └─────────────────────┘
```

---

## 📁 Project Structure

```text
CbcAi/
│
├── handlers/
│   ├── __init__.py
│   ├── admin.py
│   ├── chat.py
│   ├── common.py
│   ├── doctors.py
│   ├── lab.py
│   ├── premium.py
│   └── settings.py
│
├── services/
│   └── ai/
│       ├── __init__.py
│       ├── client.py
│       ├── chat.py
│       ├── doctors.py
│       └── lab.py
│
├── utils/
│   ├── __init__.py
│   ├── admin.py
│   ├── limits.py
│   └── user.py
│
├── config.py
├── database.py
├── i18n.py
├── keyboards.py
├── main.py
├── models.py
├── states.py
├── requirements.txt
├── .env.example
├── welcome.jpg
└── LICENSE
```

---

## 🧩 Architecture Components

| Component      | Responsibility                                      |
| -------------- | --------------------------------------------------- |
| `handlers/`    | Telegram commands, callbacks, and user interactions |
| `services/ai/` | AI-related business logic and model communication   |
| `database.py`  | Database connection and initialization              |
| `models.py`    | Database models                                     |
| `config.py`    | Environment-based application configuration         |
| `i18n.py`      | Internationalization and localized messages         |
| `keyboards.py` | Telegram keyboard interfaces                        |
| `states.py`    | Conversation and interaction states                 |
| `utils/`       | Reusable application utilities                      |
| `main.py`      | Application entry point                             |

---

## 🛠️ Technology Stack

### Backend

* Python 3.10+
* Async Python
* PostgreSQL
* SQLAlchemy
* aiogram

### Artificial Intelligence

* Large Language Models
* Conversational AI
* Prompt Engineering
* Context Management
* AI API Integration
* Safety-Aware AI Design

### Infrastructure

* Environment-based configuration
* Linux deployment
* systemd
* PostgreSQL
* External AI APIs

---

## 🔄 Request Flow

A typical conversation follows this flow:

```text
User
  │
  ▼
Telegram
  │
  ▼
Telegram Handler
  │
  ▼
User / Context Management
  │
  ▼
AI Service
  │
  ▼
LLM Client
  │
  ▼
Language Model
  │
  ▼
Response Processing
  │
  ▼
Telegram
  │
  ▼
User
```

---

## 🔐 Environment Configuration

CbcAi uses environment variables for sensitive configuration.

Create a local `.env` file based on `.env.example`:

```env
BOT_TOKEN=
GROQ_API_KEY=
DATABASE_URL=

MODEL_CHAT=openai/gpt-oss-120b
MODEL_LAB=openai/gpt-oss-120b

DAILY_CHAT_LIMIT=10
DAILY_DOCTOR_LIMIT=10
ADMIN_IDS=
```

> 🔒 **Never commit `.env`, API keys, passwords, database credentials, or other secrets to Git.**

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/PyQubit/CbcAi.git
cd CbcAi
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env` from `.env.example` and provide your own configuration.

### 5. Configure PostgreSQL

Create a PostgreSQL database and configure the connection string through `DATABASE_URL`.

Example:

```env
DATABASE_URL=postgresql+asyncpg://cbcai:your_password@localhost:5432/cbcai
```

### 6. Start the bot

```bash
python main.py
```

The application initializes the required database structures and starts the Telegram bot.

---

## ⚙️ Production Deployment

CbcAi can be deployed as a persistent Linux service using `systemd`.

Example service configuration:

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

Enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable cbcai
sudo systemctl start cbcai
sudo systemctl status cbcai
```

View logs:

```bash
journalctl -u cbcai -f
```

> For production environments, running services under a dedicated non-root system user is recommended.

---

## 🤖 Bot Commands

| Command     | Description                                |
| ----------- | ------------------------------------------ |
| `/start`    | Start the assistant and open the main menu |
| `/help`     | Display usage information                  |
| `/about`    | About CbcAi                                |
| `/language` | Change language                            |
| `/admin`    | Open the administrator panel               |

---

## 🛡️ Safety & Medical Disclaimer

CbcAi is designed to provide **general informational and educational assistance**.

Its responses should not be considered:

* A medical diagnosis
* A professional medical opinion
* A treatment prescription
* A substitute for a doctor
* Emergency medical guidance

Users experiencing potentially serious or emergency symptoms should seek immediate assistance from qualified healthcare professionals or local emergency services.

---

## 🎯 Engineering Objectives

CbcAi was built as a practical AI engineering project rather than a standalone machine-learning experiment.

The project demonstrates:

* LLM integration into a real user-facing application
* Modular Telegram bot architecture
* Asynchronous Python development
* PostgreSQL-backed persistence
* User context and profile management
* AI service abstraction
* Safety-aware prompt design
* Usage-limit management
* Internationalization
* Administrative functionality
* External AI API integration
* Linux service deployment

---

## 🔮 Future Development

Planned improvements may include:

* Advanced laboratory report understanding
* Multimodal medical document processing
* Retrieval-Augmented Generation (RAG)
* Medical knowledge-base integration
* Improved AI model routing
* Advanced monitoring and observability
* Automated testing
* Docker deployment
* CI/CD pipelines
* Expanded subscription management
* Analytics dashboard

---

## 👨‍💻 Author

**Mohammad Mahdi Omidvar — PyQubit**

AI Engineer & Data Scientist focused on:

* Artificial Intelligence
* Machine Learning & Deep Learning
* NLP & Transformers
* Computer Vision
* Generative AI
* AI Engineering
* Backend Development
* Data Science

🏆 **Gold Medalist — INNOVERSE 2025 (AI Section)**

* GitHub: https://github.com/PyQubit
* Portfolio: https://pyqubit.github.io/

---

## 📄 License

CbcAi is **proprietary software**.

The source code is publicly visible for portfolio, educational, and evaluation purposes, but **no permission is granted to use, copy, modify, distribute, sublicense, sell, or create derivative works from this software without explicit written permission from the copyright holder.**

See [`LICENSE`](LICENSE) for the complete terms.
