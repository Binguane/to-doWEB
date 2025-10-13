from app import app
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from models import User, Task
from db import db

@app.route("/")
@login_required
def home_page():
    print(current_user)
    return render_template("home.html")

@app.route("/profile/<username>")
@login_required
def profile_page(username):
    flash("Login succefuly")
    return render_template("profile.html")

@app.route("/form")
def form_page():
    return render_template("form.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = db.session.query(User).filter_by(username=username, password=password).first()

    if user:
        login_user(user)
        return redirect(url_for("home_page"))
    
    
@app.route("/logout", methods=["POST", "GET"])
@login_required
def logout():
    logout_user()
    flash("You've logged out")
    return redirect(url_for("form_page"))

@app.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)

    return redirect(url_for("home_page"))

@app.route("/tasks", methods=["POST", "GET"])
@login_required
def tasks():
    data = request.get_json()
    task_text = data["taskText"]
    print(task_text)

    task = Task(task=task_text)
    db.session.add(task)
    db.session.commit()
    
    return redirect(url_for("home_page"))
