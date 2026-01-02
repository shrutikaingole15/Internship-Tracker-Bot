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
