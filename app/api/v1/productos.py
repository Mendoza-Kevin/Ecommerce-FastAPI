from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from deps.deps import get_db, require_admin
from schemas.producto import * 
from crud.producto import *

api_router = APIRouter()

@api_router.get("/", response_model=list[ProductoResponse])
def listar_productos(db:Session = Depends(get_db)):
    return obtener_productos(db)

@api_router.post("/", response_model=ProductoCreate, dependencies=[Depends(require_admin)])
def agregar_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return crear_producto(db, producto)

@api_router.put("/{id}", response_model=ProductoCreate)
def actualizar_producto(producto_id: int, datos: ProductoCreate, db:Session = Depends(get_db)):
    return actualizar_producto(db, producto_id, datos)

@api_router.delete("/{id}")
def eliminar_producto(producto_id = int, db:Session = Depends(get_db)):
    eliminar_producto(db, producto_id)
    return {"mensaje":"Producto eliminado correctamente"}