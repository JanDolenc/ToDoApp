from db import models, schemas, crud
from typing import List
from fastapi import FastAPI, Depends
from db.database import SessionLocal, engine
from sqlalchemy.orm import Session


# Create all sql tables (empty) if they don't exist
models.Base.metadata.create_all(bind=engine) 

app = FastAPI()


# Dependency - chechk if we have connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Retrieve all records - on load
@app.get("/todo/all", response_model=List[schemas.Todo])
def get_todo_all(db: Session = Depends(get_db)):
    return crud.get_todo_all_db(db=db)


# Enter new todo into the database
@app.post("/add/todo", response_model=schemas.TodoCreate)
def create_todo(todo_create: schemas.TodoCreate, db: Session = Depends(get_db)): # function arguments | validate data | before this exec. check if we have connection to db
    return crud.create_todo_db(todo_create, db=db)


# Mark todo as completed
@app.post("/todo/completed/{compl_todo_id}")
def make_todo_completed(compl_todo_id: int, db: Session = Depends(get_db)):
    return crud.make_todo_completed_db(compl_todo_id, db=db)


# Delete todo from database    
@app.delete("/delete/todo/{del_todo_id}")
def delete_todo(del_todo_id: int, db: Session = Depends(get_db)):
    return crud.delete_todo_db(del_todo_id, db=db)