import sqlite3
import time


def init():
    with sqlite3.connect("passwords.db", check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS passwords(id integer primary key, website text, email text, password text, date_create TIMESTAMP)"
        )
        print("Database initialised")


def add_password(website, email, password):
    with sqlite3.connect("passwords.db", check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO passwords(website, email, password, date_create) VALUES (?, ?, ?, ?)",
                       (website, email, password, time.time()))
        conn.commit()
