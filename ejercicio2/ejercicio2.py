class Persona:
    def __init__(self, nombre, apellido, sexo, apellido_nacimiento=None):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.apellido_nacimiento = apellido_nacimiento
        self.conyuge = None
        self.hijos = []

    def casar(self, otra_persona):
        self.conyuge = otra_persona
        otra_persona.conyuge = self

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.sexo})"

    def mostrar_info(self):
        return "\n".join(filter(None, [
            f"Nombre: {self.nombre}",
            f"Apellido: {self.apellido}",
            f"Apellido de nacimiento: {self.apellido_nacimiento}",
            f"Sexo: {self.sexo}",
            f"Casado con: {self.conyuge.nombre} {self.conyuge.apellido}",
            f"Hijos: " + ", ".join(h.nombre for h in self.hijos)
        ]))



