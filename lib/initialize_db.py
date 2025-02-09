import sqlite3

DATABASE = "movies.db"

def initialize_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                genre TEXT NOT NULL,
                release_year INTEGER NOT NULL,
                watched BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
        conn.commit()
        print("Database initialized.")

initialize_db()
