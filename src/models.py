from application import db
import datetime


class RawData(db.Model):

    __tablename__ = 'raw_data'
    __table_args__ = {'extend_existing': True}
    ins_datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow, primary_key=True)
    raw_data = db.Column(db.String(250))