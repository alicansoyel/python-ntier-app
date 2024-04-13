from core.schemas.category_schema import CategoryInput, CategoryOutput
from services.abstract.base.base_service_interface import IBaseService

class ICategoryService(IBaseService[CategoryInput, CategoryOutput]):
    pass