from db import models, schemas
from fastapi import FastAPI
from db.database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine) # create all sql tables (empty) if they don't exist

app = FastAPI()


#--- FROM HERE CODE NEEDS TO BE MODIFIED TO WORK WITH DATABASE

db = []


@app.get("/")
def read_root():
    return {"Hello": "World"}


# vrne vse zapise iz baze. db se samodejno pretvori v json
@app.get("/todo/all")
def get_todo_all():
    return db


#Z Todo (model) določimo kakpne podatke pričakujemo | What to expect & how to handle it
# preko todo dostopamo do vrednosti določene (shranjenje) v Todo
@app.post("/add/todo")
def create_todo(todo: schemas.Todo):
    db.append(todo.dict())
    return db[-1] #last item in the db


@app.post("/todo/completed/{todo_id}")
def make_todo_completed(todo_id: int):
    for i in db:
        if(i["id"] == todo_id):
            i["status"] = True
            return db[i]


@app.delete("/delete/todo/{todo_id}")
def delete_todo(todo_id: int):
    db.pop(todo_id-1)
    return{}