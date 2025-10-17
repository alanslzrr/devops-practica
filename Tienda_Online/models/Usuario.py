# models/Usuario.py
# Implemento las clases de usuario (Usuario, Cliente, Administrador)
from __future__ import annotations   
import uuid  

class Usuario:
    """Representa a una persona que interactúa con la tienda (base)."""  

    def __init__(self, nombre: str, email: str) -> None:  # Defino el constructor con nombre y correo electrónico
        self.id: str = uuid.uuid4().hex     
        self.nombre: str = nombre   
        self.email: str = email  

    def is_admin(self) -> bool:  
        return False  


class Cliente(Usuario):
    """Subclase de usuario que añade la dirección postal."""  

    def __init__(self, nombre: str, email: str, direccion_postal: str) -> None:  # Defino el constructor con dirección postal
        super().__init__(nombre, email)  
        self.direccion_postal: str = direccion_postal  


class Administrador(Usuario):
    """Subclase de usuario que representa a los gestores de la tienda."""  

    def is_admin(self) -> bool:  # Sobrescribo el método is_admin para este tipo de usuario
        return True  
