from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from deps.deps import get_db
from schemas.categoria import *
from crud.categoria import *

api_router = APIRouter()

@api_router.get("/", response_model=list[CategoriaResponse])
def listar_categorias(db:Session = Depends(get_db)):
    return obtener_categorias(db)

@api_router.post("/", response_model=CategoriaCreate)
def agregar_categoria(categoria: CategoriaCreate, db:Session = Depends(get_db)):
    return crear_categoria(db, categoria)

@api_router.put("/{id}", response_model=CategoriaCreate)
def actualizar_categoria(categoria_id: int, datos: CategoriaCreate , db:Session = Depends(get_db)):
    return actualizar_categoria(db, categoria_id, datos)

@api_router.delete("/{id}")
def eliminar_categoria(categoria_id: int, db:Session = Depends(get_db)):
    eliminar_categoria(db, categoria_id)
    return {"mensaje":"Categoria eliminada correctamente"}