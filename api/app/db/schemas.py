from typing import List, Optional
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    value: str
    timestamp: float
    status: bool

class TodoCreate(Todo):
    value: str
    timestamp: float
    status: bool