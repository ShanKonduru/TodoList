const todoList = document.getElementById("todoList");
const todoInput = document.getElementById("todoInput");

function addTodo() {
  const todoText = todoInput.value.trim();
  if (todoText !== "") {
    const li = document.createElement("li");
    li.innerHTML = `
      <span>${todoText}</span>
      <div class="actions">
        <button onclick="deleteTodo(this)">Delete</button>
      </div>
    `;
    todoList.appendChild(li);
    todoInput.value = "";
  }
}

function deleteTodo(button) {
  const li = button.closest("li");
  li.remove();
}
