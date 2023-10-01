from fastapi import FastAPI, HTTPException, status
from app.todo import Todo
app = FastAPI()

todos = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/todolist")
async def get_todolist():
    return {"todos": todos}

@app.get("/todolist/{todo_id}")
async def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {  }

@app.post("/todolist", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "todo has been created successfully"}

@app.put("/todolist/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(todo_id: int, new_todo: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo = new_todo
            todo.id = todo_id
            return {"message": "todo has been updated successfully"}
    return {  }
    

@app.delete("/todolist/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
           todos.remove(todo)
           return {"message: todo has been deleted successfully"}
    