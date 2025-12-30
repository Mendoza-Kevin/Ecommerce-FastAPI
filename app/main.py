from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db


app = FastAPI()


@app.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db:Session = Depends(get_db)):
    return crud.obtener_productos(db)

@app.post("/productos", response_model=schemas.ProductoCreate)
def agregar_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@app.put("/productos/{id}", response_model=schemas.ProductoCreate)
def actualizar_producto(producto_id: int, datos: schemas.ProductoCreate, db:Session = Depends(get_db)):
    return crud.actualizar_producto(db, producto_id, datos)

@app.delete("/productos/{id}")
def eliminar_producto(producto_id = int, db:Session = Depends(get_db)):
    crud.eliminar_producto(db, producto_id)
    return {"mensaje":"Producto eliminado correctamente"}
   
# Categorias

@app.get("/categorias", response_model=list[schemas.CategoriaResponse])
def listar_categorias(db:Session = Depends(get_db)):
    return crud.obtener_categorias(db)

@app.post("/categorias", response_model=schemas.CategoriaCreate)
def agregar_categoria(categoria: schemas.CategoriaCreate, db:Session = Depends(get_db)):
    return crud.crear_categoria(db, categoria)