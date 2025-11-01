import sqlite3

db = sqlite3.connect("todos.db", check_same_thread=False)
cursor = db.cursor()