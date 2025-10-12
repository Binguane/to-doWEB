from flask import Flask
from db import db
from models import User
from flask_login import LoginManager, login_user


app = Flask(__name__)
app.secret_key = "1234"
app.config["SQLALCHEMY_DATABASE_URI"]  = "sqlite:///data.db"
db.init_app(app)
login_maneger = LoginManager(app)
login_maneger.login_view = "form_page"

from views import *

@login_maneger.user_loader
def user_loader(id):
   user = db.session.query(User).filter_by(id=id).first()
   return user



if __name__ == "__main__":
    with app.app_context():
       db.create_all()
    app.run(debug=True)
