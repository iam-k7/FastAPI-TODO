# 🧾 FastAPI TODO

A simple and easy **Todo API** built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.  
This project is made for learning CRUD operations (Create, Read, Update, Delete) in FastAPI step by step.

---

## 📂 Project Structure
    ```bash
    FastAPI-TODO/
    │
    ├── main.py          → Runs the FastAPI app (main file)
    ├── database.py      → Database connection setup
    ├── models.py        → Defines Todo table (database model)
    ├── schemas.py       → Defines request & response models
    ├── crud.py          → Handles Create, Read, Update, Delete functions
    ├── requirements.txt → All required Python packages
    ├── README.md        → Project details and setup guide
    └── __pycache__/     → Auto-created by Python (ignore)

---

## 🚀 Features
- Add new todos  
- Get all todos or a single todo  
- Update existing todos  
- Delete todos  
- PostgreSQL database with SQLAlchemy ORM  
- Interactive API docs using Swagger UI

---

## 🛠️ Tech Used
**FastAPI**, **Python 3.13**, **SQLAlchemy**, **Pydantic**, **PostgreSQL**, **Uvicorn**

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/iam-k7/FastAPI-TODO.git
   cd FastAPI-TODO

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # for Windows
   source venv/bin/activate   # for macOS/Linux

3. **requirements.txt**
   ```bash
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   psycopg2-binary

4. **How to Run**
   ```bash
   uvicorn main:app --reload

