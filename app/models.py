from app import db, app

from flask_sqlalchemy import SQLAlchemy

import datetime


class RoleConst:
    USER = 0b00000001


def create_tables():
    with app.app_context():
        db.create_all()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)
    phone_id = db.Column(db.Integer, db.ForeignKey('phone.id'), nullable=False)
    crypto_id = db.Column(db.Integer, db.ForeignKey('crypto.id'))
    meta_id = db.Column(db.Integer, db.ForeignKey('meta.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), default=RoleConst.USER)

    member_dlg = db.relationship("MemberDialog", backref="user", uselist=False)
    auth = db.relationship("Auth", backref="auth_info", uselist=False)
    message = db.relationship("Message", backref="user", uselist=False)


class Dialog(db.Model):
    __tablename__ = "dialog"
    id = db.Column(db.Integer, primary_key=True)
    date_create = db.Column(db.DateTime, default=datetime.datetime.now)
    date_delete = db.Column(db.DateTime, nullable=True)
    mem_dlg = db.relationship("MemberDialog", "members")
    message = db.relationship("Message", backref="dlg", uselist=False)


class MemberDialog(db.Model):  # OK 100%
    __tablename__ = "member_dialog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    dialog_id = db.Column(db.Integer, db.ForeignKey("dialog.id"), nullable=False)


class Meta(db.Model): # OK 100%
    __tablename__ = "meta"
    id = db.Column(db.Integer, primary_key=True)
    about_user = db.Column(db.String(500))
    icon = db.Column(db.String(200))
    name = db.Column(db.String(80))
    surname = db.Column(db.String(100))
    state_private_profile = db.Column(db.Boolean, default=False)
    user = db.relationship("User", backref="meta", uselist=False)


class Phone(db.Model):  # ok 100%
    __tablename__ = "phone"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(15), nullable=False)
    state_accept = db.Column(db.Boolean, default=False)
    user = db.relationship("User", backref="phone", uselist=False)


class Role(db.Model): # OK 100%
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    privellage = db.Column(db.Integer)
    name_role = db.Column(db.String(30))
    user = db.relationship("User", backref="role", uselist=False)


class Auth(db.Model):  # OK 100%
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(36), nullable=False)
    state = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class HistoryTransaction(db.Model): #  OK 100%
    __tablename__ = "history_transaction"
    id = db.Column(db.Integer, primary_key=True)
    from_wallet_id = db.Column(db.Integer, db.ForeignKey("crypto.id"))
    to_wallet_id = db.Column(db.Integer, db.ForeignKey("crypto.id"))
    count = db.Column(db.Float)
    state = db.Column(db.Boolean)


class Crypto(db.Model): # OK 100%
    __tablename__ = "crypto"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(80))
    count_token = db.Column(db.Float, default=0)
    his_transaction = db.relationship("HistoryTransaction", backref="crypto_wallet")
    user = db.relationship("User", backref="crypto_wallet", uselist=False)


# class PathFiles(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     path = db.Column(db.String(60))

class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500))
    state_message = db.Column(db.Integer, db.ForeignKey("state_message.id"))
    # path_files_id
    sender_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    dialog_id = db.Column(db.Integer, db.ForeignKey("dialog.id"))


class StateMessage(db.Model):
    __tablename__ = "state_message"
    id = db.Column(db.Integer, primary_key=True)
    message = db.relationship("Message", backref="state_message", uselist=False)
    isRead = db.Column(db.Boolean, default=False)
    isGetByUser = db.Column(db.Boolean, default=False)
    isDelete = db.Column(db.Boolean, default=False)
