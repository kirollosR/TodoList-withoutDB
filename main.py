from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world!"}

todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get a todo by id
@app.get("/todos/{todo_id}")
async def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message": "Todo not found!"}

# Create a todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been created successfully!",
            "todo": todo}

# Update a todo by id
@app.put("/todos/{todo_id}")
async def update_todo_by_id(todo_id: int, todo: Todo):
    for t in todos:
        if t.id == todo_id:
            t.item = todo.item
            return {"message": "Todo has been updated successfully!",
                    "todo": t}
    return {"message": "Todo not found!"}

# Delete a todo by id
@app.delete("/todos/{todo_id}")
async def delete_todo_by_id(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been deleted successfully!"}
    return {"message": "Todo not found!"}