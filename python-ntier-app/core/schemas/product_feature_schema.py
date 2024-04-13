from pydantic import BaseModel, Field,validator

class ProductFeatureInput(BaseModel):
    color: str = Field(min_length=3,max_length=100,default="red")
    height: int = Field(default=1)
    width: int = Field(default=1)
    product_id: int = Field(default=1)

    @validator('color')
    def color_cannot_be_empty(cls, v):
        if not v:
            raise ValueError('Renk boş olamaz.')
        return v

    @validator('height')
    def height_should_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Yükseklik pozitif bir değer olmalıdır.')
        return v

    @validator('width')
    def width_should_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Genişlik pozitif bir değer olmalıdır.')
        return v

    @validator('product_id')
    def product_id_cannot_be_negative(cls, v):
        if v < 0:
            raise ValueError('Ürün ID negatif olamaz.')
        return v

    @validator('product_id')
    def product_id_cannot_be_empty(cls, v):
        if not v:
            raise ValueError('Ürün ID boş olamaz.')
        return v

class ProductFeatureOutput(BaseModel):
    id: int
    color: str
    height: int
    width: int
    product_id: int

    class Config:
        orm_mode = True
