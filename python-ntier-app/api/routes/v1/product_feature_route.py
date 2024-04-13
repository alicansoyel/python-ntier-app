from typing import List,Iterable
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data_access.db_context.config.database import get_db
from core.schemas.product_feature_schema import ProductFeatureInput, ProductFeatureOutput
from services.concrete.product_features.product_feature_service import ProductFeatureService


class ProductFeatureRoute:
    def __init__(self)->None:
        self.router = APIRouter(
            prefix="/product_feature",
            tags=["product_feature"]
        )
    def register_routes(self)->APIRouter:
        self.router.post("", status_code=201, response_model=ProductFeatureOutput)(self.create_product_feature)
        self.router.get("", status_code=200, response_model=List[ProductFeatureOutput])(self.get_product_features)
        self.router.delete("/{id}", status_code=204)(self.delete_product_feature)
        self.router.put("/{id}", status_code=200, response_model=ProductFeatureOutput)(self.update_product_feature)
        self.router.get("/{id}", status_code=200,response_model=ProductFeatureOutput)(self.get_product_feature_by_id)

        return self.router
    
    def create_product_feature(self, product_feature_data: ProductFeatureInput, session: Session = Depends(get_db))->ProductFeatureOutput:
        _service = ProductFeatureService(session)
        return _service.create(product_feature_data)

    def get_product_features(self, session: Session = Depends(get_db))->Iterable[ProductFeatureOutput]:
        _service = ProductFeatureService(session)
        return _service.get_all()

    def delete_product_feature(self, product_feature_id: int, session: Session = Depends(get_db)):
        _service = ProductFeatureService(session)
        return _service.delete(product_feature_id)

    def update_product_feature(self, product_feature_id: int, product_feature_data: ProductFeatureInput, session: Session = Depends(get_db))->ProductFeatureOutput:
        _service = ProductFeatureService(session)
        return _service.update(product_feature_id, product_feature_data)

    def get_product_feature_by_id(self, product_feature_id: int, session: Session = Depends(get_db))->ProductFeatureOutput:
        _service = ProductFeatureService(session)
        return _service.get_by_id(product_feature_id)
