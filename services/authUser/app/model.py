from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(UserMixin, db.Model):
    user_id = db.Column(db.String(80), primary_key=True)
    pending_role = db.Column(db.Integer())
    user_role = db.Column(db.Integer())
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    address = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(14), nullable=False)
    reg_date = db.Column(db.DateTime(), nullable=False)

    #
    def get_id(self):
        return str(self.user_id + " " + self.user_role)
