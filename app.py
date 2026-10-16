
from flask import Flask, render_template, request, redirect, url_for, flash
import re

from database import (
    initialize_db,
    get_all_students,
    get_student,
    add_student,
    update_student,
    delete_student,
    get_total_students,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "local-development-key"

initialize_db()


def validate_student(form):
    name = form.get("name", "").strip()
    age_text = form.get("age", "").strip()
    course = form.get("course", "").strip()
    email = form.get("email", "").strip()

    if not all([name, age_text, course, email]):
        return None, "Please fill in all fields."

    try:
        age = int(age_text)
    except ValueError:
        return None, "Age must be a whole number."

    if not 1 <= age <= 120:
        return None, "Age must be between 1 and 120."

    if len(name) > 100 or len(course) > 100 or len(email) > 150:
        return None, "One or more fields are too long."

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return None, "Please enter a valid email address."

    return {
        "name": name,
        "age": age,
        "course": course,
        "email": email,
    }, None


@app.route("/")
def index():
    return render_template(
        "index.html",
        students=get_all_students()[:5],
        total=get_total_students(),
    )


@app.route("/students")
def students():
    search = request.args.get("search", "").strip()
    return render_template(
        "students.html",
        students=get_all_students(search),
        search=search,
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        student, error = validate_student(request.form)

        if error:
            flash(error, "error")
            return render_template("add_student.html")

        add_student(**student)
        flash("Student added successfully!", "success")
        return redirect(url_for("students"))

    return render_template("add_student.html")


@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit(student_id):
    record = get_student(student_id)

    if record is None:
        flash("Student not found.", "error")
        return redirect(url_for("students"))

    if request.method == "POST":
        student, error = validate_student(request.form)

        if error:
            flash(error, "error")
            return render_template("edit_student.html", student=record)

        update_student(student_id, **student)
        flash("Student updated successfully!", "success")
        return redirect(url_for("students"))

    return render_template("edit_student.html", student=record)


@app.route("/delete/<int:student_id>", methods=["POST"])
def delete(student_id):
    if get_student(student_id) is None:
        flash("Student not found.", "error")
    else:
        delete_student(student_id)
        flash("Student deleted successfully!", "success")

    return redirect(url_for("students"))


if __name__ == "__main__":
    app.run(debug=True)
