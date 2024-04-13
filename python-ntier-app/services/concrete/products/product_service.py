from sqlalchemy.orm import Session
from data_access.repositories.concrete.products.product_repository import ProductRepository
from core.schemas.product_schema import ProductInput, ProductOutput
from services.concrete.base.base_service import BaseService
from services.abstract.products.product_service_interface import IProductService

class ProductService(BaseService[ProductInput, ProductOutput],IProductService):
    def __init__(self, session: Session):
        self.product_repository = ProductRepository(session)
        super().__init__(self.product_repository)