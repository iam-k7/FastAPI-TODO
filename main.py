from fastapi import FastAPI, Depends, HTTPException
from schemas import Todo as Todoschema, TodoCreate
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from models import Todo
Base.metadata.create_all(bind = engine)

app = FastAPI()

# Dependency for DB session 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST - Create TODO
@app.post("/todos", response_model=Todoschema)
def create(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# GET - All Todos
@app.get("/todos", response_model=list[Todoschema])
def read_todos(db: Session= Depends(get_db)):
    return db.query(Todo).all()

# GET - Get single todo
@app.get("/todos/{todo_id}", response_model=Todoschema)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="ID not found")
    return todo

# PUT - Update Todo
@app.put("/todos/{todo_id}", response_model=Todoschema)
def Update_todo(todo_id: int, Update: TodoCreate, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="ID not found")
    for key, value in Update.dict().items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

# DELETE - Delete ID
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="ID not found")
    db.delete(todo)
    db.commit()
    return {"message": " You're ID delete successful"}
