from sqlalchemy import Boolean, Column, Integer, String 
from sqlalchemy.sql.sqltypes import TIMESTAMP

from db.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(255))
    time_created = Column(TIMESTAMP)
    due_time = Column(TIMESTAMP)
    status = Column(Boolean, default=False)
