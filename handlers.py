# handlers.py

from datetime import datetime
import os
from db import get_connection
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def start(update, context):
    await update.message.reply_text(
        "Internship Tracker is live.\n\n"
        "Commands:\n"
        "/add Company Role YYYY-MM-DD\n"
        "/list"
    )


async def add(update, context):
    try:
        company = context.args[0]
        role = context.args[1]
        deadline = context.args[2]

        now = datetime.now().strftime("%Y-%m-%d")

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO internships VALUES (?, ?, ?, ?, ?, ?)",
            (company, role, deadline, "APPLIED", now, now)
        )

        conn.commit()
        conn.close()

        await update.message.reply_text(
            f"✅ Added:\n{company} | {role} | {deadline}"
        )

    except Exception:
        await update.message.reply_text(
            "❌ Usage:\n/add Company Role YYYY-MM-DD"
        )


async def list_all(update, context):
    conn = get_connection()
    cur = conn.cursor()

    rows = cur.execute(
        "SELECT company, role, status, deadline FROM internships"
    ).fetchall()

    conn.close()

    if not rows:
        await update.message.reply_text("No internships tracked yet.")
        return

    msg = "📋 Internship Applications:\n\n"
    for r in rows:
        msg += f"{r[0]} | {r[1]} | {r[2]} | {r[3]}\n"

    await update.message.reply_text(msg)

async def update_status(update, context):
    try:
        company = context.args[0]
        new_status = context.args[1].upper()

        allowed = ["APPLIED", "OA", "INTERVIEW", "OFFER", "REJECTED", "GHOSTED"]
        if new_status not in allowed:
            await update.message.reply_text(
                "Invalid status.\n"
                "Use one of:\n"
                "APPLIED, OA, INTERVIEW, OFFER, REJECTED, GHOSTED"
            )
            return

        now = datetime.now().strftime("%Y-%m-%d")

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            UPDATE internships
            SET status = ?, last_update = ?
            WHERE company = ?
            """,
            (new_status, now, company)
        )

        if cur.rowcount == 0:
            await update.message.reply_text("Company not found.")
            conn.close()
            return

        conn.commit()
        conn.close()

        await update.message.reply_text(
            f"🔄 Updated:\n{company} → {new_status}"
        )

    except Exception:
        await update.message.reply_text(
            "Usage:\n/update Company STATUS"
        )

async def deadline_check(context):
    conn = get_connection()
    cur = conn.cursor()

    rows = cur.execute(
        "SELECT company, role, deadline FROM internships"
    ).fetchall()

    conn.close()

    today = datetime.now().date()
    chat_id = context.job.chat_id

    for r in rows:
        deadline = datetime.strptime(r[2], "%Y-%m-%d").date()
        days_left = (deadline - today).days

        if days_left in (7, 3, 0):
            await context.bot.send_message(
                CHAT_ID = int(os.getenv("CHAT_ID")),
                text=(
                    f"⏰ Deadline reminder\n"
                    f"{r[0]} | {r[1]}\n"
                    f"{days_left} days left"
                )
            )


import csv

async def export_csv(update, context):
    conn = get_connection()
    cur = conn.cursor()

    rows = cur.execute("SELECT * FROM internships").fetchall()
    conn.close()

    filename = "internships_export.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Company", "Role", "Deadline", "Status", "Applied On", "Last Update"])
        writer.writerows(rows)

    await update.message.reply_document(open(filename, "rb"))
