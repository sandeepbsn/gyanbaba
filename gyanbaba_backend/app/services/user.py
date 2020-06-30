from ..models import db
from ..models.UserModel import User 
# import random


def load_user():

    usr1=User(name="Abhishek",user_channel_id="X12KS")
    db.session.add(usr1)  
    usr2=User(name="Shivam",user_channel_id="XY46BD")
    db.session.add(usr2)    
    usr3=User(name="Sandeep",user_channel_id="MKJJSDI87")
    db.session.add(usr3)

    db.session.commit()    
  


    return {'loaded users'}


    
