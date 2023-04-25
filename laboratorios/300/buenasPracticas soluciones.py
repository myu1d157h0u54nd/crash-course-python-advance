import pytest


########################################################################################################################
# Pytest y test unitarios
########################################################################################################################

# 3. Escribe un test que compruebe que la función ordenar_palabras devuelve una lista ordenada de palabras a partir de una lista desordenada.


def ordenar(lista):
    return sorted(lista)

from unittest import TestCase
class TestEjercicios(TestCase):
    def test_order_palabras(self):
        lista_de_palabras = ["banco", "casa", "arbol"]
        assert ordenar(lista_de_palabras) == ["arbol", "banco", "casa"]


# 2. Escribe un test que compruebe que la función division devuelve un error ZeroDivisionError cuando el segundo argumento es 0.

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

def test_division():
    with pytest.raises(ZeroDivisionError):
        division(4, 0)
    assert division(8, 2) == 4


