from sqlalchemy import Column, INTEGER, VARCHAR, FLOAT, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from my_framework.hw.db.alchemy.models.products import Products

Base = declarative_base()


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(INTEGER, primary_key=True)
    product_id = Column(INTEGER, ForeignKey(Products.id))
    quantity = Column(INTEGER)

    def __str__(self):
        return f"{self.id}, {self.name}, {self.price}"
