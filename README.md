# 🧠 SerenAI
> A Mental Health Support Platform powered by AI and Django.

SerenAI is a web-based platform designed to provide emotional support, relaxation techniques, and mental health resources. It integrates Large Language Models (LLMs) to offer a gentle, supportive conversational interface.

---

## ⚠️ Project Status — Security and Ethics Pivot

**Current State: Secure Prototype**

Development was intentionally paused to address critical AI Safety and Data Privacy concerns:

1. **Data Sovereignty** — Evaluating methods to prevent sensitive user emotional data from being used for third-party LLM training.
2. **Prompt Injection Hardening** — Developing robust sanitization layers to prevent malicious overrides of the system's therapeutic guidelines.
3. **Privacy-First Architecture** — Transitioning to local LLM hosting (on-premise) to ensure end-to-end encryption of conversations.

---

## 🛠️ Technical Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.x, Django 5.0 |
| **AI Orchestration** | LangChain, OpenAI API |
| **Database** | PostgreSQL (Production), SQLite (Development) |
| **Environment** | Fedora Linux |

---

## 🚀 Setup and Installation

### Prerequisites

- Python installed
- PostgreSQL or SQLite

### Installation Steps

**1. Clone and Navigate**
```bash
git clone https://github.com/andrawiP801/SerenAI-Platform.git
cd SerenAI-Platform
```

**2. Environment Setup (Linux)**
```bash
python -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Configuration**
```bash
# Create a .env file in the root directory based on .env.example
# Do not modify settings.py directly
# Set DJANGO_DEBUG=True for local development
```

**5. Database Initialization**
```bash
python manage.py migrate
python manage.py load_book_covers
python manage.py createsuperuser
```

---

## 💻 Usage

**Run the Development Server**
```bash
python manage.py runserver
```
Access the site at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

**Admin Panel Configuration**
- Visit `/admin/` to manage users and logs.
- Configure AI parameters at `/admin/chatai/siteconfig/`
- Ensure your `OPENAI_API_KEY` is set in your `.env` file.

---

## 🔒 Security Features

- **Secret Isolation** — Environment variables for all sensitive keys (API Keys, DB Passwords).
- **System Prompt Pinning** — Strict persona definition via LangChain to maintain ethical boundaries.
- **Hardened Settings** — Production-ready HSTS and SSL configurations for secure deployments.

---

> **⚕️ Disclaimer:** SerenAI is not a substitute for professional medical advice. Always seek professional assistance for mental health concerns.

  
