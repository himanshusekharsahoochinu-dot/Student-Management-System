
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "students.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL CHECK(age > 0),
                course TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)


def get_all_students(search=""):
    with get_connection() as conn:
        return conn.execute("""
            SELECT * FROM students
            WHERE name LIKE ? OR course LIKE ? OR email LIKE ?
            ORDER BY id DESC
        """, (f"%{search}%", f"%{search}%", f"%{search}%")).fetchall()


def get_student(student_id):
    with get_connection() as conn:
        return conn.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        ).fetchone()


def add_student(name, age, course, email):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO students (name, age, course, email)
            VALUES (?, ?, ?, ?)
        """, (name, age, course, email))


def update_student(student_id, name, age, course, email):
    with get_connection() as conn:
        conn.execute("""
            UPDATE students
            SET name = ?, age = ?, course = ?, email = ?
            WHERE id = ?
        """, (name, age, course, email, student_id))


def delete_student(student_id):
    with get_connection() as conn:
        conn.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )


def get_total_students():
    with get_connection() as conn:
        return conn.execute(
            "SELECT COUNT(*) FROM students"
        ).fetchone()[0]
