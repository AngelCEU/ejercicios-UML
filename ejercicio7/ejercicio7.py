from datetime import date
from typing import List, Optional

class LugarDeActuacion:
    def __init__(self, coordenada_x: float, coordenada_y: float, nombre: Optional[str] = None):
        self.nombre = nombre  # 0..* Texto (puede ser None o una lista de nombres)
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y

    def __str__(self):
        return f"Lugar(nombre={self.nombre}, X={self.coordenada_x}, Y={self.coordenada_y})"


class MiembroDelEquipo:
    def __init__(self, nombre: str, apellidos: str, rol: Optional[str] = None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.rol = rol  # 0..* Texto (puede ser None o lista de roles)

    def __str__(self):
        return f"Miembro({self.nombre} {self.apellidos}, rol={self.rol})"


class Proyecto:
    def __init__(self, nombre: str, fecha_inicio: date, fecha_fin: Optional[date] = None):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.miembros: List[MiembroDelEquipo] = []
        self.lugares: List[LugarDeActuacion] = []

    def agregar_miembro(self, miembro: MiembroDelEquipo):
        self.miembros.append(miembro)

    def agregar_lugar(self, lugar: LugarDeActuacion):
        self.lugares.append(lugar)

    def __str__(self):
        miembros_str = ", ".join(str(m) for m in self.miembros)
        lugares_str = ", ".join(str(l) for l in self.lugares)
        return (f"Proyecto({self.nombre}, inicio={self.fecha_inicio}, fin={self.fecha_fin},\n"
                f"  Miembros=[{miembros_str}],\n"
                f"  Lugares=[{lugares_str}])")
    