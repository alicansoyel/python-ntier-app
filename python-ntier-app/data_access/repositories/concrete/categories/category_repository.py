from core.models.category import Category
from sqlalchemy.orm import Session
from data_access.repositories.concrete.base.base_repository import BaseRepository
from data_access.repositories.abstract.categories.category_repository_interface import ICategoryRepository

class CategoryRepository(BaseRepository[Category],ICategoryRepository):
    def __init__(self, session: Session):
        super().__init__(session, Category)
