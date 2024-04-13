from pydantic import BaseModel, Field, validator
from typing import List
from core.schemas.product_schema import ProductOutput

class CategoryInput(BaseModel):
    name: str = Field(max_length=120, default="name")
    @validator('name')
    def name_cannot_be_empty(cls, v):
        if not v:
            raise ValueError('Kategori adı boş olamaz.')
        return v

class CategoryInDb(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class CategoryOutput(BaseModel):
    id: int
    name: str
    products: List[ProductOutput]

    class Config:
        orm_mode = True
