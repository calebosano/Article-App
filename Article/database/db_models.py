from database import db

from datetime import datetime


# Creating the users DB model

class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email= db.Column(db.String(120), nullable=False)
    phone= db.Column(db.Integer, nullable=False)
    admin = db.Column(db.Boolean)

    articles_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    article = db.relationship('Articles', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<Post %r>' % self.firstname


# Creating the users DB model

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.title
