

########################################################################################################################
# Repaso de funciones, clases, y objetos
########################################################################################################################

# funcion ejemplo base
def nombreDeMiFuncion(arguntamento1, argumento2):
    # logica de negocio, o funcion
    resultado = arguntamento1 + argumento2
    return resultado

# funcion con parametros

def funcionConMasPArametro(*args):
    # logica de negocio, o funcion
    for un_solo_argumento in args:
        print(un_solo_argumento)
        resultado = resultado + un_solo_argumento
    return resultado



def funcionEjemplokwargs(**kwargs):
    # logica de negocio, o funcion

    for key, value in kwargs.items():
        print(key, value)

print(funcionEjemplokwargs(nombre="Nikos", edad=42))



def funcionEjemplokwargs(*args, **kwargs):
    # logica de negocio, o funcion

    for un_solo_argumento in args:
        print(un_solo_argumento)

    for key, value in kwargs.items():
        print(key, value)

print(funcionEjemplokwargs(1, 2, 3, nombre="Nikos", edad=42))

# funcion lambda

datos = [("Juan", 25), ("Ana", 34), ("Carlos", 22)]

datos_ordenados = sorted(datos, key=lambda x: x[1])

print(datos_ordenados)

# Clases

class MiClase:
    def query_select_a_db():
        pass
        return True
        # init de DB
        #logica de la query"

# miObjetoDeClase = MiClase(arg1,arg2)

# miObjetoDeClase.atributo_2
# miObjetoDeClase.query_select_a_db()

# Clases y Objetos:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

empleado_id_1 = Persona("Juan", 23)

empleado_id_1.saludar()

# Herencias en subclases

# class Superclase:
    # definicion de atributos y metodos

# class Subclase:
    # Heredando atributos y metodos
    # Opcional:
        # Crear nuevos metodos y atributos
        # Sobreescribir: los metodos y atributos

# Ejemplo de herencia

class Vehiculo:
    # constructor
    def __init__(self, fabricante, modelo, year, motor):
        self.fabricante = fabricante
        self.modelo = modelo
        self.year =  year
        self.motor = motor
        self.velocidad = 0

    def arrancar(self):
        print("Arrancar el motor")

    def apagar(self):
        print("Apagar el motor")

    def acelerar(self):
        self.velocidad +=10
        print(f"Acelerando a {self.velocidad} km/h")

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 10
            print(f"El auto comienza a frenar")
        else:
            print(f"El auto se ah detenido")

class VehiculoElectrico(Vehiculo):
    def __init__(self, fabricante, modelo, year, reservaCombustible ):
        super().__init__(fabricante, modelo, year, motor)
        self.reservaCombustible = reservaCombustible

    def electricidad(self):
        self.carga = 110
        print(f"El auto carga combustible")

# Crear instancia de un auto a combustible fosil
# fabricante, modelo, year, motor):
FordFocus = Vehiculo("Ford", "Focus", 2010, "1.6")

FordFocus.arrancar()
FordFocus.acelerar()
FordFocus.acelerar()
FordFocus.acelerar()
FordFocus.frenar()








