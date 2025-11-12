# 🧾 FastAPI TODO

A simple and easy **Todo API** built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.  
This project is made for learning CRUD operations (Create, Read, Update, Delete) in FastAPI step by step.

---

## 📂 Project Structure

FastAPI-TODO/
│
├── main.py                # Entry point - runs the FastAPI app
│
├── database.py            # Database setup (SQLAlchemy + PostgreSQL connection)
│
├── models.py              # SQLAlchemy ORM models (Todo table)
│
├── schemas.py             # Pydantic models (for request/response validation)
│
├── crud.py                # All database operations (create, read, update, delete)
│
├── requirements.txt       # List of dependencies
│
├── README.md              # Project documentation
│
└── __pycache__/           # (auto-created by Python)

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

4.**How to Run**
```bash
   uvicorn main:app --reload

