from . import db


class User(db.Model):
    __table_name__='user'
    id=db.Column(db.Integer,primary_key=True)
    user_channel_id=db.Column(db.String(100),unique=True)
    name=db.Column(db.String(100),nullable=False)
    status=db.Column(db.Boolean,default=False)
    active_time=db.Column(db.DateTime)
    isAdmin=db.Column(db.Boolean,default=False)
