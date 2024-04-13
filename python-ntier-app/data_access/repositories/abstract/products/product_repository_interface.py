from core.models.product import Product
from data_access.repositories.abstract.base.base_repository_interface import IBaseRepository

class IProductRepository(IBaseRepository[Product]):
    pass