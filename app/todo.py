import uuid
from pydantic import BaseModel

class Todo(BaseModel):

    def __init__(self, id: uuid, title: str, description: str, priority: bool = False, completed: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed
