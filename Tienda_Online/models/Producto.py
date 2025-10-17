# models/Producto.py
# Implemento las clases de productos
from __future__ import annotations   
import uuid   

class Producto:
    """Clase base para productos con id, nombre, precio y stock."""  

    def __init__(self, nombre: str, precio: float, stock: int) -> None:  # Defino el constructor con tipado para nombre, precio y stock
        self.id: str = uuid.uuid4().hex     
        self.nombre: str = nombre   
        self.precio: float = precio   
        self.stock: int = stock   

    def hay_stock(self, cantidad: int) -> bool:  # 
        return self.stock >= cantidad  

    def actualizar_stock(self, cambio: int) -> None: 
        self.stock += cambio  

    def __str__(self) -> str:  # Defino la representación en texto de las características principales del producto
        return f"Producto(id={self.id}, nombre={self.nombre}, precio={self.precio:.2f}, stock={self.stock})"  


class ProductoElectronico(Producto):
    """Subclase de producto que añade meses de garantía."""  

    def __init__(self, nombre: str, precio: float, stock: int, meses_garantia: int) -> None:  # Defino el constructor incluyendo la garantía
        super().__init__(nombre, precio, stock)  
        self.meses_garantia: int = meses_garantia   

    def __str__(self) -> str:  # Sobrescribo __str__ para incluir la información extra de garantía  
        return (
            f"ProductoElectronico(id={self.id}, nombre={self.nombre}, "
            f"precio={self.precio:.2f}, stock={self.stock}, garantia_meses={self.meses_garantia})"
        )  


class ProductoRopa(Producto):
    """Subclase de producto que añade talla y color."""  

    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str) -> None:  # Defino el constructor con talla y color
        super().__init__(nombre, precio, stock)  
        self.talla: str = talla   
        self.color: str = color   

    def __str__(self) -> str:  
        return (
            f"ProductoRopa(id={self.id}, nombre={self.nombre}, precio={self.precio:.2f}, "
            f"stock={self.stock}, talla={self.talla}, color={self.color})"
        )  
