from ..models import db
from ..models.ScheduleResourceModel import ScheduleResource 
from  sqlalchemy.sql.expression import func
import random
import datetime



def getschedule(view_id):
    res=ScheduleResource.query.filter(ScheduleResource.view_id==view_id).all()
    # res=db.session.execute('select id from category where title="quote"')
    if res:
        for a in res:
            temp_dict ={}
            temp_dict["view_id"]=str(a.view_id)
            temp_dict["date_sched"]=str(a.data_sched)
            temp_dict["date_end"]=str(a.data_end)
            temp_dict["hours"]=str(a.hours)
            temp_dict["minutes"]=str(a.minutes)
            temp_dict["flag"]='true'
            break

        return temp_dict
    else:
        temp_dict={}
        temp_dict["flag"]='false'
        return temp_dict

    # res1=db.session.execute('''select id from user where user_channel_id="%s"'''%channel_id)
    # for a in res1:
    #     user_id=a[0]
    #     break   
def addschedule(view_id,col_name,col_val):
    
    res=ScheduleResource.query.filter_by(view_id=view_id).first()
    if res:
        if col_name =="date_sched":
            res.data_sched=col_val
        elif col_name =="date_end":
            res.data_end=col_val
        elif col_name =="hours":
            res.hours=col_val
        elif col_name =="minutes":
            res.minutes=col_val
        
        db.session.commit()
        
        return True
    else:
        if col_name =="date_sched":
            sch=ScheduleResource(view_id=view_id,data_sched=col_val)
        elif col_name =="date_end":
            sch=ScheduleResource(view_id=view_id,data_end=col_val)
        elif col_name =="hours":
            sch=ScheduleResource(view_id=view_id,hours=col_val)
        elif col_name =="minutes":
            sch=ScheduleResource(view_id=view_id,minutes=col_val)
        
        db.session.add(sch)
        db.session.commit()