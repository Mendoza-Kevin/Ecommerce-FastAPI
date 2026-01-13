from sqlalchemy.orm import Session
from models.producto import Producto
from models.pedido import Carrito, Pedido, DetallePedido

def crear_pedido(db:Session, usuario_id:int):
    carrito = db.query(Carrito).filter_by(usuario_id=usuario_id).first()

    if not carrito or not carrito.items:
        raise ValueError("El carrito esta vacio")
    
    total = 0
    pedido = Pedido(usuario_id=usuario_id, total=0)
    db.add(pedido)
    db.commit()
    db.refresh(pedido)
    
    for item in carrito.items:
        producto = db.get(Producto, item.producto_id)
        if not producto or not producto.en_stock or producto.precio <= 0:
            continue
        if item.cantidad > 0 and item.cantidad <= producto.stock:
            producto.stock -= item.cantidad
            subtotal = producto.precio * item.cantidad
            detalle = DetallePedido(
                pedido_id= pedido.id,
                producto_id = producto.id,
                cantidad = item.cantidad,
                subtotal = subtotal
            )
            db.add(detalle)
            total += subtotal
            db.delete(item)
        
    if total == 0:
        db.delete(pedido)
        db.commit()
        raise ValueError("No hay productos válidos para crear el pedido")
        
    pedido.total = total
    db.commit()
    db.refresh(pedido)
    return pedido