from core.schemas.product_schema import ProductInput, ProductOutput
from services.abstract.base.base_service_interface import IBaseService

class IProductService(IBaseService[ProductInput, ProductOutput]):
    pass