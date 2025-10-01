from datetime import date
from enum import Enum
from typing import Optional

class TipoActuacion(Enum):
    SONDEO = "Sondeo"
    EXCAVACION = "Excavación"
    SEGUIMIENTO = "Seguimiento"

class Actuacion:
    def __init__(self, fecha_inicio: date, tipo: TipoActuacion, fecha_fin: Optional[date] = None):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo

    def __str__(self):
        return (f"Actuación(tipo={self.tipo.value}, "
                f"inicio={self.fecha_inicio}, "
                f"fin={self.fecha_fin})")
