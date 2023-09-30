from fastapi import FastAPI, HTTPException, status
from app.todo import Todo
app = FastAPI()

todos = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/todolist")
async def get_todolist():
    return {"todos": todos}, status.HTTP_200_OK

@app.get("/todolist/{todo_id}")
async def get_todo_by_id():
    for todo in todos:
        if todo.id == id:
            return {"todo": todo}, status.HTTP_200_OK
    return {  }

@app.post("/todolist")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "todo was created successfully"}, status.HTTP_201_CREATED

@app.put("/todolist/{todo_id}")
async def update_todo():
    for todo in todos:
        if todo.id == id:
            return {"todo": todo}, status.HTTP_204_NO_CONTENT
    return {  }
    

@app.get("/todolist/{todo_id}")
async def delete_todo():
    return {"message: tpdo deleted"}