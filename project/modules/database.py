import sqlite3
import json

# Connect to the database
def get_cursor_and_connection():
    conn = sqlite3.connect("documents.db")
    c = conn.cursor()
    return c, conn

# create the table if not exists
c, conn = get_cursor_and_connection()
c.execute('''CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY,
                type TEXT NOT NULL,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                tags TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()

def execute_sql(c: sqlite3.Cursor, conn: sqlite3.Connection, sql_command: str):
    output = ""

    if sql_command.startswith("INSERT") or sql_command.startswith("UPDATE") or sql_command.startswith("DELETE"):
        try:
            sql_command = sql_command.replace('"', "'")
            c.execute(sql_command)
            conn.commit()
            output = "The operation was successfully executed."
        except sqlite3.Error as e:
            output = f"An error occurred: {e}"
    elif sql_command.startswith("SELECT"):
        try:
            sql_command = sql_command.replace('"', "'")
            c.execute(sql_command)
            rows = c.fetchall()
            formatted_rows = []
            for row in rows:
                formatted_row = {
                    "id": row[0],
                    "type": row[1],
                    "title": row[2],
                    "content": row[3],
                    "tags": row[4],
                    "timestamp": row[5]
                }
                formatted_rows.append(formatted_row)
            output = json.dumps(formatted_rows, indent=4) #output as json.
        except sqlite3.Error as e:
            output = f"An error occurred: {e}"
    else:
        output = "Invalid SQL command. Please try again."

    return output