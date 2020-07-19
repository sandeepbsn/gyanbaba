from . import db
from .CategoryModel import *


class Resource(db.Model):
    __table_name__='resource'
    id=db.Column(db.Integer,primary_key=True)
    # title=db.Column(db.String(255),unique=True)
    cat_id=db.Column(db.Integer,db.ForeignKey('category.id'))
    payload=db.Column(db.JSON)
    up_votes=db.Column(db.Integer,default=0)
    down_votes= db.Column(db.Integer,default=0)
    

