from pydantic import BaseModel, ConfigDict
from typing import List

class ItemCarritoResponse(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    model_config = ConfigDict(from_attributes=True)

class CarritoResponse(BaseModel):
    id: int
    usuario_id: int
    items: List[ItemCarritoResponse] = []
    model_config = ConfigDict(from_attributes=True)