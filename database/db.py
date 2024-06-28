from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(50))
    title = db.Column(db.String(100))
    subtitle = db.Column(db.String(100))
    description = db.Column(db.String(200))
    image = db.Column(db.String(200))


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(50))
    title = db.Column(db.String(100))
    subtitle = db.Column(db.String(100))
    description = db.Column(db.String(200))
    image = db.Column(db.String(200))


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(50))
    likes = db.Column(db.Integer)
    title = db.Column(db.String(100))
    image = db.Column(db.String(200))


class ResumeEducation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    institution = db.Column(db.String(100))
    period = db.Column(db.String(50))
    grade = db.Column(db.String(10))
    description = db.Column(db.String(200))


class ResumeExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    institution = db.Column(db.String(100))
    period = db.Column(db.String(50))
    grade = db.Column(db.String(10))
    description = db.Column(db.String(200))
