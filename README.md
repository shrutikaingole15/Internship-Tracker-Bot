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

### 2️⃣ Create a .env file
```bash
Create a file named .env in the root directory:

BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id


⚠️ This file is ignored by Git and must not be committed.

3️⃣ Install dependencies
```bash
pip install python-telegram-bot python-dotenv

4️⃣ Run the bot
python bot.py


Open Telegram and start chatting with your bot.

🔒 Security Notes

Bot token is never committed

.env and database files are ignored via .gitignore

Safe to fork and reuse with your own credentials

📈 Future Improvements

Application analytics (/stats, /funnel)

Weekly summary reports

Cloud deployment (24/7 uptime)

Google Sheets integration

Multi-user support

👩‍💻 Author

Built by Shrutika Ingole as a personal automation project to improve consistency and discipline during internship applications.

⭐ Why this matters

This project demonstrates:

real-world backend structure

async debugging & scheduling

secure configuration handling

system-oriented thinking over one-off scripts


---

### What to do now (quick checklist)
1. Open `README.md` in VS Code  
2. Paste **everything above**  
3. Save (`Ctrl + S`)  
4. Run:
   ```bash
   git add README.md
   git commit -m "Add detailed README"
   git push
