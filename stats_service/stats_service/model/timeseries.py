from sqlalchemy import func
from stats_service.db import db


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

    @classmethod
    def calculate_sum_by_time_range(cls, from_, to):
        return (
            cls.query.with_entities(func.sum(cls.v).label("sum"))
            .filter(cls.t >= from_, cls.t <= to)
            .first()
        )

    @classmethod
    def calculate_avg_by_time_range(cls, from_, to):
        return (
            cls.query.with_entities(func.avg(cls.v).label("average"))
            .filter(cls.t >= from_, cls.t <= to)
            .first()
        )
