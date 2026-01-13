from pydantic import BaseModel, ConfigDict

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    stock: int
    en_stock: bool
    categoria_id: int

class ProductoResponse(ProductoCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)