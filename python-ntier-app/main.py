from fastapi import FastAPI
from api.routes.api_route_manager import APIRouteManager
from data_access.db_context.init_db import create_tables
from fastapi.middleware.cors import CORSMiddleware
from core.conf import settings

app = FastAPI(
    debug=True,
    title=settings.DESCRIPTION,
    version=settings.VERSION,
    openapi_url=settings.OPENAPI_URL

)

@app.on_event("startup")
def on_startup() -> None:
    create_tables()

api_router_manager = APIRouteManager()
api_router = api_router_manager.include_routes()
app.include_router(api_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)