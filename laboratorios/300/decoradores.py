

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








########################################################################################################################
# Decoradores
########################################################################################################################



