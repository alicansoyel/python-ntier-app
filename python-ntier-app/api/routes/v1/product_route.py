from typing import List,Iterable
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data_access.db_context.config.database import get_db
from core.schemas.product_schema import ProductInput, ProductOutput
from services.concrete.products.product_service import ProductService

class ProductRoute:
    def __init__(self)->None:
        self.router = APIRouter(
            prefix="/product",
            tags=["product"],
        )
        
    def register_routes(self) -> APIRouter:
        self.router.post("", status_code=201, response_model=ProductOutput)(self.create_product)
        self.router.get("", status_code=200, response_model=List[ProductOutput])(self.get_products)
        self.router.get("/{id}", status_code=200,response_model=ProductOutput)(self.get_product_by_id)
        self.router.delete("/{id}", status_code=204)(self.delete_product)
        self.router.put("/{id}", status_code=200, response_model=ProductOutput)(self.update_product)

        return self.router
    
    def create_product(self, product_data: ProductInput, session: Session = Depends(get_db))->ProductOutput:
        _service = ProductService(session)
        return _service.create(product_data)

    def get_products(self, session: Session = Depends(get_db))->Iterable[ProductOutput]:
        _service = ProductService(session)
        return _service.get_all()

    def delete_product(self, product_id: int, session: Session = Depends(get_db)):
        _service = ProductService(session)
        return _service.delete(product_id)

    def update_product(self, product_id: int, product_data: ProductInput, session: Session = Depends(get_db))->ProductOutput:
        _service = ProductService(session)
        return _service.update(product_id, product_data)

    def get_product_by_id(self, product_id: int, session: Session = Depends(get_db))->ProductOutput:
        _service = ProductService(session)
        return _service.get_by_id(product_id)
