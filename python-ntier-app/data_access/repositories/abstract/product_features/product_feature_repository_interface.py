from core.models.product_feature import ProductFeature
from data_access.repositories.abstract.base.base_repository_interface import IBaseRepository
class IProductFeatureRepository(IBaseRepository[ProductFeature]):
    pass
    

    
