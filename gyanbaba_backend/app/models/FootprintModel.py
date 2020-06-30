from . import db
from .UserModel import *
from .ResourceModel import *

class Footprint(db.Model):
    __table_name__='footprint'
    id=db.Column(db.Integer,primary_key=True)
    resource_id=db.Column(db.Integer,db.ForeignKey('resource.id'))
    user_id=db.Column(db.String(100))
    up_votes=db.Column(db.Integer,default=0)
    down_votes=db.Column(db.Integer,default=0)