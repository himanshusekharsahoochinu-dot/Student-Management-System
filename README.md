# Student Management System

A simple web-based Student Management System developed using Python, Flask, SQLite, HTML, CSS, and JavaScript.

## About the Project

The Student Management System helps users manage student records through a simple web interface. Users can add, view, search, update, and delete student information.

## Features

- Dashboard with total student count
- Add new student records
- View all student records
- Search students by name, course, or email
- Update student details
- Delete student records with confirmation
- SQLite database for storing student information
- Responsive user interface

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Database:** SQLite
- **Code Editor:** Visual Studio Code

## Project Structure

```text
Student_Management_System/
├── app.py
├── database.py
├── requirements.txt
├── students.db
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_student.html
│   ├── students.html
│   └── edit_student.html
└── static/
    ├── style.css
    └── script.js
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Open the Project Folder

```bash
cd Student_Management_System
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open in Your Browser

Visit:

http://127.0.0.1:5000

## Database

The project uses SQLite to store student records. The `students.db` file is created automatically when it does not exist.

The database stores the following fields:

- Student ID
- Student Name
- Age
- Course
- Email Address

## Future Improvements

- Student login and authentication
- Admin dashboard
- Student profile photos
- Export student records to CSV or Excel
- Pagination for large datasets
- Improved security and form protection

## Learning Objectives

This project demonstrates how to build a web application using Python, Flask, SQLite, HTML, CSS, and JavaScript. It also provides practice with CRUD operations: Create, Read, Update, and Delete.

## Author

**Himanshu Sekhar Sahoo**

## License

This project is intended for educational and learning purposes.
