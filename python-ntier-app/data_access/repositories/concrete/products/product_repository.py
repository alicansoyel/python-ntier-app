from sqlalchemy.orm import Session
from core.models.product import Product
from data_access.repositories.concrete.base.base_repository import BaseRepository
from data_access.repositories.abstract.products.product_repository_interface import IProductRepository

class ProductRepository(BaseRepository[Product],IProductRepository):
    def __init__(self, session: Session):
        super().__init__(session, Product)