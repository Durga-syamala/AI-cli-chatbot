
import sqlite3

class Database:

    def __init__(self, path="chatbot.db"):
        self.conn = sqlite3.connect(path)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                provider TEXT,
                model TEXT,
                role TEXT,
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS usage (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                provider TEXT,
                model TEXT,
                input_tokens INTEGER,
                output_tokens INTEGER,
                estimated_cost REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.conn.commit()

    def save_message(self, provider, model, role, content):
        self.conn.execute(
            """INSERT INTO conversations
            (provider, model, role, content)
            VALUES (?, ?, ?, ?)""",
            (provider, model, role, content)
        )
        self.conn.commit()

    def save_usage(self, provider, model,
                   input_tokens, output_tokens, cost):
        self.conn.execute(
            """INSERT INTO usage
            (provider, model, input_tokens,
             output_tokens, estimated_cost)
            VALUES (?, ?, ?, ?, ?)""",
            (provider, model, input_tokens,
             output_tokens, cost)
        )
        self.conn.commit()