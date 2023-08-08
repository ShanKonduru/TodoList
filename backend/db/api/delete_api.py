import sqlite3
from flask import Blueprint, jsonify

# Create a Blueprint for the delete API
delete_api = Blueprint("delete_api", __name__)

@delete_api.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    connection = sqlite3.connect("db/todo.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    connection.commit()
    connection.close()

    return jsonify({"message": f"Todo with ID {todo_id} deleted successfully"})
