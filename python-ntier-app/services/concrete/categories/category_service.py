from typing import List,Iterable
from sqlalchemy.orm import Session
from data_access.repositories.concrete.categories.category_repository import CategoryRepository
from core.schemas.category_schema import CategoryInput, CategoryOutput
from services.concrete.base.base_service import BaseService
from services.abstract.categories.category_service_interface import ICategoryService

class CategoryService(BaseService[CategoryInput, CategoryOutput],ICategoryService):
    def __init__(self, session: Session):
        self.category_repository = CategoryRepository(session)
        super().__init__(self.category_repository)
    