from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# With Pydantic model (schema) we determine what type of data we expect & how to handle it

class TodoCreate(BaseModel):
    value: str
    time_created: datetime
    #due_time: datetime

class Todo(TodoCreate):
    id: int    
    status: bool


    class Config:
        orm_mode = True
