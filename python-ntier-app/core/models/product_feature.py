from sqlalchemy import Column, String,Integer,ForeignKey
from sqlalchemy.orm import relationship
from data_access.db_context.config.database import Base

class ProductFeature(Base):
    __tablename__ = 'product_features'
    id = Column(Integer, primary_key=True,unique=True,nullable=False)
    color = Column(String,nullable=False)
    height = Column(Integer,nullable=False)
    width = Column(Integer,nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), unique=True,nullable=False)
    product = relationship("Product", back_populates="product_feature")

