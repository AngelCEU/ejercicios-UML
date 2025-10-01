#ejercicio1
from Ejerccio1.ejercicio1 import Circulo
from Ejerccio1.ejercicio1 import Cuadrado
from Ejerccio1.ejercicio1 import Rectangulo
from Ejerccio1.ejercicio1 import Elipse

circulo_negro = Circulo(color="negro", diametro=1)
rectangulo_naranja = Rectangulo(color="naranja", longitud=3, anchura=1)
cuadrado_azul = Cuadrado(color="azul", longitud=1.5)
elipse_amarilla = Elipse(color="amarillo", eje_mayor=3, eje_menor=1)

print(f"El círculo es de color {circulo_negro.color} y tiene un diámetro de {circulo_negro.diametro}.")

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#ejercicio2
from ejercicio2.ejercicio2 import Persona

kate = Persona("Kate", "Windsor", "Mujer", "Middleton")
guillermo = Persona("Guillermo", "Windsor", "Hombre")
carlos = Persona("Carlos", "Windsor", "Hombre")
diana = Persona("Diana", "Windsor", "Mujer", "Spencer")

kate.casar(guillermo)
carlos.casar(diana)

carlos.agregar_hijo(guillermo)
diana.agregar_hijo(guillermo)

print(kate.mostrar_info())
print(guillermo.mostrar_info())
print(carlos.mostrar_info())
print(diana.mostrar_info())

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#ejercicio3
from ejercicio3.ejercicio3 import Lugar
from ejercicio3.ejercicio3 import Cuadro

louvre = Lugar("Museo del Louvre", "Paris", "Francia")
prado = Lugar("Museo del Prado", "Madrid", "España")

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

gioconda.localizar_en(louvre)
replica.localizar_en(prado)
gioconda.agregar_replicas(replica)

print(gioconda.mostrar_info())
print()
print(replica.mostrar_info())

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#ejercicio4
from ejercicio4.ejercicio4 import Lugar
from ejercicio4.ejercicio4 import EtapaConstruccion
from ejercicio4.ejercicio4 import Edificio  


santiago = Lugar("Santiago de Compostela", "Galicia", "España")

catedral = Edificio(
    nombre="Catedral de Santiago de Compostela",
    culto="Católico",
    material="Granito",
    estilos=["Románico", "Gótico", "Barroco", "Plateresco", "Neoclásico"],
    fecha_primera_consg=1128,
    fecha_segunda_consg="3 de abril de 1211",
    fecha_declaracion_bic=1896
)

catedral.localizar_en(santiago)

etapa1 = EtapaConstruccion(1075, 1122)
etapa2 = EtapaConstruccion(1168, None)

catedral.agregar_etapa(etapa1)
catedral.agregar_etapa(etapa2)

print(catedral.mostrar_info())

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#ejercicio6
from ejercicio6.ejercicio6 import persona

maria=persona("Maria", "Garcia", "Pereda", "01/01/1970", "F", "12345678A")
print(maria.nombre)
print(maria.primer_apellido)
print(maria.segundo_apellido)
print(maria.fecha_nacimiento)
print(maria._sexo)
print(maria.numero_identificador)

#-----------------------------------------------------------------------------------------------------------------------------------------------------