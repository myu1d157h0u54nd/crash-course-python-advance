
########################################################################################################################
# Decoradores
########################################################################################################################


# decoradores:
    # de funciones, o metodos
    # de clases o sus propiedades

# wrappers

def myLogger(func):
    import logging
    logging.basicConfig(filename="myloggerpractica.log", level=logging.INFO)

    def wrapper (*args, **kwargs):
        logging.info(f"Funcion de nombre {func.__name__} con los argumentos={args}, y kwargs={kwargs}")
        return func(*args, **kwargs)

    return wrapper
@myLogger
def add(a, b):
    return a + b

#resultado = add(2, "a")
#print(resultado)

#resultado = add(22, 3)
#print(resultado)

#resultado = add(2, 3, 3)
#print(resultado)


# Decoradores en funciones

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"La funcion {func.__name__} tardo {end_time - start_time} segundos en ejecutarse ")
        return result
    return wrapper

#@segundoDecorador
#@decoradoresALaN
@timer
def funcionEjemplo(sleep):
    time.sleep(sleep)

#funcionEjemplo(1)
#funcionEjemplo(2)
#funcionEjemplo(3)
#funcionEjemplo(4)

# Decoradores de clases

def contadorIntancias(clase):
    class NuevaClase(clase):
        contador = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            NuevaClase.contador += 1

        def __del__(self):
            NuevaClase.contador -= 1

    return NuevaClase

@contadorIntancias
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Nicolas", 42)
print("Contador de Instancias: ", Persona.contador)

personaHermano1 = Persona("Ignacio", 37)
print("Contador de Instancias: ", Persona.contador)

personaHermano2 = Persona("Horacio", 37)
print("Contador de Instancias: ", Persona.contador)

personaHermano3 = Persona("Carlos", 37)
print("Contador de Instancias: ", Persona.contador)

del personaHermano1
personaHermano2.__del__()
personaHermano3.__del__()
print("Contador de Instancias: ", Persona.contador)