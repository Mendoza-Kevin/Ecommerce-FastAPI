from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from deps.deps import get_db, get_current_user
from schemas.pedido import *
from crud.pedido import *

api_router = APIRouter()

@api_router.post("/confirmar", response_model=PedidoResponse)
def confirmar_pedido(db:Session = Depends(get_db), usuario = Depends(get_current_user)):
    try:
        pedido = crear_pedido(db, usuario.id)
        return pedido
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))