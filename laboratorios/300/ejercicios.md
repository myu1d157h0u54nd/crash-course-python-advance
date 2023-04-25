
########################################################################################################################
# Repaso:  funciones, clases, instancias
########################################################################################################################

#------------------------------------
## Funciones 
#------------------------------------
### Ejercicio 1:
 - Una función para calcular el costo total de un paquete de viaje.
 - La función toma como entrada el costo base del paquete, los costos adicionales como el costo del transporte, alojamiento y actividades.
 - Devuelve el costo total del paquete.

### Ejercicio 2:
 - Una función para determinar el itinerario de un viaje.
 - La función toma como entrada el destino, la duración del viaje y la fecha de inicio.
 - Devuelve una lista con el itinerario del viaje.

#------------------------------------
## Clases 
#------------------------------------
### Ejercicio 1:
 - Creando una clase para manejar reservaciones de viajes.
 - Supongamos que tienes un negocio de viajes para rememorar y necesitas una forma de manejar las reservaciones de tus clientes.
 - Crea una clase llamada Reservacion que tenga los siguientes atributos:
    nombre: el nombre del cliente
    destino: el lugar al que el cliente quiere viajar
    fecha: la fecha en la que el cliente quiere viajar
    precio: el precio de la reservación
 - La clase debe tener un método llamado: mostrar_reservacion
   - este metodo imprime en consola los detalles de la reservación.
   - También debe tener un método llamado calcular_precio que calcule el precio de la reservación basándose en el destino y la fecha.

### Ejercicio 2:
  - Crea una clase base llamada Animal con los atributos:
    - nombre y edad
  - y los métodos comer() y dormir().
  - Crea una clase derivada llamada Perro que herede de la clase Animal.
    - y agregue un método adicional llamado ladrido().
  - Finalmente, crea una instancia de Perro y llama a los métodos:
    - comer(), dormir() y ladrido().


#------------------------------------
## Decoradores 
#------------------------------------
Ejercicio, Decoradores de funciones 1
Escribe un decorador de función que compruebe si un usuario tiene permisos de administrador antes de ejecutar la función.
Si el usuario no tiene permisos de administrador, el decorador debería imprimir un mensaje de error y salir sin ejecutar la función.



#------------------------------------
## Pytest 
#------------------------------------
1. Escribe un test que compruebe que la función suma devuelve el resultado esperado para dos números enteros positivos.
2. Escribe un test que compruebe que la función division devuelve un error ZeroDivisionError cuando el segundo argumento es 0.
3. Escribe un test que compruebe que la función ordenar_palabras devuelve una lista ordenada de palabras a partir de una lista desordenada.
4. Escribe un test que compruebe que la función obtener_edad devuelve un valor numérico para una fecha de nacimiento válida.
5. Escribe un test que compruebe que la función calcular_estadisticas devuelve:
   6. una tupla con los valores mínimo, máximo y promedio a partir de una lista de números.

# informacion util:
 - NameError: cuando se intenta acceder a una variable o función que no está definida.
 - TypeError: cuando se utiliza un objeto de un tipo incorrecto.
 - ValueError: cuando se utiliza un valor que es de un tipo correcto pero tiene un valor inapropiado.
 - IndexError: cuando se intenta acceder a un índice fuera de rango en una lista o tupla.
 - KeyError: cuando se intenta acceder a una clave que no existe en un diccionario.
 - FileNotFoundError: cuando se intenta abrir un archivo que no existe.
 - AssertionError: cuando una afirmación en el test falla.
 - TimeoutError: cuando una función toma más tiempo del esperado para completar su tarea.
 - KeyboardInterrupt: cuando se interrumpe el proceso con Ctrl + C.

