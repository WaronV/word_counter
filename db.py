from asyncio.windows_events import CONNECT_PIPE_MAX_DELAY
from contextlib import contextmanager
import sqlite3

@contextmanager
def connect_db():
    conn = sqlite3.connect("data_base.db")
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        #conn.commit()
    except Exception as e:
        conn.rollback
        raise e
    finally:
        conn.close()

def list_tables():
    with connect_db() as conn:
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print(tables["name"])
        return tables["name"]

def count_all_rows():
    with connect_db() as conn:
        cursor = conn.execute("SELECT COUNT(*) FROM worktable")
        number = cursor.fetchone()
        print(number)
        return(number)

def take_3_words(words):
    with connect_db() as conn:
        cursor = conn.execute("SELECT name, count FROM worktable WHERE id IN (?, ?, ?)", words)
        rows = cursor.fetchall()
        print(rows["name"])
        return rows["name"]

def change_count(words, numb):
    with connect_db() as conn:
        #cursor = conn.executemany("UPDATE worktable SET count = ? WHERE id = ?", words)
        print("x")
