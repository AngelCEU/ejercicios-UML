class Lugar:
    def __init__(self, institucion, ciudad, pais):
        self.institucion = institucion
        self.ciudad = ciudad
        self.pais = pais

    def __str__(self):
        return f"{self.institucion}, {self.ciudad} ({self.pais})"


class Cuadro:
    def __init__(self, titulo, ac, tecnica, subt, soporte, autor, estado):
        self.titulo = titulo
        self.adscripcion_cronologica = ac
        self.tecnica = tecnica
        self.subtecnica = subt
        self.soporte = soporte
        self.autor = autor
        self.estado = estado
        self.lugar = None
        self.replicas = []

    def localizar_en(self, lugar):
        self.lugar = lugar

    def agregar_replicas(self, cuadro):
        self.replicas.append(cuadro)

    def mostrar_info(self):
        info = f"🎨 {self.titulo}\n"
        info += f"AC: {self.adscripcion_cronologica}\n"
        info += f"Técnica: {self.tecnica}\n"
        info += f"Subtécnica: {self.subtecnica}\n"
        info += f"Soporte: {self.soporte}\n"
        info += f"Autor: {self.autor}\n"
        info += f"Estado de conservación: {self.estado}\n"
        if self.lugar:
            info += f"Ubicado en: {self.lugar}\n"
        if self.replicas:
            info += "Réplicas:\n"
            for r in self.replicas:
                info += f"   - {r.titulo} ({r.lugar.ciudad}, {r.lugar.pais})\n"
        return info


# Definir lugares
louvre = Lugar("Museo del Louvre", "Paris", "Francia")
prado = Lugar("Museo del Prado", "Madrid", "España")

# Definir cuadros
gioconda = Cuadro(
    titulo="La Gioconda",
    ac="1503 - 1516",
    tecnica="Óleo",
    subt="Sfumato",
    soporte="Madera de álamo",
    autor="Leonardo da Vinci",
    estado="Regular"
)

replica = Cuadro(
    titulo="Gioconda de El Prado",
    ac="1503 - 1516",
    tecnica="Óleo",
    subt="Pincelada simple",
    soporte="Madera de nogal",
    autor="Desconocido",
    estado="Bueno"
)

# Establecer relaciones
gioconda.localizar_en(louvre)
replica.localizar_en(prado)
gioconda.agregar_replicas(replica)

# Mostrar información
print(gioconda.mostrar_info())
print()
print(replica.mostrar_info())
