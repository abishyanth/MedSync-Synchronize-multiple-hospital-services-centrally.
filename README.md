# MedSync 🏥  
_MedSync - Synchronize multiple hospital services centrally_

A Django-based, multi-hospital management system with role-based access—allowing admin, doctor, and patient users to manage hospitals, departments, doctors, and patients from a unified platform.

---

## 🧾 Features  
- 🔐 Role-based permissions: **Superuser**, **Doctor**, **Patient**  
- 🏥 Central access to **multiple hospitals** in one interface  
- 🧑‍⚕️ Departments & Doctors assignment by hospital  
- 👤 Patient registration, profiles, and doctor assignment  
- ✅ Confirm/remove patient status management  
- 🖥️ Modern UI with Bootstrap 5, responsive card-based forms  

---

## 📦 Tech Stack  
- **Backend**: Python 3.11+, Django 4.x  
- **Frontend**: Bootstrap 5, Font Awesome  
- **Database**: SQLite (default; PostgreSQL/MySQL supported)  
- **Forms**: Django Forms and crispy forms (optional)  

---

## 🚀 Installation Guide

```bash
# Clone repository
git clone https://github.com/abishyanth/MedSync.git
cd MedSync

# Set up virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Launch development server
python manage.py runserver
