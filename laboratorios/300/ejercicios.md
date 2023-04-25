
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
 - Creando una subclase para manejar reservaciones de hotel.
 - Ahora supongamos que también ofreces reservaciones de hotel a tus clientes.
 - Crea una subclase llamada: ReservacionHotel
   - Que herede de la clase Reservacion y agregue un atributo llamado duracion.
     - Este atributo debe representar la cantidad de noches que el cliente desea quedarse en el hotel.
 - El método calcular_precio debe ser sobreescrito para tomar en cuenta la duración de la estadía y el precio por noche del hotel.


