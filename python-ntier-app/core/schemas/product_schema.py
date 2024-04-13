from pydantic import BaseModel, Field, validator
from core.schemas.product_feature_schema import ProductFeatureOutput
from typing import Optional

class ProductInput(BaseModel):
    name: str = Field(max_length=120, default="name")
    stock: int = Field(default=1)
    price: float = Field(default=1)
    category_id: int = Field(default=1)

    @validator('name')
    def name_cannot_be_empty(cls, v):
        if not v:
            raise ValueError('Ürün adı boş olamaz.')
        return v
    @validator('stock')
    def stock_cannot_be_negative(cls, v):
        if v < 0:
            raise ValueError('Stok adedi negatif olamaz.')
        return v

    @validator('price')
    def price_cannot_be_negative(cls, v):
        if v < 0:
            raise ValueError('Fiyat negatif olamaz.')
        return v

    @validator('category_id')
    def category_id_cannot_be_negative(cls, v):
        if v < 0:
            raise ValueError('Kategori id negatif olamaz.')
        return v
    @validator('category_id')
    def category_id_cannot_be_empty(cls, v):
        if not v:
            raise ValueError('Kategori id boş olamaz.')
        return v
    
    @validator('price')
    def price_should_be_positive_when_stock_is_positive(cls, v, values, **kwargs):
        if values.get('stock', 0) > 0 and v <= 0:
            raise ValueError('Ürün stokta varsa, fiyat pozitif olmalıdır.')
        return v
    
    @validator('price')
    def price_should_be_zero_when_stock_is_zero(cls, v, values, **kwargs):
        if values.get('stock', 0) == 0 and v != 0:
            raise ValueError('Ürün stokta yoksa, fiyat 0 olmalıdır.')
        return v
    
class ProductOutput(BaseModel):
    id: int
    name: str
    stock: int
    price: float
    category_id: int
    product_feature: Optional[ProductFeatureOutput]
    class Config:
        orm_mode = True
