from sqlalchemy.orm import Session
from data_access.repositories.concrete.product_features.product_feature_repository import ProductFeatureRepository
from core.schemas.product_feature_schema import ProductFeatureInput, ProductFeatureInput
from services.concrete.base.base_service import BaseService
from services.abstract.product_features.product_feature_service_interface import IProductFeatureService

class ProductFeatureService(BaseService[ProductFeatureInput, ProductFeatureInput],IProductFeatureService):
    def __init__(self, session: Session):
        self.product_feature_repository = ProductFeatureRepository(session)
        super().__init__(self.product_feature_repository)

    