from fastapi import APIRouter
from api.routes.v1.category_route import CategoryRoute
from api.routes.v1.product_feature_route import ProductFeatureRoute
from api.routes.v1.product_route import ProductRoute
from core.conf import settings

class APIRouteManager:
    def __init__(self)->None:
        self._router = APIRouter(prefix=settings.API_V1_STR)
    
    def include_routes(self) -> APIRouter:
        self._router.include_router(CategoryRoute().register_routes())
        self._router.include_router(ProductFeatureRoute().register_routes())
        self._router.include_router(ProductRoute().register_routes())
        return self._router