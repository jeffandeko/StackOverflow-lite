# Model for questions and answers
from datetime import datetime

from app.instances import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, question, post_date=None):
        self.title = title
        self.body = body
        if post_date is None:
            post_date = datetime.utcnow()
        self.pub_date = post_date
        self.question = question

    def __repr__(self):
        return '<Questions %r>' % self.title


class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Answers %r>' % self.name
