# Services/Tienda_service.py
# Aqui buscaremos gestionar usuarios, productos y pedidos  
from __future__ import annotations   
from typing import Dict, List, Tuple, Optional, Literal   
from models.Usuario import Usuario, Cliente, Administrador   
from models.Producto import Producto   
from models.Pedido import Pedido   

class TiendaService:
    """Servicio que actúa como intermediario entre usuarios y productos."""   

    def __init__(self) -> None:  # Defino el constructor del servicio
        self.usuarios: Dict[str, Usuario] = {}  # Mantengo un diccionario de usuarios indexado por id
        self.productos: Dict[str, Producto] = {}  # Mantengo un diccionario de productos indexado por id
        self.pedidos: List[Pedido] = []  # Mantengo una lista con todos los pedidos registrados

    def registrar_usuario(
        self,
        tipo: Literal["cliente", "administrador"],
        nombre: str,
        email: str,
        direccion_postal: Optional[str] = None,    
        ) -> Optional[Usuario]:  
        
        if tipo == "cliente":  
            if direccion_postal is None:  
                return None   
            usuario = Cliente(nombre=nombre, email=email, direccion_postal=direccion_postal)  
        elif tipo == "administrador":   
            usuario = Administrador(nombre=nombre, email=email)  
        else:  
            return None  
        self.usuarios[usuario.id] = usuario  
        return usuario  

    def anadir_producto(self, producto: Producto) -> None:  # defino un metodo para añadir productos al inventario
        self.productos[producto.id] = producto   

    def eliminar_producto(self, producto_id: str) -> bool:  # Defino un método para eliminar un producto por su identificador
        if producto_id in self.productos:   
            del self.productos[producto_id]   
            return True  
        return False   

    def listar_productos(self) -> List[Producto]:  
        return list(self.productos.values())  

    def realizar_pedido(self, usuario_id: str, items: List[Tuple[str, int]]) -> Optional[Pedido]:  # Defino un método para realizar un pedido
        usuario = self.usuarios.get(usuario_id)  
        if not isinstance(usuario, Cliente):  # Verifico que el usuario exista y sea de tipo cliente
            return None  
        lineas: List[Tuple[Producto, int]] = []  # Preparo una lista para almacenar las líneas con objetos producto y cantidades
        for prod_id, cantidad in items:   
            producto = self.productos.get(prod_id)  
            if producto is None:  
                return None  
            if not producto.hay_stock(cantidad):  
                return None  
            lineas.append((producto, cantidad))  
        for producto, cantidad in lineas:  
            producto.actualizar_stock(-cantidad)  
        pedido = Pedido(cliente=usuario, items=lineas)  # Creo el objeto Pedido con el cliente y las líneas confirmadas
        self.pedidos.append(pedido)  
        return pedido  

    def listar_pedidos_por_usuario(self, usuario_id: str) -> List[Pedido]:  # Defino un método para listar pedidos por usuario ordenados por fecha
        pedidos_usuario = [p for p in self.pedidos if p.cliente.id == usuario_id]  
        pedidos_ordenados = sorted(pedidos_usuario, key=lambda p: p.fecha)  
        return pedidos_ordenados  
