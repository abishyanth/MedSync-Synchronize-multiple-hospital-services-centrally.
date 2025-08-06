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
# user name: Hadmin
# password: hospital
python manage.py createsuperuser

# Launch development server
python manage.py runserver


🧭 Usage
Superuser: Add hospitals, departments, doctors, and patients. Manage all assignments.

Doctor: Log in to view and add patients in your assigned department.

Patient: Log in to fill profile and book appointments; see your doctor’s list.

🔖 URL Structure Overview
/
📂 hospital/
   ├── /                   → Dashboard (hospital list)
   ├── /<id>/             → Hospital Detail
   ├── /<id>/doctors/     → Doctor list by hospital
   ├── /<id>/patients/    → Patient list by hospital
   ├── /add_department/   → Add new department
   └── /add_doctor/       → Add new doctor
/auth/
   ├── signup             → Role-based registration (admin/doctor/patient)
   ├── login
   └── logout


🏗 Folder Structure
MedSync/
├── hospital/         # Main Django app
├── authentication/   # Authentication & signup/login , contains app level template and static
├── hms_project/      # Django settings & core , contains app level template and static
├── manage.py
└── requirements.txt

🙏 Acknowledgements
Inspired by GitDocify README aesthetics and modular template structure.
Built with love using Django and Bootstrap.

💬 Contact
Abishyanth S
✉️ abishyanth14@gmail.com
🔗 LinkedIn : https://www.linkedin.com/in/kartik-d-k-470942153/
