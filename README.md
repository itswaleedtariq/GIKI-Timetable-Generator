# GIKI-Timetable-Generator
# 📅 GIKI Timetable Generator

A Django-based web application that automatically generates an optimized university timetable system using constraint-based scheduling. The system helps efficiently allocate courses, teachers, and time slots while avoiding clashes.

🌐 Live Demo: https://giki-timetable-generator-2.onrender.com/

---

## 🚀 Features

- Automatic timetable generation
- Conflict-free scheduling (teachers, rooms, courses)
- Admin panel for data management
- Dynamic timetable view
- Django-based backend architecture
- Responsive web interface

---

## 🛠️ Tech Stack

- Python
- Django
- HTML / CSS / JavaScript
- SQLite (default database)
- Gunicorn (deployment server)

---

## 📂 Project Structure
timetable_project/
│
├── timetable_project/ # Main project settings
├── app/ # Core scheduling app
├── templates/ # HTML templates
├── static/ # CSS/JS files
├── db.sqlite3 # Database
├── manage.py


---

## ⚙️ Installation (Local Setup)

### 1. Clone Repository
```bash
git clone https://github.com/itswaleedtariq/GIKI-Timetable-Generator.git
cd GIKI-Timetable-Generator

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

🌍 Deployment

This project is deployed on Render:

Hosting Platform: Render
WSGI Server: Gunicorn
Static Files: WhiteNoise

Live URL:
👉 https://giki-timetable-generator-2.onrender.com/

📌 How It Works
Admin enters:
Courses
Teachers
Classes
Time slots
System processes constraints
Generates optimized timetable automatically
🧠 Future Improvements
AI-based optimization improvements
Better UI/UX design
PostgreSQL integration
Multi-department support
👨‍💻 Author
Waleed Tariq
Software Engineering Student @ GIKI
⭐ Support

If you like this project, give it a ⭐ on GitHub!


---

# 🔥 What I improved for you
- Added **live deployment link**
- Clean professional structure
- Proper Django project format (like real GitHub repos)
- Recruiter-friendly wording
- Deployment section included (important for CV)

---

# 🚀 If you want next upgrade
I can also help you:
- Make it look like a **FAANG-level README**
- Add screenshots section
- Add GIF demo of your timetable system
- Write LinkedIn post for this project
- Improve UI for portfolio

Just tell me 👍
::contentReference[oaicite:0]{index=0}
