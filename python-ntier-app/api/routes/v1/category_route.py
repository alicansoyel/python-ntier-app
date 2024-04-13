from typing import List,Iterable
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data_access.db_context.config.database import get_db
from core.schemas.category_schema import CategoryInput, CategoryOutput
from services.concrete.categories.category_service import CategoryService

class CategoryRoute:
    def __init__(self)->None:
        self.router = APIRouter(
            prefix="/category",
            tags=["category"]
        )

    def register_routes(self)->APIRouter:
        self.router.post("", status_code=201, response_model=CategoryOutput)(self.create_category)
        self.router.get("/{id}", status_code=200,response_model=CategoryOutput)(self.get_category_by_id)
        self.router.get("", status_code=200, response_model=List[CategoryOutput])(self.get_all_categories)
        self.router.delete("/{id}", status_code=204)(self.delete_category)
        self.router.put("/{id}", status_code=200, response_model=CategoryInput)(self.update_category)
        
        return self.router

    def create_category(self, category_data: CategoryInput, session: Session = Depends(get_db))->CategoryOutput:
        _service = CategoryService(session)
        return _service.create(category_data)

    def get_all_categories(self, session: Session = Depends(get_db))->Iterable[CategoryOutput]:
        _service = CategoryService(session)
        return _service.get_all()

    def delete_category(self, category_id: int, session: Session = Depends(get_db)):
        _service = CategoryService(session)
        return _service.delete(category_id)

    def update_category(self, category_id: int, category_data: CategoryInput, session: Session = Depends(get_db))->CategoryOutput:
        _service = CategoryService(session)
        return _service.update(category_id, category_data)
    
    def get_category_by_id(self, category_id: int, session: Session = Depends(get_db))->CategoryOutput:
        _service = CategoryService(session)
        return _service.get_by_id(category_id)

