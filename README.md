# 📌 Internship Tracker Telegram Bot

A personal Telegram bot built to **track internship applications, deadlines, and status updates**, designed to replace messy spreadsheets and forgotten Notion pages with a simple, disciplined workflow.

This bot is actively used as a **daily application-tracking system**.

---

## 🚀 Why this project?

Applying to internships usually means:
- tracking dozens of applications
- forgetting deadlines
- losing context about where each application stands

Instead of using static tools, this project builds a **stateful, automated system** that:
- remembers application history
- enforces consistency
- sends deadline reminders
- keeps data private and local

This is not a demo bot — it is a **personal productivity system**.

---

## ✨ Features

### Core functionality
- ➕ Add internship applications
- 📋 List all applications
- 🔄 Update application status
- 📤 Export application data to CSV

### Automation
- ⏰ Daily deadline reminders (7, 3, and 0 days before deadline)
- ⚠️ “Needs action” view for applications stuck too long

### Design principles
- Persistent storage (data survives restarts)
- Clear state transitions
- No hardcoded secrets
- Minimal commands, maximum clarity

---

## 🧠 Command List

| Command | Description |
|------|------------|
| `/start` | Start the bot |
| `/add <Company> <Role> <YYYY-MM-DD>` | Add a new application |
| `/list` | View all tracked applications |
| `/update <Company> <Status>` | Update application status |
| `/action` | View applications needing attention |
| `/export` | Export all data as CSV |

### Supported Status Values 
APPLIED
OA
INTERVIEW
OFFER
REJECTED


---

## 🛠 Tech Stack

- **Language**: Python  
- **Framework**: python-telegram-bot (v20+)  
- **Database**: SQLite  
- **Scheduling**: Telegram JobQueue  
- **Version Control**: Git & GitHub  

Secrets are managed using environment variables (`.env`), following best practices.

---

## 📂 Project Structure



internship-tracker-bot/
│── bot.py # Entry point
│── handlers.py # Bot command handlers
│── db.py # Database connection
│── models.py # Database schema
│── config.py # Configuration loader
│── .gitignore
│── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/internship-tracker-bot.git
cd internship-tracker-bot
```

### 2️⃣ Create a .env file

Create a file named .env in the root directory:
```bash
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
```

⚠️ This file is ignored by Git and must not be committed.

3️⃣ Install dependencies
```bash
pip install python-telegram-bot python-dotenv
```

4️⃣ Run the bot
```bash
python bot.py
```

---

## 🔒 Security Notes

- Telegram bot token and chat ID are stored in a local `.env` file
- `.env` is excluded from version control using `.gitignore`
- Database files (`*.db`) are not committed
- No secrets are hardcoded anywhere in the repository

This makes the project safe to publish and easy for others to fork and reuse.

---

## 📈 Future Improvements

Planned and possible extensions for this project:

- 📊 Application analytics (`/stats`, `/funnel`)
- 📅 Weekly summary reports via Telegram
- ☁️ Cloud deployment for 24/7 availability
- 📄 Google Sheets integration
- 👥 Multi-user support
- 🧠 Smart reminders based on inactivity patterns

---

## 👩‍💻 Author

Built by **Shrutika Ingole** as a personal automation project to improve consistency, organization, and discipline during internship applications.

This project reflects hands-on experience with:
- backend structuring
- async scheduling
- environment-based configuration
- real-world debugging

---

## ⭐ Why this project matters

This project demonstrates:

- Practical backend development (not a tutorial clone)
- Persistent state management
- Secure handling of secrets
- Automation using scheduled jobs
- System-oriented thinking over one-off scripts

It is actively used as a **personal productivity system**, not just a demo.

---

## 📌 License

This project is open for learning and personal use.  
Feel free to fork, modify, and adapt it for your own workflow.
