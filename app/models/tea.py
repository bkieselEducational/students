from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Tea(db.Model):
    __tablename__ = 'teas'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id"), ondelete="CASCADE"), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String)
    # flavors = db.Column(db.String)
    sold_in = db.Column(db.String)
    certification = db.Column(db.String)
    ingredients = db.Column(db.String)
    caffeine = db.Column(db.String(255))
    description = db.Column(db.String)
    image_url = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    #relationships
    user = db.relationship("User", back_populates="teas")
    tasting_notes = db.relationship("TastingNote", back_populates="tea", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'company': self.company,
            'type': self.type,
            # 'flavors': self.flavors,
            'sold_in': self.sold_in,
            'certification': self.certification,
            'ingredients': self.ingredients,
            'caffeine': self.caffeine,
            'description': self.description,
            'image_url': self.image_url,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
