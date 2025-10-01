class persona:
    def __init__ (self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, _sexo, numero_identificador):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self._sexo = _sexo
        self.numero_identificador = numero_identificador


maria=persona("Maria", "Garcia", "Pereda", "01/01/1970", "F", "12345678A")

