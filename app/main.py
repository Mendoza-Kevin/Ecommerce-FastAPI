from fastapi import FastAPI
from api.v1.api import api_router


app = FastAPI(
    title="E-commerce API",
    description="""
    API RESTful completa para la gestión de un E-commerce.

    Incluye: 
    - Autenticación con JWT
    - Administración de Productos y Categorías
    - Carrito de compras
    - Gestión de Pedidos
    """,
    version="1.0.0",
    contact={
        "name": "Kevin Mendoza - Backend Developer",
        "url": "https://github.com/Mendoza-Kevin/Ecommerce-FastAPI",
        "email": "kevin.mendozaa016@gmail.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/license/MIT"
    }
)

app.include_router(api_router, prefix="/api/v1")