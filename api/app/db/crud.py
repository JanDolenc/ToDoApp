from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import delete
from db import models, schemas


# Enter new todo into the database - click on plus btn
def create_todo_db(todo_create: schemas.TodoCreate, db: Session):
    dt_ts = datetime.fromtimestamp(todo_create.time_created) # Convert ts (int) to ts (date format)
    
    todos = models.Todo() # models.py model 
    todos.value = todo_create.value # insert into todos.value data from the api
    todos.time_created = dt_ts
    #todos.due_time = todo_create.due_time

    db.add(todos)
    db.commit()


# Mark todo as completed - click on checkmark 
def make_todo_completed_db(compl_todo_id: int, db: Session):
    todos = models.Todo()
    
    completed_todo = db.query(models.Todo).filter(models.Todo.id == compl_todo_id).first()
    #completed_todo = db.query(todos).filter(todos.id == compl_todo_id).first()
    
    if completed_todo.status == False:
        completed_todo.status = True
    else:
         completed_todo.status = False

   # db.add(completed_todo)
    db.commit()
    #db.refresh()


    return {"compl_todo_id:": completed_todo.id, "status:": completed_todo.status}


# Delete todo from database - click on trash can
def delete_todo_db(del_todo_id: int, db: Session):
    delete_todo = db.query(models.Todo).filter(models.Todo.id == del_todo_id).first()

    db.delete(delete_todo)
    db.commit()

    return {"del_todo_id:": delete_todo.id, "value:": delete_todo.value}


# Retrieve all records from the database - on load
def get_todo_all_db(db: Session):
    all_todos = db.query(models.Todo).all()
    return all_todos