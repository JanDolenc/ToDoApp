from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# With Pydantic model (schema) we determine what type of data we expect & how to handle it

class TodoCreate(BaseModel):
    value: str
    time_created: int
    #due_time: int

class Todo(TodoCreate):
    id: int
    value: str
    time_created: datetime
    
    status: bool


    class Config:
        orm_mode = True





#class Todo(BaseModel):
#    id: int
#    value: str
#    time_created: int
    #due_time: int
#    status: bool

#class TodoCreate(Todo):
    #value: str
    #time_created: int
    #due_time: int
   #status: bool