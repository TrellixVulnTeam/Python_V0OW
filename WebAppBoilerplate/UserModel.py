from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from appConfig import *

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'usercompany'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80),nullable = False)
    age = db.Column(db.Integer,nullable = False)
    company = db.Column(db.String(80))

    def add_user(_name, _age, _company):
        new_user = User(name=_name,age=_age,company=_company)
        db.session.add(new_user)
        db.session.commit()
     
    def get_all_users():
        return db.query.all()

    def __repr__(self):
        user_object = {
            'name' : self.name,
            'age' : self.age,
            'company' : self.company
        }
        return json.dumps(user_object)