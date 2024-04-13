from sqlalchemy import Column, String,Integer,Float,ForeignKey
from sqlalchemy.orm import relationship
from data_access.db_context.config.database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True,unique=True,nullable=False)
    name = Column(String,nullable=False)
    stock = Column(Integer,nullable=False)
    price = Column(Float,nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'),nullable=False)
    category = relationship("Category", back_populates="products")
    product_feature = relationship("ProductFeature", uselist=False, back_populates="product")
