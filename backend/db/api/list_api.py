import sqlite3
from flask import Blueprint, jsonify

# Create a Blueprint for the list API
list_api = Blueprint("list_api", __name__)

@list_api.route("/api/todos", methods=["GET"])
def get_todos():
    connection = sqlite3.connect("db/todo.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    connection.close()

    todos_list = []
    for todo in todos:
        todo_dict = {
            "id": todo[0],
            "title": todo[1],
            "completed": bool(todo[2])
        }
        todos_list.append(todo_dict)

    return jsonify(todos_list)
