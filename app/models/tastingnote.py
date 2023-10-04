from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class TastingNote(db.Model):
    __tablename__ = 'tasting_notes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id"), ondelete="CASCADE"), nullable=False)
    tea_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("teas.id"), ondelete="CASCADE"), nullable=False)
    note = db.Column(db.String)
    score = db.Column(db.Integer, default=50)
    # tea_amount = db.Column(db.Integer)
    # water_amount = db.Column(db.Integer)
    # steep_time = db.Column(db.String)
    # temperature = db.Column(db.String)
    flavors = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    #relationships
    user = db.relationship("User", back_populates="tasting_notes")
    tea = db.relationship("Tea", back_populates="tasting_notes")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'tea_id': self.tea_id,
            'note': self.note,
            'score': self.score,
            # 'tea_amount': self.tea_amount,
            # 'water_amount': self.water_amount,
            # 'steep_time': self.steep_time,
            # 'temperature': self.temperature,
            'flavors': self.flavors,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
