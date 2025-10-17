# models/Pedido.py
# Implemento la clase Pedido vinculada a un cliente y a productos con cantidades 
from __future__ import annotations  
import uuid  
from datetime import datetime  
from typing import List, Tuple  
from .Usuario import Cliente    
from .Producto import Producto  

class Pedido:
    """Representa un pedido con id, fecha, cliente y líneas producto-cantidad."""  

    def __init__(self, cliente: Cliente, items: List[Tuple[Producto, int]]) ->None:  # Defino el constructor con cliente y lista de líneas
        self.id: str = uuid.uuid4().hex  
        self.fecha: datetime = datetime.now()  
        self.cliente: Cliente = cliente  
        self.items: List[Tuple[Producto, int]] = items  # Guardo la lista de tuplas (producto, cantidad)

    def total(self) -> float: 
        return sum(prod.precio * cantidad for prod, cantidad in self.items)  

    def __str__(self) -> str:  
        return (
            f"Pedido(id={self.id}, fecha={self.fecha.isoformat(timespec='seconds')}, "
            f"cliente={self.cliente.nombre}, total={self.total():.2f})"
        )  
