from sqlalchemy import Column, INTEGER, VARCHAR, FLOAT, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(255))
    price = Column(FLOAT)

    def __str__(self):
        return f"{self.id}, {self.name}, {self.price}"