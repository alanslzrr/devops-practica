# main.py
# Implemento el script principal para crear la tienda

from models.Producto import ProductoElectronico, ProductoRopa   
from Services.Tienda_service import TiendaService  

def main() -> None: 
    servicio = TiendaService()  # Creo una instancia de TiendaService para operar con la tienda

    #  Registro de usuarios: al menos tres clientes y un administrador ---
    cliente1 = servicio.registrar_usuario(   
        tipo="cliente", nombre="Ana", email="ana@example.com", direccion_postal="Calle A 1, Ciudad"
    )
    cliente2 = servicio.registrar_usuario(   
        tipo="cliente", nombre="Bruno", email="bruno@example.com", direccion_postal="Calle B 2, Ciudad"
    )
    cliente3 = servicio.registrar_usuario(   
        tipo="cliente", nombre="Carla", email="carla@example.com", direccion_postal="Calle C 3, Ciudad"
    )
    admin1 = servicio.registrar_usuario(   
        tipo="administrador", nombre="Admin", email="admin@example.com"
    )
    #  registramos un administrador para cumplir el requisito
    print(admin1.is_admin())

    #  cremos cinco productos de diferentes categorías
    p1 = ProductoElectronico(nombre="Portátil", precio=999.99, stock=10, meses_garantia=24)   
    p2 = ProductoElectronico(nombre="Smartphone", precio=599.50, stock=20, meses_garantia=12)   
    p3 = ProductoElectronico(nombre="Auriculares", precio=89.90, stock=30, meses_garantia=12)   
    p4 = ProductoRopa(nombre="Camiseta", precio=19.99, stock=50, talla="M", color="Azul") 
    p5 = ProductoRopa(nombre="Chaqueta", precio=79.95, stock=15, talla="L", color="Negro")   

    #  añadimos los productos al inventario
    servicio.anadir_producto(p1)   
    servicio.anadir_producto(p2)   
    servicio.anadir_producto(p3)  
    servicio.anadir_producto(p4)   
    servicio.anadir_producto(p5)   

    #  Listamos para ver que se hayan añadido
    print("Inventario inicial:")   
    for prod in servicio.listar_productos():  
        print(str(prod))   

    #  Simulamos tres pedidos 
    # Pedido 1 por Ana: 1 portátil y 2 camisetas
    pedido1 = servicio.realizar_pedido(     
        usuario_id=cliente1.id if cliente1 else "",     
        items=[(p1.id, 1), (p4.id, 2)]  # 
    )
    if pedido1:  
        print("\nResumen pedido 1:")   
        print(str(pedido1))   
        print("Stock actualizado tras pedido 1:")   
        print(str(p1))   
        print(str(p4))   

    # Pedido 2 por Bruno: 2 smartphones y 1 chaqueta
    pedido2 = servicio.realizar_pedido(   
        usuario_id=cliente2.id if cliente2 else "",   
        items=[(p2.id, 2), (p5.id, 1)]   
    )
    if pedido2:   
        print("\nResumen pedido 2:")   
        print(str(pedido2))    
        print("Stock actualizado tras pedido 2:")   
        print(str(p2))   
        print(str(p5))   

    # Pedido 3 por Carla: 1 portátil, 1 auriculares y 1 camiseta
    pedido3 = servicio.realizar_pedido(   
        usuario_id=cliente3.id if cliente3 else "",   
        items=[(p1.id, 1), (p3.id, 1), (p4.id, 1)]   
    )
    if pedido3:   
        print("\nResumen pedido 3:")  
        print(str(pedido3))  
        print("Stock actualizado tras pedido 3:")   
        print(str(p1))   
        print(str(p3))   
        print(str(p4))  

#  Historial de pedidos de todos los clientes (por id) ---
    print("\nHistorial pedidos de Ana:")  
    historico_ana = servicio.listar_pedidos_por_usuario(cliente1.id if cliente1 else "")  
    for p in historico_ana:  
        print(str(p))   
    print("\nHistorial pedidos de Bruno:")  
    historico_bruno = servicio.listar_pedidos_por_usuario(cliente2.id if cliente2 else "")  
    for p in historico_bruno:  
        print(str(p))   

    print("\nHistorial pedidos de Carla:")  
    historico_carla = servicio.listar_pedidos_por_usuario(cliente3.id if cliente3 else "")  
    for p in historico_carla:  
        print(str(p))   

if __name__ == "__main__":  
    main()  
