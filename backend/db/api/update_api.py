import sqlite3
from flask import Blueprint, request, jsonify

# Create a Blueprint for the update API
update_api = Blueprint("update_api", __name__)

@update_api.route("/api/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.get_json()
    title = data.get("title")
    completed = data.get("completed", False)

    connection = sqlite3.connect("db/todo.db")
    cursor = connection.cursor()

    if title is not None:
        cursor.execute("UPDATE todos SET title = ? WHERE id = ?", (title, todo_id))

    cursor.execute("UPDATE todos SET completed = ? WHERE id = ?", (completed, todo_id))
    connection.commit()
    connection.close()

    return jsonify({"message": f"Todo with ID {todo_id} updated successfully"})
