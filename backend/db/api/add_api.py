import sqlite3
from flask import Blueprint, request, jsonify

# Create a Blueprint for the add API
add_api = Blueprint("add_api", __name__)

@add_api.route("/api/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    title = data.get("title")
    completed = data.get("completed", False)

    if title is None:
        return jsonify({"error": "Todo title missing"}), 400

    connection = sqlite3.connect("db/todo.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO todos (title, completed) VALUES (?, ?)", (title, completed))
    connection.commit()
    connection.close()

    return jsonify({"message": "Todo added successfully"}), 201
