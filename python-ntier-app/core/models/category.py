from sqlalchemy import Column, String,Integer
from sqlalchemy.orm import relationship
from data_access.db_context.config.database import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True,unique=True,nullable=False)
    name = Column(String,nullable=False)
    products = relationship("Product", back_populates="category")