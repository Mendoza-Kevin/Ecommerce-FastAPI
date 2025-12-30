from sqlalchemy.orm import Session
from models import Producto, Categoria
from schemas import ProductoCreate, CategoriaCreate
from fastapi import HTTPException

def crear_producto(db:Session, producto:ProductoCreate):
    db_producto = Producto(**producto.model_dump())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def obtener_productos(db:Session):
    return db.query(Producto).all()

def obtener_producto(db:Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def actualizar_producto(db:Session, producto_id: int, datos:ProductoCreate):
    producto = obtener_producto(db, producto_id)

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    for key, value in datos.model_dump(exclude_unset=True).items():
        setattr(producto, key, value)

    db.commit()
    db.refresh(producto)
    return producto

def eliminar_producto(db:Session, producto_id: int):
    producto = obtener_producto(db, producto_id)

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if producto:
        db.delete(producto)
        db.commit()
    return True

# Categoría

def crear_categoria(db:Session, categoria:Categoria):
    db_categoria = Categoria(nombre=categoria.nombre)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def obtener_categorias(db:Session):
    return db.query(Categoria).all()