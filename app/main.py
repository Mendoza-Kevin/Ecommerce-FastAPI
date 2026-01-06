from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from utils import verify_password
from auth import crear_token
from deps import get_current_user, require_admin


app = FastAPI()

# Productos

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

@app.put("/categorias/{id}", response_model=schemas.CategoriaCreate)
def actualizar_categoria(categoria_id: int, datos: schemas.CategoriaCreate , db:Session = Depends(get_db)):
    return crud.actualizar_categoria(db, categoria_id, datos)

@app.delete("/categorias/{id}")
def eliminar_categoria(categoria_id: int, db:Session = Depends(get_db)):
    crud.eliminar_categoria(db, categoria_id)
    return {"mensaje":"Categoria eliminada correctamente"}

# Usuarios

@app.post("/usuarios", response_model=schemas.UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario:schemas.UsuarioCreate, db:Session = Depends(get_db)):
    try:
        return crud.crear_usuario(db, usuario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = crud.obtener_usuario_por_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales invalidas")
    token = crear_token(sub=user.email, es_admin=user.es_admin)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/usuarios/perfil", response_model=schemas.UsuarioResponse)
def leer_perfil(current_user = Depends(get_current_user)):
    return current_user

@app.get("/admin/ping")
def admin_ping(_admin = Depends(require_admin)):
    return {"ok": True, "rol": "admin"}