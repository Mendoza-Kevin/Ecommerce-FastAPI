from pydantic import BaseModel, ConfigDict, EmailStr

# Productos
class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    categoria_id: int

class ProductoResponse(ProductoCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Categorias

class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Usuarios

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str
    es_admin: bool = False

class UsuarioResponse(UsuarioBase):
    id: int
    es_admin: bool
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"