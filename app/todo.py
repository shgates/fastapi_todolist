import uuid
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    title: str
    description: str | None = None
    priority: bool | None = False
    completed: bool | None = False