
#######################################################################################################################3
# Colecciones:
#######################################################################################################################3

## deque
#########################################

### ejercicio 5: rotar una pila
from collections import deque

pila_ejercicio5 = deque()
pila_ejercicio5.append(10)
pila_ejercicio5.append(20)
pila_ejercicio5.append(30)
pila_ejercicio5.append(40)
pila_ejercicio5.append(50)

pila_ejercicio5.rotate(-3)
pila_ejercicio5.rotate(2)

print("pila con rotacion: ", pila_ejercicio5)

# ChainMap
#########################################


# Crea un ChainMap de todos esos diccionarios como inventario.
# Reporta la cantidad de algunos artículos.

# Actualiza la cantidad de uno solo de esos artículos. Reporta el nuevo valor.
# Agrega un nuevo ítem. Reporta su valor.

from collections import ChainMap

# Define los diccionarios
juegos_de_mesa = {"monopoly": 10, "jenga": 5, "risk": 2}
celulares = {"iphone": 20, "samsung": 15, "xiaomi": 7}
libros = {"novelas": 50, "poesía": 20, "historia": 30}
flores = {"rosas": 100, "margaritas": 50, "tulipanes": 30}

inventario_completo = ChainMap(juegos_de_mesa, celulares, libros, flores)

print("Cantidad de flores margaritas", inventario_completo["margaritas"])
print("Cantidad de libros de historia", inventario_completo["historia"])


print("Cantidad de libros de poesia original", inventario_completo["poesía"])
inventario_completo["novelas"] = 2
libros["poesía"] = 2
inventario_completo["televisores"] = 222
print("Cantidad de libros de poesia nueva", inventario_completo["poesía"])



print("inventario completo", inventario_completo)


# Enum: Ejercicio 3 BugStatus
#########################################

from enum import Enum

class BugStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    IN_PROGRESS = "in progress"

class Bug:
    def __init__(self, status: BugStatus):
        self.status = status

bug1 = Bug(BugStatus.OPEN)
bug2 = Bug(BugStatus.OPEN)
bug3 = Bug(BugStatus.CLOSED)
bug34 = Bug(BugStatus.IN_PROGRESS)

print("status del bug: ", bug34.status)
print("status del bug: ", bug3.status)
print("status del bug: ", bug2.status)
print("status del bug: ", bug1.status)