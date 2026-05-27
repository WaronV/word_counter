import sqlite3
import random
import tkinter as tk
from tkinter import ttk # nowsza bilioteka do od ttk i trzeba to tak dodac aby moc korzystac z jeje elementow

conn = sqlite3.connect("data_base.db")
cursor = conn.cursor()

def random_words():
    cursor.execute("SELECT COUNT(*) FROM worktable") # policz wszytskie wiersze w tablicy workplace
    count = cursor.fetchone()[0]
    words = random.sample(range(1, count), 3) # losuje 3 niezalezne liczby ze zbioru
    cursor.execute("SELECT name, count FROM worktable WHERE id IN (?, ?, ?)", words)
    rows = cursor.fetchall()
    rows_names = [row[0] for row in rows]
    rows_counts = [row[1] for row in rows]
    rows_counts = [row + 1 for row in rows_counts]
    rows = [(rows_counts[numb], words[numb]) for numb in range(0,3)]
    cursor.executemany("UPDATE worktable SET count = ? WHERE id = ?", rows) # linijak od zmiany liczby wystapien slowa
    print(f"Words: {rows_names}")
    words_label.config(text = f"Words: {rows_names}")
    #conn.commit()

window = tk.Tk()
window.title("word_counter")
window.geometry("300x200")
table_list = ttk.Combobox(window)
table_list.pack()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") # zbierz wszystkie tablice
tab_list = cursor.fetchall()
table_list["values"] = tab_list

words_label = tk.Label(window, text="Witaj!")
words_label.pack()
random_words()
button_rand = tk.Button(window, text="New words", command=random_words)
button_rand.pack(pady=50)
window.mainloop()

conn.close()
