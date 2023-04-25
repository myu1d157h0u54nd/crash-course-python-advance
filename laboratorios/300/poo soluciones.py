# Una función para calcular el costo total de un paquete de viaje.
# La función toma como entrada el costo base del paquete, los costos adicionales como el costo del transporte, alojamiento y actividades.
# Devuelve el costo total del paquete.

def costoTotal (costoBasePAquete, costoTransporte, costoAlojamiento, costoActividades):
    resultadoCostoTotal = costoBasePAquete + costoTransporte + costoAlojamiento + costoActividades
    return resultadoCostoTotal

viajeAlaCosta = costoTotal(150, 100, 200, 50)
print("El costo total del viaje a la costa", viajeAlaCosta)

#   - Crea una clase base llamada Animal con los atributos:
#    - nombre y edad
#  - y los métodos comer() y dormir().
#  - Crea una clase derivada llamada Perro que herede de la clase Animal.
#    - y agregue un método adicional llamado ladrido().
#  - Finalmente, crea una instancia de Perro y llama a los métodos:
#    - comer(), dormir() y ladrido().

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f"{self.nombre} esta comiendo")

    def dormir(self):
        print(f"{self.nombre} esta durmiendo")

class Perro(Animal):
    def ladrido(self):
        print(f"{self.nombre} esta ladrando")

elPerroVecino = Perro("molesto", 4)
elPerroVecino.ladrido()

