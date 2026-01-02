# models.py
from db import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS internships (
        company TEXT PRIMARY KEY,
        role TEXT NOT NULL,
        deadline TEXT NOT NULL,
        status TEXT NOT NULL,
        applied_on TEXT NOT NULL,
        last_update TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
