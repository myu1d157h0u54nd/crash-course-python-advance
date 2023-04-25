
########################################################################################################################
# Decoradores
########################################################################################################################

# Ejercicio, Decoradores de funciones 1
# Escribe un decorador de función que compruebe si un usuario tiene permisos de administrador antes de ejecutar la función.
# Si el usuario no tiene permisos de administrador, el decorador debería imprimir un mensaje de error y salir sin ejecutar la función.


class User:
    def __init__(self, is_admin=False):
        self.is_admin = is_admin

def checkAdmin(func):
    def wrapper(user, *arg, **wkargs):
        if user.is_admin:
            return func(*arg, **wkargs)
        else:
            print(f"Error: Acceso denegado. User {user} trato de utilizar el metodo {func}")
    return wrapper

@checkAdmin
def funcionProtegida_require_admin():
    print("Acceso permitido")
    print("El proceso se ejecuto exitosamente")

# pruebas user no admin
userNoAdmin = User(is_admin=False)
funcionProtegida_require_admin(userNoAdmin)

# pruebas user admin
userAdmin = User(is_admin=True)
funcionProtegida_require_admin(userAdmin)

