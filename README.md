# E-commerce FastAPI

Una API RESTful completa para la gestión de un e-commerce construida con FastAPI, SQLAlchemy y PostgreSQL.

## 🚀 Características

- **Autenticación con JWT**: Sistema seguro de autenticación basado en tokens
- **Administración de Productos**: CRUD completo para productos
- **Gestión de Categorías**: Organización de productos por categorías
- **Carrito de Compras**: Funcionalidad completa de carrito para usuarios
- **Gestión de Pedidos**: Sistema de confirmación de pedidos
- **Roles de Usuario**: Sistema de autenticación con roles (admin/usuario)
- **Base de Datos Relacional**: PostgreSQL con SQLAlchemy ORM
- **Documentación Automática**: Interfaz Swagger/OpenUI integrada

## 📁 Estructura del Proyecto

```
Ecommerce-FastAPI/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── api.py          # Router principal de la API
│   │       ├── auth.py          # Endpoints de autenticación
│   │       ├── productos.py     # Endpoints de productos
│   │       ├── categorias.py    # Endpoints de categorías
│   │       ├── carrito.py       # Endpoints del carrito
│   │       └── pedido.py        # Endpoints de pedidos
│   ├── core/
│   │   ├── config.py            # Configuración de la aplicación
│   │   └── security.py          # Funciones de seguridad y JWT
│   ├── crud/
│   │   ├── usuario.py           # Operaciones CRUD de usuarios
│   │   ├── producto.py          # Operaciones CRUD de productos
│   │   ├── categoria.py         # Operaciones CRUD de categorías
│   │   ├── carrito.py           # Operaciones CRUD del carrito
│   │   └── pedido.py            # Operaciones CRUD de pedidos
│   ├── db/
│   │   ├── database.py          # Configuración de la base de datos
│   │   └── init_db.py           # Script de inicialización
│   ├── deps/
│   │   └── deps.py              # Dependencias comunes
│   ├── models/
│   │   ├── __init__.py
│   │   ├── usuario.py           # Modelo de Usuario
│   │   ├── categoria.py         # Modelo de Categoría
│   │   ├── producto.py          # Modelo de Producto
│   │   └── pedido.py            # Modelos de Pedido y Carrito
│   ├── schemas/
│   │   ├── usuario.py           # Esquemas Pydantic de usuarios
│   │   ├── categoria.py         # Esquemas Pydantic de categorías
│   │   ├── producto.py          # Esquemas Pydantic de productos
│   │   ├── carrito.py           # Esquemas Pydantic del carrito
│   │   ├── pedido.py            # Esquemas Pydantic de pedidos
│   │   └── token.py             # Esquema de token JWT
│   ├── tests/
│   │   ├── test_auth.py         # Tests de autenticación
│   │   └── test_productos.py    # Tests de productos
│   ├── .env                     # Variables de entorno
│   └── main.py                  # Aplicación FastAPI principal
├── requirements.txt             # Dependencias del proyecto
├── .gitignore                   # Archivos ignorados por Git
└── README.md                    # Documentación del proyecto
```

## 🛠️ Instalación y Configuración

### Prerrequisitos

- Python 3.8+
- PostgreSQL 12+
- pip (gestor de paquetes de Python)

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Mendoza-Kevin/Ecommerce-FastAPI.git
cd Ecommerce-FastAPI
```

### 2. Crear Entorno Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos

1. **Crear la base de datos en PostgreSQL:**
   ```sql
   CREATE DATABASE ecommerce_db;
   ```

2. **Configurar las variables de entorno:**
   
   Copiar y editar el archivo `.env`:
   ```bash
   cp app/.env.example app/.env
   ```
   
   O crear el archivo `app/.env` con el siguiente contenido:
   ```env
   DATABASE_URL = postgresql://usuario:password@localhost:5432/ecommerce_db
   SECRET_KEY = tu_clave_secreta_muy_segura
   ALGORITHM = HS256
   ACCESS_TOKEN_EXPIRE_MINUTES = 30
   ```

### 5. Inicializar la Base de Datos

```bash
cd app
python db/init_db.py
```

## 🚀 Ejecución de la Aplicación

### Modo Desarrollo

```bash
# Desde la raíz del proyecto
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Modo Producción

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📚 Documentación de la API

Una vez iniciada la aplicación, puedes acceder a:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI Schema**: `http://localhost:8000/openapi.json`

## 🔗 Endpoints Disponibles

### Autenticación (`/api/v1/auth`)

- `POST /api/v1/auth/usuarios` - Registrar nuevo usuario
- `POST /api/v1/auth/login` - Iniciar sesión y obtener token
- `GET /api/v1/auth/usuarios/perfil` - Obtener perfil del usuario
- `GET /api/v1/auth/admin/ping` - Endpoint de prueba para admin

### Productos (`/api/v1/productos`)

- `GET /api/v1/productos/` - Listar todos los productos
- `POST /api/v1/productos/` - Crear nuevo producto (requiere admin)
- `PUT /api/v1/productos/{id}` - Actualizar producto
- `DELETE /api/v1/productos/{id}` - Eliminar producto

### Categorías (`/api/v1/categorias`)

- `GET /api/v1/categorias/` - Listar todas las categorías
- `POST /api/v1/categorias/` - Crear nueva categoría
- `PUT /api/v1/categorias/{id}` - Actualizar categoría
- `DELETE /api/v1/categorias/{id}` - Eliminar categoría

### Carrito (`/api/v1/carrito`)

- `GET /api/v1/carrito/` - Ver carrito del usuario
- `POST /api/v1/carrito/` - Agregar item al carrito
- `DELETE /api/v1/carrito/{item_id}` - Eliminar item del carrito

### Pedidos (`/api/v1/pedido`)

- `POST /api/v1/pedido/confirmar` - Confirmar pedido del carrito

## 🔐 Autenticación

La API utiliza tokens JWT para la autenticación. Para acceder a los endpoints protegidos:

1. Inicia sesión obteniendo un token:
   ```bash
   curl -X POST "http://localhost:8000/api/v1/auth/login" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "username=tu_email&password=tu_password"
   ```

2. Usa el token en las solicitudes protegidas:
   ```bash
   curl -X GET "http://localhost:8000/api/v1/auth/usuarios/perfil" \
        -H "Authorization: Bearer tu_token_jwt"
   ```

## 🧪 Testing

Para ejecutar las pruebas:

```bash
pytest
```

## 📦 Dependencias Principales

- **FastAPI**: Framework web moderno y rápido
- **SQLAlchemy**: ORM para base de datos
- **PostgreSQL**: Base de datos relacional
- **Pydantic**: Validación de datos
- **PassLib**: Manejo de contraseñas
- **Python-JOSE**: Manejo de tokens JWT
- **Uvicorn**: Servidor ASGI

## 🤝 Contribución

1. Fork del proyecto
2. Crear una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de los cambios (`git commit -am 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Kevin Mendoza** - Backend Developer

- GitHub: [@Mendoza-Kevin](https://github.com/Mendoza-Kevin)

## 📝 Notas

- Asegúrate de configurar correctamente las variables de entorno antes de ejecutar la aplicación
- La base de datos PostgreSQL debe estar corriendo antes de inicializar las tablas
- En producción, utiliza claves secretas más seguras y considera variables de entorno adicionales