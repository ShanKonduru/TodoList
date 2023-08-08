import sqlite3
from flask import Flask, request, jsonify
from db.api.add_api import add_api
from db.api.delete_api import delete_api
from db.api.update_api import update_api
from db.api.list_api import list_api

app = Flask(__name__)

# Database setup
DB_PATH = "data/todo.db"

def create_todo_table():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
        """
    )
    connection.commit()
    connection.close()

# Initialize the database table
create_todo_table()

# Register API Blueprints
app.register_blueprint(add_api)
app.register_blueprint(delete_api)
app.register_blueprint(update_api)
app.register_blueprint(list_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
