class Lugar:
    def __init__(self, ciudad, comunidad, pais):
        self.ciudad = ciudad
        self.comunidad = comunidad
        self.pais = pais

    def __str__(self):
        return f"{self.ciudad}, {self.comunidad} ({self.pais})"


class EtapaConstruccion:
    def __init__(self, fecha_inicio, fecha_fin=None):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self):
        if self.fecha_fin:
            return f"Desde {self.fecha_inicio} hasta {self.fecha_fin}"
        return f"Desde {self.fecha_inicio} (fecha fin: desconocida)"


class Edificio:
    def __init__(self, nombre, culto, material, estilos, fecha_primera_consg, fecha_segunda_consg, fecha_declaracion_bic):
        self.nombre = nombre
        self.culto = culto
        self.material = material
        self.estilos = estilos
        self.fecha_primera_consg = fecha_primera_consg
        self.fecha_segunda_consg = fecha_segunda_consg
        self.fecha_declaracion_bic = fecha_declaracion_bic
        self.lugar = None
        self.etapas = []

    def localizar_en(self, lugar):
        self.lugar = lugar

    def agregar_etapa(self, etapa):
        self.etapas.append(etapa)

    def mostrar_info(self):
        info = f"⛪ {self.nombre}\n"
        info += f"Culto: {self.culto}\n"
        info += f"Material principal: {self.material}\n"
        info += f"Estilos arquitectónicos: {', '.join(self.estilos)}\n"
        info += f"Primera consagración: {self.fecha_primera_consg}\n"
        info += f"Segunda consagración: {self.fecha_segunda_consg}\n"
        info += f"Declaración BIC: {self.fecha_declaracion_bic}\n"
        if self.lugar:
            info += f"Ubicación: {self.lugar}\n"
        if self.etapas:
            info += "Etapas de construcción:\n"
            for etapa in self.etapas:
                info += f"   - {etapa}\n"
        return info


# Crear lugar
santiago = Lugar("Santiago de Compostela", "Galicia", "España")

# Crear edificio
catedral = Edificio(
    nombre="Catedral de Santiago de Compostela",
    culto="Católico",
    material="Granito",
    estilos=["Románico", "Gótico", "Barroco", "Plateresco", "Neoclásico"],
    fecha_primera_consg=1128,
    fecha_segunda_consg="3 de abril de 1211",
    fecha_declaracion_bic=1896
)

# Asociar lugar
catedral.localizar_en(santiago)

# Crear etapas de construcción
etapa1 = EtapaConstruccion(1075, 1122)
etapa2 = EtapaConstruccion(1168, None)

# Agregar etapas al edificio
catedral.agregar_etapa(etapa1)
catedral.agregar_etapa(etapa2)

# Mostrar información
print(catedral.mostrar_info())

