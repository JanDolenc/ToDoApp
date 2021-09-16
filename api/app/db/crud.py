from sqlalchemy.orm import Session
from db import models, schemas


# Enter new todo into the database - click on plus btn
def create_todo_db(todo_create: schemas.TodoCreate, db: Session):
    todos = models.Todo() # models.py model 
    todos.value = todo_create.value # insert into todos.value data from the api
    todos.time_created = todo_create.time_created
    #todos.due_time = todo_create.due_time

    db.add(todos)
    db.commit()
    db.refresh(todos)

    return todos


# Mark todo as completed - click on checkmark 
def make_todo_completed_db(compl_todo_id: int, db: Session):
    todos = models.Todo
    completed_todo = db.query(todos).filter(todos.id == compl_todo_id).first()
    
    if completed_todo.status == False:
        completed_todo.status = True
    else:
         completed_todo.status = False

    db.commit()
    db.refresh(completed_todo)

    return completed_todo


# Delete todo from database - click on trash can
def delete_todo_db(del_todo_id: int, db: Session):
    todos = models.Todo
    delete_todo = db.query(todos).filter(todos.id == del_todo_id).first()

    db.delete(delete_todo)
    db.commit()

    return delete_todo


# Retrieve all records from the database - on load
def get_all_todos_db(db: Session):
    todos = models.Todo
    all_todos = db.query(todos).all()
    return all_todos
