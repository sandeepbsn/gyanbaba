from . import db


class Category(db.Model):
    __table_name__='category'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255),unique=True)
    