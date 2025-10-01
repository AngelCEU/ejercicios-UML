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
        info = f"Nombre: {self.nombre}\nApellido: {self.apellido}\n"
        if self.apellido_nacimiento:
            info += f"Apellido de nacimiento: {self.apellido_nacimiento}\n"
        info += f"Sexo: {self.sexo}\n"
        if self.conyuge:
            info += f"Casado con: {self.conyuge.nombre} {self.conyuge.apellido}\n"
        if self.hijos:
            info += "Hijos: " + ", ".join([h.nombre for h in self.hijos]) + "\n"
        return info


# Crear personas
kate = Persona("Kate", "Windsor", "Mujer", "Middleton")
guillermo = Persona("Guillermo", "Windsor", "Hombre")
carlos = Persona("Carlos", "Windsor", "Hombre")
diana = Persona("Diana", "Windsor", "Mujer", "Spencer")

# Establecer matrimonios
kate.casar(guillermo)
carlos.casar(diana)

# Establecer relación de hijos
carlos.agregar_hijo(guillermo)
diana.agregar_hijo(guillermo)

# Mostrar información
print(kate.mostrar_info())
print(guillermo.mostrar_info())
print(carlos.mostrar_info())
print(diana.mostrar_info())

