# bot.py

import datetime
from telegram.ext import ApplicationBuilder, CommandHandler

from config import BOT_TOKEN
from models import init_db
from handlers import (
    start,
    add,
    list_all,
    update_status,
    deadline_check,
    export_csv,
)

CHAT_ID = 6637335833  # <-- put your actual chat id here

def main():
    init_db()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("list", list_all))
    app.add_handler(CommandHandler("update", update_status))
    app.add_handler(CommandHandler("export", export_csv))

    # Telegram-native scheduler (SAFE)
    app.job_queue.run_daily(
        deadline_check,
        time=datetime.time(hour=9, minute=0),
        chat_id=CHAT_ID
    )

    print("Internship Tracker running...")
    app.run_polling()

if __name__ == "__main__":
    main()
