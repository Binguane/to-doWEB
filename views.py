from app import app
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from models import User, Task
from db import db

@app.route("/")
@login_required
def home_page():
    tasks = db.session.query(Task).all()
    return render_template("home.html", tasks=tasks)


@app.route("/profile/<username>")
@login_required
def profile_page(username):
    return render_template("profile.html")


@app.route("/form")
def form_page():
    return render_template("form.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    if not email or not email or not password:
        flash("Please fill out all fields!", "error")
        return redirect(url_for("form_page"))
        
    user = db.session.query(User).filter_by(email=email, password=password).first()

    if not user:
        flash("Enter your credentials correctly!", "error")
        return redirect(url_for('form_page'))
    
    login_user(user)
    return redirect(url_for("home_page"))

@app.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    if not username or not email or not password:
        flash("Please fill out all fields!" "error")
        return redirect(url_for("form_page"))

    existing_user = db.session.query(User).filter_by(email=email).first()

    if existing_user:
        flash("User already exists!", "error")
        return redirect(url_for("form_page"))

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)

    return redirect( url_for("home_page"))

    
@app.route("/logout", methods=["POST", "GET"])
@login_required
def logout():
    logout_user()

    return redirect(url_for("form_page"))


@app.route("/tasks", methods=["POST", "GET"])
@login_required
def tasks():
    data = request.get_json()
    task_text = data["taskText"]
    print(task_text)

    task = Task(task=task_text)
    db.session.add(task)
    db.session.commit()

    flash("Task added succesfuly!", "success")
    return redirect(url_for("home_page"))


@app.route("/edit_task/<int:task_id>", methods=["POST"])
@login_required
def edit_task(task_id):
    data = request.get_json()
    content = data.get("content")
    
    task = db.session.query(Task).filter_by(id=task_id).first()
    task.task = content
    db.session.commit()

    return redirect(url_for("home_page"))


@app.route("/delete_task/<int:task_id>", methods=["POST"])
@login_required
def delete_task(task_id):
    task = db.session.query(Task).filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("home_page"))
