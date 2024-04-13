from core.models.category import Category
from data_access.repositories.abstract.base.base_repository_interface import IBaseRepository


class ICategoryRepository(IBaseRepository[Category]):
    pass
    

    
