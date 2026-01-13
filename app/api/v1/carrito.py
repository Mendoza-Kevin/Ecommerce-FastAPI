from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from deps.deps import get_db, get_current_user
from schemas.carrito import *
from crud.carrito import *

api_router = APIRouter()

@api_router.get("/", response_model=CarritoResponse)
def ver_carrito(db: Session = Depends(get_db), usuario = Depends(get_current_user)):
    carrito = obtener_carrito(db, usuario.id)
    return carrito

@api_router.post("/", response_model=ItemCarritoResponse)
def agregar_item_carrito(producto_id: int, cantidad: int, db:Session = Depends(get_db),
    usuario = Depends(get_current_user)):
    carrito = obtener_carrito(db, usuario.id)
    item = agregar_item(db, carrito.id, producto_id, cantidad)
    return item

@api_router.delete("/{item_id}")
def eliminar_item_carrito(item_id: int, db:Session = Depends(get_db), 
    usuario = Depends(get_current_user)):
    eliminar_item(db, item_id)
    return {"mensaje": "Producto eliminado del carrito"}