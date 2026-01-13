from pydantic import BaseModel, ConfigDict, Field
from typing import List
from datetime import datetime

class DetallePedidoResponse(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    subtotal: float 
    model_config = ConfigDict(from_attributes=True)

class PedidoResponse(BaseModel):
    id: int
    usuario_id: int
    fecha: datetime
    total: float
    detalles: List[DetallePedidoResponse] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)
