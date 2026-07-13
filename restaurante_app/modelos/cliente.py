
from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str

    def mostrar_informacion(self):
        print(f"ID Cliente: {self.id_cliente} | Nombre: {self.nombre} | Correo: {self.correo}")
