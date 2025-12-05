
This project also uses Postman for API testing and DBeaver for viewing database tables.

---

# 🚀 Features

- Create, Read, Update, Delete (CRUD) TODO items  
- PostgreSQL as the database  
- Uses Django's class-based structure  
- Clean modular architecture  
- API tested via Postman  
- Database tables visible in DBeaver  

---

# 📂 Project Structure

myapp/
│
├── core/ # Django project
│ ├── settings.py
│ ├── urls.py
│ └── views.py (ping endpoint)
│
├── core_app/
│ └── todo/ # TODO application
│ ├── models.py # Model layer
│ ├── views.py # Business logic layer
│ ├── controller.py # HTTP request handlers
│ ├── urls.py # Route definitions
│ ├── migrations/
│ └── ...
│
├── .env # Environment variables (not committed)
├── venv/ # Virtual environment (ignored)
└── README.md


Create & Activate Virtual Environment

python -m venv venv
.\venv\Scripts\activate   # Windows

Start Server
python manage.py runserver
