from . import db


class ScheduleResource(db.Model):
    __table_name__='scheduleresource'
    id=db.Column(db.Integer,primary_key=True)
    view_id=db.Column(db.String(255),unique=True)
    data_sched=db.Column(db.String(255))
    data_end=db.Column(db.String(255))
    hours=db.Column(db.String(255))
    minutes=db.Column(db.String(255))
    