# Contest App using Python Django

This project is a web-based **Contest App** built using **Python** and **Django**. The app allows students to view problems, submit their solutions, and view all submissions. 
The app allow teachers to create problem, approve student's solutions etc.

It is designed to be simple, easy to understand, and extendable for other features or use cases.

However, I did not focus on front-end. I will design a better user-friendly interface latter.

### You may visit my [Portfolio](https://montasirfahim.github.io/Portfolio/) website to explore my all projects and know more about me in one place 

---
## Features
- User authentication (login, registration).
- Creation and management of problems and submissions.
- Submission of contest solutions.
- Problems and Submissions List.
- Easy to extend and modify.

---
## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python** 3.1 or later.
- **Django** 3.1 or later.
- **Database**: SQLite (default) or any other database (can be configured in `settings.py`).
- **Git** to clone the repository.

---
## Getting Started

### Step 1: Clone the Repository

Start by cloning the repository to your local machine.

```bash
git clone https://github.com/montasirfahim/Contest-App-using-Python-Django.git
cd Contest-App-using-Python-Django
```
### Step 2: Create and Activate a Virtual Environment with pipenv 
```bash
pip install pipenv
pipenv shell
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Run Database Migrations
```bash
python manage.py migrate
```
### Step 5: Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server
After running server, the app will be available at http://127.0.0.1:8000/ in your web browser.
```bash
python manage.py runserver
```
### Step 7: Access the Admin Panel (Optional)
http://127.0.0.1:8000/admin/
