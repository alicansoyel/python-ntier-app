from core.schemas.product_feature_schema import ProductFeatureInput, ProductFeatureOutput
from services.abstract.base.base_service_interface import IBaseService
from abc import abstractmethod

class IProductFeatureService(IBaseService[ProductFeatureInput, ProductFeatureOutput]):
    pass
