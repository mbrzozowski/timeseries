from marshmallow import Schema, fields, post_load
from timeseries_service.db import db


class TimeseriesModel(db.Model):
    __tablename__ = "timeseries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    t = db.Column(db.Integer)
    v = db.Column(db.Float(precision=2))

    def __init__(self, name, t, v):
        self.name = name
        self.t = t
        self.v = v

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class TimeseriesSchema(Schema):
    name = fields.Str()
    t = fields.Int()
    v = fields.Float()

    @post_load
    def make_timeseries(self, data, **kwargs):
        return TimeseriesModel(**data).save_to_db()
