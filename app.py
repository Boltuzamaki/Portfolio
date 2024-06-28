from flask import Flask, render_template, redirect, url_for, request
from database import create_app
from database.db import (
    db,
    Experience,
    Education,
    Portfolio,
    ResumeEducation,
    ResumeExperience,
)
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
    UserMixin,
)
from werkzeug.security import check_password_hash
from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
SECRET_KEY = os.environ.get("SECRET_KEY")
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME")
ADMIN_PASSWORD_HASH = os.environ.get("ADMIN_PASSWORD_HASH")

app = create_app(
    database_uri=SQLALCHEMY_DATABASE_URI,
    track_modifications=SQLALCHEMY_TRACK_MODIFICATIONS,
    secret_key=SECRET_KEY,
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin):
    id = "admin"


@login_manager.user_loader
def load_user(user_id):
    if user_id == "admin":
        return User()
    return None


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login"))


class AuthenticatedAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login"))


admin = Admin(
    app,
    name="Admin Panel",
    template_mode="bootstrap3",
    index_view=AuthenticatedAdminIndexView(),
)
admin.add_view(AuthenticatedModelView(Experience, db.session))
admin.add_view(AuthenticatedModelView(Education, db.session))
admin.add_view(AuthenticatedModelView(Portfolio, db.session))
admin.add_view(AuthenticatedModelView(ResumeEducation, db.session))
admin.add_view(AuthenticatedModelView(ResumeExperience, db.session))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(password, "===========>")
        print(ADMIN_PASSWORD_HASH, "============>")
        print(check_password_hash(ADMIN_PASSWORD_HASH, password), "================>")
        if username == ADMIN_USERNAME and check_password_hash(
            ADMIN_PASSWORD_HASH, password
        ):
            login_user(User())
            return redirect(url_for("admin.index"))
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/")
def index():
    experiences = Experience.query.all()
    education = Education.query.all()
    portfolio = Portfolio.query.all()
    resume_education = ResumeEducation.query.all()
    resume_experience = ResumeExperience.query.all()

    resume = {
        "education": resume_education,
        "experience": resume_experience,
    }

    return render_template(
        "index.html",
        experiences=experiences,
        education=education,
        portfolio=portfolio,
        resume=resume,
    )


if __name__ == "__main__":
    app.run(debug=True)
