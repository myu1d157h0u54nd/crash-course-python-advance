import char as char

#######################################################################################################################3
# repaso de colecciones basicas:
#######################################################################################################################3

# listas

mi_lista = ["nombre", "ciudad: Madrid", 1, 2, 3]
elmento = mi_lista[1]
print(elmento)

## tuple
mi_tupla = (1, 2, 3, "libros", "peliculas")
print(mi_tupla[3])

## set
estudiantes_ids = {23, 24, 26, 33, 55}
print ("Ids de estudiantes: ", estudiantes_ids)

### set add
estudiantes_ids.add (999)
print ("Ids de estudiantes actualizados: ", estudiantes_ids)


## diccionarios:
id_de_ciudades = {1: "Madrid", 2: "Barcelona", 3: "Paris", 4: "Roma"}
nombre_ciudad_2 = id_de_ciudades[2]
print(nombre_ciudad_2)

#######################################################################################################################3
# Colecciones:
#######################################################################################################################3

## deque
#########################################
from collections import deque
import collections

pila = deque()
pila.append("a")
pila.append("b")
pila.append("c")

print("Mi pila de datos: ", pila)
primer_elemento = pila.popleft()
print(primer_elemento)
print(pila)

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
from collections import ChainMap

dict1 = {"a": "Barcelona", "b": "Madrid", "c": "Paris"}
dict2 = {"d": "frutas", "e": "Libros", "f": "Peliculas"}
dict3 = {"g": "flores", "h": "ruedas"}

diccionario_encadenados = ChainMap(dict1, dict2)

print("diccionario_encadenados")
print(diccionario_encadenados["a"])
print(diccionario_encadenados["b"])
print(diccionario_encadenados["c"])
print(diccionario_encadenados["d"])
print(diccionario_encadenados["e"])
print(diccionario_encadenados["f"])

# Counter
#########################################

## contador de datos tipo int
from collections import Counter

lista_sin_concurrencias = [1, 2, 3, 6, 7, 8, 11, 22, 33]
lista_con_concurrencias = [1, 2, 3, 6, 7, 8, 2, 3, 6, 7, 8, 2, 3, 6, 7, 8, 2, 3, 6, 7, 8]

contador = Counter(lista_con_concurrencias)
print(contador)

## contador de datos tipo string
from collections import Counter

texto = "No hay sueño mas grande en la vida que el sueño del regreso. El mejor camino es el camino de vuelta, que es también el camino imposible."
palabras = texto.split()

contador_de_palabras = Counter(palabras)

print ("Contador de palabras: ", contador_de_palabras)
print ("top 5 de palabras repetidas: ", contador_de_palabras.most_common(5))

# Orderedict
#########################################

from collections import OrderedDict

# ejemplo 1

normal_dic1 = {"b": 2, "a": 1, "c": 3}
print("diccionario mornal: ", normal_dic1)

diccionario_ordenado = OrderedDict(sorted(normal_dic1.items()))

print("diccionario original: ", normal_dic1)
print("diccionario ordenado: ", diccionario_ordenado)

# ejemplo 2

normal_dic2 = {"b": 2, "a": 1, "c": 3}
print("diccionario 2 mornal: ", normal_dic2)

diccionario_ordenado = OrderedDict(normal_dic1)

print("diccionario 2 original: ", normal_dic2)
print("diccionario 2 ordenado: ", diccionario_ordenado)

# defaultdict
#########################################

# ejemplo 1
from collections import defaultdict

texto = "Hola Mundo"
diccionario = defaultdict(int)

for caracter in texto:
    diccionario[caracter] += 1

print("Mi diccionario: ", diccionario)


# ejemplo 2
from collections import defaultdict

diccionario = defaultdict(list)
diccionario["frutas"].append("Tomate")
diccionario["frutas"].append("Bananda")
diccionario["verduras"].append("Limon")
diccionario["verduras"].append("Zanahoria")

print(diccionario)

########################################################################################################################
# enum
########################################################################################################################

from enum import Enum

class DiasSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def obtener_dia_habil(dia: DiasSemana) -> bool:
    return dia.value < 6

print(obtener_dia_habil(DiasSemana.LUNES))
print(obtener_dia_habil(DiasSemana.MARTES))
print(obtener_dia_habil(DiasSemana.MIERCOLES))
print(obtener_dia_habil(DiasSemana.JUEVES))
print(obtener_dia_habil(DiasSemana.VIERNES))
print(obtener_dia_habil(DiasSemana.SABADO))
print(obtener_dia_habil(DiasSemana.DOMINGO))