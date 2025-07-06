# 🤖 AIChatForWork

AIChatForWork is a multilingual Telegram bot built with **Aiogram 3** and powered by **OpenAI (ChatGPT)**.  
Users can ask topic-based questions in 3 languages. Admins can broadcast messages with delivery stats.

---

## 🔧 Tech Stack

- Python 3.10+
- Aiogram 3.x
- OpenAI (ChatGPT)
- Django REST API (for user and answer tracking)
- PostgreSQL

---

## ✨ Features

- 🌍 Language support: Uzbek, English, Russian
- 🧠 Ask questions by topic (limit: 3 per day)
- 🤖 Smart AI responses using ChatGPT
- 📢 Admin panel: send text or forwarded ads to all users

---

## 🚀 Getting Started

```bash
[git clone https://github.com/yourusername/AIChatForWork.git](https://github.com/muhammadnuruz/ask_question_bot.git)
cd ask_question_bot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
python main.py
```
## 🔐 Environment Configuration

Create a `.env` file in the project root and add the following:

```bash
BOT_TOKEN=your_telegram_token
OPENAI_API_KEY=your_openai_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432(postgresql's_post)
```

---

## 📂 Project Structure

bot/
├── handlers/ # start, question, admin handlers
├── buttons/ # reply & inline keyboards
├── dispatcher.py # Dispatcher and bot instance
main.py # Entry point
apps/ # Django-side API config (users, answers)

---

## 👤 Author

**Muhammad Nur** — Telegram AI bot developer  
🔗 [GitHub Profile](https://github.com/yourusername)
