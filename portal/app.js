import { APIURL } from "./configDev.js";

// Selectors
const todoInput = document.querySelector(".todo-input");
const todoButton = document.querySelector(".todo-button");
const todoList = document.querySelector(".todo-list");
const filterOption = document.querySelector(".filter-todo");
const messageBox = document.querySelector(".message-box");

// Event listeners
document.addEventListener("DOMContentLoaded", printAllTodos);
todoButton.addEventListener("click", addTodo);
todoList.addEventListener("click", deleteCheck);
filterOption.addEventListener("click", filterTodo);

// Functions
// Create todo, add it to todo list and save to db
function addTodo(event) {
  // Prevent form from sending
  event.preventDefault();

  // Create new todo div (box) | includes: text, check mark and trash btn
  const todoDiv = document.createElement("div");
  todoDiv.classList.add("todo");

  // Create li and append it to todoDiv
  const newTodo = document.createElement("li");
  newTodo.innerText = todoInput.value;
  newTodo.classList.add("todo-item");
  todoDiv.appendChild(newTodo);

  // Create check mark and trash btn then append it to todoDiv
  const completedButton = document.createElement("button");
  completedButton.innerHTML = '<i class="fas fa-check"></i>';
  completedButton.classList.add("complete-btn");
  todoDiv.appendChild(completedButton);

  const trashButton = document.createElement("button");
  trashButton.innerHTML = '<i class="fas fa-trash"></i>';
  trashButton.classList.add("trash-btn");
  todoDiv.appendChild(trashButton);

  // Add to db
  AddNewTodoDb(todoInput.value)
    .then((data) => {
      todoDiv.id = data.id;

      // Then Append todoDiv (value-text, and buttons) to todo List
      todoList.appendChild(todoDiv);
      // Clear todo input value
      todoInput.value = "";
    })
    .catch((err) => {
      console.error("Error with fetch add todo:", err);
      errorMessage("Your todo can't be added to the database.");
    });
}

const AddNewTodoDb = async (value) => {
  const dateObject = new Date();
  const time_created = dateObject.toISOString().split(".")[0];

  const postData = { value, time_created };
  const response = await fetch(APIURL.addTodo, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(postData),
  });

  return response.json();
};

// Trash, check mark btn click
function deleteCheck(e) {
  const item = e.target;

  // Delete todo
  if (item.classList[0] === "trash-btn") {
    const todo = item.parentElement;

    deleteFromDb(todo.id)
      .then(() => {
        // Animation
        todo.classList.add("fall");
        todo.addEventListener("transitionend", function () {
          todo.remove();
        });
      })
      .catch((err) => {
        console.error("Error with fetch delete todo:", err);
        errorMessage("We have trouble deleting todo from the database.");
      });
  }

  // Mark todo as completed
  if (item.classList[0] === "complete-btn") {
    const todo = item.parentElement;
    makeTodoCompletedDb(todo.id)
      .then(() => {
        todo.classList.toggle("completed");
      })
      .catch((err) => {
        console.error("Error with fetch completed todo:", err);
        errorMessage("Todo can't be marked as completed.");
      });
  }
}

// Delete todo from db
const deleteFromDb = async (del_todo_id) => {
  await fetch(`${APIURL.deleteTodo}${del_todo_id}`, {
    method: "DELETE",
  });
};

// Mark as completed in db
const makeTodoCompletedDb = async (compl_todo_id) => {
  await fetch(`${APIURL.todoCompleted}${compl_todo_id}`, {
    method: "POST",
  });
};

// Retrive all todos from db
const getTodos = async () => {
  const response = await fetch(APIURL.getAllTodos);
  const data = await response.json();

  return data;
};

function printAllTodos() {
  getTodos()
    .then((data) => {
      data.forEach(function (todo) {
        // Create new todo div (box) | includes: text, check mark and trash btn
        const todoDiv = document.createElement("div");
        // Is the todo already completed?
        if (todo.status === true) {
          todoDiv.classList.add("todo", "completed");
        } else {
          todoDiv.classList.add("todo");
        }

        // Create li and append it to todoDiv
        const newTodo = document.createElement("li");
        newTodo.innerText = todo.value;
        newTodo.classList.add("todo-item");
        todoDiv.appendChild(newTodo);

        // Create check mark and trash btn then append it to todoDiv
        const completedButton = document.createElement("button");
        completedButton.innerHTML = '<i class="fas fa-check"></i>';
        completedButton.classList.add("complete-btn");
        todoDiv.appendChild(completedButton);

        const trashButton = document.createElement("button");
        trashButton.innerHTML = '<i class="fas fa-trash"></i>';
        trashButton.classList.add("trash-btn");
        todoDiv.appendChild(trashButton);

        // Then Append todoDiv (value-text, and buttons) to todo List
        todoDiv.id = todo.id;
        todoList.appendChild(todoDiv);
      });
    })
    .catch((err) => {
      console.error("Error with fetch get all todos:", err);
      errorMessage("Can’t connect to the database.");
    });
}

function filterTodo(e) {
  const todos = todoList.childNodes;
  todos.forEach(function (todo) {
    switch (e.target.value) {
      case "all":
        todo.style.display = "flex";
        break;

      case "completed":
        if (todo.classList.contains("completed")) {
          todo.style.display = "flex";
        } else {
          todo.style.display = "none";
        }
        break;

      case "uncompleted":
        if (!todo.classList.contains("completed")) {
          todo.style.display = "flex";
        } else {
          todo.style.display = "none";
        }
        break;

      default:
        break;
    }
  });
}

// Display errors (while connecting to db)
let messageText;
function errorMessage(customMsg) {
  // Is error shown for the first time?
  if (messageText != undefined) {
    messageText.remove();
  }
  // Create message div | add text | unhide and animate | add to html
  messageText = document.createElement("div");
  messageText.classList.add("message-text");

  messageText.innerHTML = `<b>Oops,</b> someting went wrong. <u>${customMsg}</u> Please, <strong>refresh the page</strong> and try again.`;

  messageBox.removeAttribute("hidden");
  messageBox.classList.toggle("pop-up");
  messageBox.appendChild(messageText);

  // Remove the class with the animation
  setTimeout(function () {
    messageBox.classList.toggle("pop-up");
  }, 450);
}
