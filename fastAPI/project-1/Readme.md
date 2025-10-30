# ⚡ FastAPI Backend Project — Technical Portfolio

This project is a **FastAPI-based backend application** developed as part of my **technical portfolio** to demonstrate backend development skills with modern Python frameworks and clean architecture principles.

It includes complete CRUD operations, database integration using SQLAlchemy ORM, modular routing, and a well-structured codebase suitable for scaling into a full application.

---

## 🧠 Purpose

This repository is built to:
- Showcase proficiency with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**
- Demonstrate understanding of **RESTful API design**
- Display clean and modular code structure for backend systems
- Serve as a foundation for more advanced projects (authentication, JWT, etc.)

---

## 🚀 Features

- **FastAPI Framework** — modern async web framework  
- **SQLAlchemy ORM** — relational database modeling  
- **PostgreSQL Integration**  
- **Pydantic Models (v2)** for request & response validation  
- **Modular Routers** for products, categories, users, and orders  
- **Automatic DB Initialization** with dummy data  
- **Ready for Authentication Extension (JWT)**

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Language | Python 3.11 |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL |
| Validation | Pydantic v2 |
| Environment | Virtualenv |
| Auth (Planned) | JWT Tokens |

## 📁 Project Structure

```bash
project-1/
│
├── main.py                  # Application entry point
├── database.py              # DB engine and session config
├── data/                    # Initial dummy data
├── models/                  # SQLAlchemy ORM models
│   ├── products.py
│   ├── category.py
│   └── user.py
├── schemas/                 # Pydantic schemas
├── routes/                  # API routes (CRUD)
│   ├── product_routes.py
│   ├── category_routes.py
│   ├── user_router.py
│   └── order_routes.py
├── utils/                   # Utility functions
│   ├── hashing.py           # Password hashing utilities
│   └── token.py             # JWT token generation and verification
└── requirements.txt

```

## ⚙️ Quick Start

1. **Clone the repository**  
   `git clone https://github.com/mjangali94/tech-interview-portfolio.git`  
   `cd fastAPI/project-1`

2. **Create & activate virtualenv**  
   `python3 -m venv .venv`  
   `source .venv/bin/activate`

3**Configure DB**  
   Edit `database.py` and set your `DATABASE_URL`, e.g.:  
   `DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/postgres"`

5. **Run server**  
   `fastapi dev`  
   Open:  
   - Swagger UI → `http://127.0.0.1:8000/docs`  
   - ReDoc → `http://127.0.0.1:8000/redoc`



These interfaces allow you to interact with all available CRUD routes for:

- Products (`/products`)  
- Categories (`/categories`)  
- Users (`/users`)  
- Orders (`/orders`)  

---

## 📌 Notes

- The project initializes the database with **dummy product data** automatically on first run.  
- You can **extend authentication** using JWT tokens in the `user_router` module.  
- The modular router design allows easy **extension of features** like analytics, reporting, or additional resources.  
- Use a **virtual environment** to avoid dependency conflicts.  

---

## 📚 Further Improvements / Future Work

- Add **role-based access control**  
- Implement **pagination, filtering, and search** for API endpoints  
- Add **unit tests and integration tests** using Pytest  
- Containerize the application using **Docker** for deployment  

---

## 💻 Contact / Profile

This project is part of my **technical portfolio**.  
Feel free to explore the code and connect with me for any questions or collaborations.

