
########################################################################################################################
# Documentation:
########################################################################################################################
"""
Esto es un comentario
siempre que este dentro de las triple comillas
puedo seguir escribiendo
"""
import unittest


def funcion(x, y):
    # logica de metodo
    resultado = True
    return resultado



def funcion(x, y):
    """
    :param numero int x:
    :param numero int y:
    :return:
        int, la suma de x + y
    """
    return x + y

########################################################################################################################
# Logger o Logging
########################################################################################################################

import logging

logging.basicConfig(filename="logFileBuenasPracticas-all.log", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.ERROR)
#logging.basicConfig(filename="logFileBuenasPracticas-critical.log", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.CRITICAL)
# logging.basicConfig(filename="logFileBuenasPracticas-error.log", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.ERROR)
#logging.basicConfig(filename="logFileBuenasPracticas-warning.log", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.WARNING)
# logging.basicConfig(filename="logFileBuenasPracticas-info.log", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
# logging.basicConfig(filename="logFileBuenasPracticas-debug.log", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# mensajes de prueba
logging.debug("este es un msg de nivel: debug")
logging.info("este es un msg de nivel: info")
logging.warning("este es un msg de nivel: warning")
logging.error("este es un msg de nivel: error")
logging.critical("este es un msg de nivel: critical")


########################################################################################################################
# Testing en python: pytest
########################################################################################################################

# pip install pytest

# funcion del negocio

def sumar(a, b):
    """
    sumar dos numeros: a + b
    return resultado
    """
    resultado = a + b
    return resultado

from unittest import TestCase
# from funcionesDelProyecto import metodo

class TestSuma(unittest.TestCase):

    def test_suma_entero_y_string(self):
        with self.assertRaises(TypeError):
            resultado = sumar(2, "texto")

    def test_personalizacion_suma_simple(self):
        self.assertEquals(sumar(2, 3), 5)

    def test_suma_negativa(self):
        self.assertEquals(sumar(-1, -4), -5)

    def test_suma_str(self):
        resultado = sumar("hola ", "mundo")
        self.assertEquals(resultado, "hola mundo")




########################################################################################################################
# Testing en python: pytest + mocks
########################################################################################################################

import requests

def get_clima(ciudad):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid=API_KEY'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["main"]["temp"]
    else:
        return None

import unittest
from unittest.mock import patch

class TestClima(unittest.TestCase):
    @patch("app.request.get")
    def test_get_clima(self, mock_get):
        mock_data = {"main": {"temp": 34}}
        mock_response = type("MockResponse", (), {"status_code": 200, "json": lambda self: mock_data})
        mock_get.return_value = mock_response
        result = get_clima("Barcelona")
        print(result)
        self.assertEquals(result, 34)


