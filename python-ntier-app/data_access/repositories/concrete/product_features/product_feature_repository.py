from sqlalchemy.orm import Session
from core.models.product_feature import ProductFeature
from data_access.repositories.concrete.base.base_repository import BaseRepository
from data_access.repositories.abstract.product_features.product_feature_repository_interface import IProductFeatureRepository

class ProductFeatureRepository(BaseRepository[ProductFeature],IProductFeatureRepository):
    def __init__(self, session: Session):
        super().__init__(session, ProductFeature)


