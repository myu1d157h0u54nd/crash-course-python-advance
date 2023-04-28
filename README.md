# Curso acelerado de Python avanzado

## Requisitos previos:
Requisitos previos
Antes de empezar el curso, es necesario tener conocimientos básicos de programación en Python, como los que se pueden adquirir en un curso introductorio. Además, se requiere tener instalado Python y algunas librerías que se especificarán durante el curso. También se recomienda tener conocimientos básicos de programación orientada a objetos y del protocolo HTTP para el módulo de Python como servidor de APIs.

# Temario: 

## 100 Gestión de dependencias y workspaces
- Instalar y cambiar entre diferentes versiones de Python en la misma máquina
- Gestión de dependencias
  - Entornos virtuales
  - Docker
- Ejercicios

## 150 Colecciones (Collections)
- Chainmap
- Counter
- OrderedDict
- defaultdict

## 200 POO en Python:
- funciones
  - parametros: (*args), (**kwargs), (*args, **kwargs) 
  - Funciones lambda
- clases
  - El parámetro "self" en métodos de clases
  - Instancias de clase (Objetos)
    - Como acceder a sus atributos o métodos
  - Herencia en subclases
    - Clase (padre) y subclase (hija)
    - Métodos y atributos heredados
    - Encapsulamiento en clases

## 250 Decorators y wrapper
- Diferencias entre decoradores y wrapper
- Wrappers
- Decoradores de funciones
- Decoradores de clases

## 300 Buenas prácticas
- Documentation
- logging 
- testing
  - pytest
    - Assert: ()
    - Exception: error (TypeError, ValueError, IndexError, KeyError, AttributeError, ZeroDivisionError)
      - Exception (custom)
  - Resolviendo test unitarios con simulacion
    - Mocks (libreria)
      - Mocking de una dependencia externa
      - Mocking de objetos internos
    - Monkey Patch (tecnica)
- El ZEN de Python

## 400 WEB y conceptos fundamentales
- Servicios web
  - Características técnicas de SOAP y REST
  - Protocolo HTTP
    - Tabla con los métodos HTTP más comunes y su descripción
    - Tabla con los códigos de estado HTTP más comunes
  - Proceso de comunicación HTTP
    - Formatos de respuesta en webservices
      - json
      - xml
      - yaml
- Python como cliente de APIs
  - GET request
  - POST request
  - Serializando y deserializando datos JSON

## 500 Python como servidor de APIs
- Flask:
  - ¿Qué es Flask?
  - Estructura de una aplicación Flask
    - ¿Cómo funciona una aplicación Flask?
      - Estructura de una aplicación Flask
      - Route: definición de rutas
        - Rutas dinámicas y reglas variables
  - app_flask_blog
    - rutas estáticas
    - rutas dinámicas (simples y anidadas)
  - app_flask_api (espocision de metodos HTTP)
    - GET, POST, DELETE
  - Autenticación y autorización en Flask API Restful
    - Autenticación y autorización
  - Integración con plantillas y Jinja2
    - Su uso en FrontEnd
    - ¿Y entonces en BackEnd que?

## 600 Optimización del procesamiento
- Generadores
  - Escenario para procesar archivos no binarios (string)
  - Escenario para procesar videos (archivos binarios)
- List Comprehensions

## 650 Concurrencia y Paralelismo
- AsyncIO
- Multiproceso
- Multihilo

## Python 2 vs Python 3
 - Diferencias de sintaxis
 - Prepara el código para facilitar la migración y migración de código entre versiones

# Licencia
Este material está licenciado bajo la licencia Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional. Esto significa que puedes compartir, copiar y redistribuir el material en cualquier medio o formato siempre que des crédito al autor original y que no se use con fines comerciales. No tienes permitido imprimir ni modificar el material, pero sí puedes citarlo enlaces o fragmentos.

Para más información sobre esta licencia, puedes visitar:
  - https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es.

# Quien soy?

Soy un experto en DevOps y soporte técnico con experiencia en industrias de ciberseguridad, bancaria y telecomunicaciones. Me especializo en linux sysadmin, desarrollo de DevOPs y liderazgo de equipos.

Tengo habilidades técnicas y tecnologías en roles de SysAdmin, RPA y DevOps, incluyendo Linux, Jenkins, Pytest, Ansible, Docker y Kubernetes. 

Actualmente, estoy enfocado en profundizar mis conocimientos en Kubernetes y proyectos de CI/CD, con una fuerte atención a la gestión de riesgos y seguridad en todo lo que hago.

Estoy emocionado por la oportunidad de aplicar mis habilidades y conocimientos en un nuevo desafío.

## Contacto
Pueden contactar conmigo en:

  * [LinkedIn](https://www.linkedin.com/in/nikoslastra/)
  * [Email](mailto:lastra.nikos@gmail.com)

## Colaboración
Estoy abierto a avisos sobre mejoras y colaboraciones dentro de pull requests al repositorio para sumar y colaborar en el contenido.
Estas colaboraciones no darán derechos sobre el material final, pero sí figurarán en la sección de colaboradores.

## Contribución
Estoy abierto a dar consultorías y responder a solicitudes para brindar talleres.
También puedo recibir donativos en el siguiente enlace:
  * [Donativos](https://ayudar.ar/nikosbluelion)
