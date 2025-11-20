from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/user/<name>")
def profile_page(name):
    return render_template("profile.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
