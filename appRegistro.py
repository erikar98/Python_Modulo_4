
from datetime import datetime

fecha_actual = datetime.now()

def mostrar_usuarios_invalidos():
    try:
        ARCHIVO = "./usuarios.txt"
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay usuarios registrados.")
                return

            print("\nUsuarios con formato inválido:")
            for linea in lineas:
                partes = linea.strip().split(",")
                if len(partes) != 3:
                    registrar_log_(f"Mostrar usuarios inválidos - Formato de línea inválido: {linea.strip()}, Fecha: {fecha_actual}", "info")
                    print(f"Formato de línea inválido: {linea.strip()}")

    except FileNotFoundError:
        registrar_log_(f"Mostrar usuarios inválidos fallido - Archivo de usuarios no encontrado, Fecha: {fecha_actual}", "error")
        print("No se encontró el archivo de usuarios")
    except PermissionError:
        registrar_log_(f"Mostrar usuarios inválidos fallido - Permisos insuficientes para leer el archivo, Fecha: {fecha_actual}", "error")
        print("No se tienen permisos para leer el archivo.")
    except Exception as error:
        registrar_log_(f"Mostrar usuarios inválidos fallido - Error inesperado: {error}, Fecha: {fecha_actual}", "error")
        print(f"Ocurrió un error inesperado: {error}")

def eliminar_usuario():
    try:
        ARCHIVO = "./usuarios.txt"
        nombre_eliminar = input("Ingrese el nombre del usuario a eliminar: ")
        if nombre_eliminar == "":
            print("El nombre no puede estar vacío.")
            return

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        with open(ARCHIVO, "w", encoding="utf-8") as archivo:
            eliminado = False
            for linea in lineas:
                partes = linea.strip().split(",")
                if len(partes) != 3:
                    if partes[0] == nombre_eliminar:
                        eliminado = True
                    else:
                        archivo.write(linea)
                    continue
                nombre, edad, fecha = partes
                if nombre != nombre_eliminar:
                    archivo.write(linea)
                else:
                    eliminado = True

        if eliminado:
            registrar_log_(f"Usuario '{nombre_eliminar}' eliminado exitosamente, Fecha: {fecha_actual}", "info")
            print("Usuario eliminado exitosamente.")
        else:
            registrar_log_(f"Eliminar usuario - Usuario '{nombre_eliminar}' no encontrado, Fecha: {fecha_actual}", "info")
            print("Usuario no encontrado.")

    except FileNotFoundError:
        registrar_log_(f"Eliminar usuario fallido - Archivo de usuarios no encontrado, Fecha: {fecha_actual}", "error")
        print("No se encontró el archivo de usuarios")
    except PermissionError:
        registrar_log_(f"Eliminar usuario fallido - Permisos insuficientes para escribir en el archivo, Fecha: {fecha_actual}", "error")
        print("No se tienen permisos para escribir en el archivo.")
    except Exception as error:
        registrar_log_(f"Eliminar usuario fallido - Error inesperado: {error}, Fecha: {fecha_actual}", "error")
        print(f"Ocurrió un error inesperado: {error}")

def estadistica_usuarios(opcion_estadistica):
    try:
        ARCHIVO = "./usuarios.txt"
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay usuarios registrados.")
                return

            if opcion_estadistica == "1":
                cantidad_usuarios = len(lineas)
                print(f"Cantidad de usuarios registrados: {cantidad_usuarios}")
            elif opcion_estadistica == "2":
                total_edad = 0
                for linea in lineas:
                    partes = linea.strip().split(",")
                    if len(partes) != 3:
                        registrar_log_(f"Estadísticas de usuarios - Formato de línea inválido: {linea.strip()}, Fecha: {fecha_actual}", "error")
                        continue
                    nombre, edad, fecha = partes
                    total_edad += int(edad)
                edad_promedio = total_edad / len(lineas)
                print(f"Edad promedio de los usuarios: {edad_promedio:.2f}")
    except FileNotFoundError:
        registrar_log_(f"Estadísticas de usuarios fallido - Archivo de usuarios no encontrado, Fecha: {fecha_actual}", "error")
        print("No se encontró el archivo de usuarios")
    except PermissionError:
        registrar_log_(f"Estadísticas de usuarios fallido - Permisos insuficientes para leer el archivo, Fecha: {fecha_actual}", "error")
        print("No se tienen permisos para leer el archivo.")
    except Exception as error:
        registrar_log_(f"Estadísticas de usuarios fallido - Error inesperado: {error}, Fecha: {fecha_actual}", "error")
        print(f"Ocurrió un error inesperado: {error}")
    

def registrar_log_(mensaje, tipo):

    if tipo == "error":
        LOG_FILE = "./logs_error.txt"
    else:
        LOG_FILE = "./logs_info.txt"
    
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"{mensaje}, Fecha: {fecha_actual}\n")

def registrar_usuario():
    try:
        ARCHIVO = "./usuarios.txt"
       
        nombre = input("Ingrese el nombre del usuario:")
        if nombre == "":
            print("El nombre no puede estar vacío.")
            return
        edad = int(input("Ingrese la edad del usuario:"))
        if edad < 0:
            print("La edad no puede ser negativa.")
            return

        registrar_log_(f"Intento de registro - Nombre: {nombre}, Edad: {edad}, Fecha: {fecha_actual}", "info")

        if evitar_duplicados(nombre):
            registrar_log_(f"Registro fallido - Usuario duplicado: {nombre}, Fecha: {fecha_actual}", "error")
            print("El usuario ya está registrado, no se registrará de nuevo.")
            return

        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad},{fecha_actual}\n")

        registrar_log_(f"Registro exitoso - Nombre: {nombre}, Edad: {edad}, Fecha: {fecha_actual}", "info")
        print("Usuario registrado exitosamente.")

    except ValueError:

        registrar_log_(f"Registro fallido - Edad no numérica: {edad}, Fecha: {fecha_actual}", "error")
        print("La edad debe de ser numérica")
    except PermissionError:
        registrar_log_(f"Registro fallido - Permisos insuficientes para escribir en el archivo, Fecha: {fecha_actual}", "error")
        print("No se tienen permisos para escribir en el archivo.")
    except FileNotFoundError:
        registrar_log_(f"Registro fallido - Archivo de usuarios no encontrado, Fecha: {fecha_actual}", "error")
        print("No se encontró el archivo de usuarios")
    except Exception as error:
        registrar_log_(f"Registro fallido - Error inesperado: {error}, Fecha: {fecha_actual}", "error")
        print(f"Ocurrió un error inesperado: {error}")


def mostrar_usuarios():
    try:
        ARCHIVO = "./usuarios.txt"
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay usuarios registrados.")
                return

            print("\nUsuarios registrados:")
            for linea in lineas:
                partes = linea.strip().split(",")
                if len(partes) != 3:
                    registrar_log_(f"Mostrar usuarios fallido - Formato de línea inválido: {linea.strip()}, Fecha: {fecha_actual}", "error")
                    print(f"Formato de línea inválido: {linea.strip()}")
                    continue
                nombre, edad, fecha = partes
                print(f"Nombre: {nombre}, Edad: {edad}, Fecha: {fecha}")
            registrar_log_(f"Usuarios mostrados exitosamente, Fecha: {fecha_actual}", "info")
    except FileNotFoundError:
        registrar_log_(f"Mostrar usuarios fallido - Archivo de usuarios no encontrado, Fecha: {fecha_actual}", "error")
        print("No se encontró el archivo de usuarios")
    except PermissionError:
        registrar_log_(f"Mostrar usuarios fallido - Permisos insuficientes para leer el archivo, Fecha: {fecha_actual}", "error")
        print("No se tienen permisos para leer el archivo.")
    except Exception as error:
        registrar_log_(f"Mostrar usuarios fallido - Error inesperado: {error}, Fecha: {fecha_actual}", "error")
        print(f"Ocurrió un error inesperado: {error}")

def buscar_usuario():
    try:
        ARCHIVO = "./usuarios.txt"
        nombre_buscar = input("Ingrese el nombre del usuario a buscar: ")
        if nombre_buscar == "":
            print("El nombre no puede estar vacío.")
            return

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            encontrado = False
            for linea in lineas:
                partes = linea.strip().split(",")
                if len(partes) != 3:
                    registrar_log_(f"Buscar usuario fallido - Formato de línea inválido: {linea.strip()}, Fecha: {fecha_actual}", "error")
                    print(f"Formato de línea inválido: {linea.strip()}")
                    continue
                nombre, edad, fecha = partes
                if nombre == nombre_buscar:
                    registrar_log_(f"Busqueda de usuario '{nombre_buscar}' realizada, Resultado: Encontrado, Fecha: {fecha_actual}", "info")
                    print(f"Usuario encontrado - Nombre: {nombre}, Edad: {edad}, Fecha: {fecha}")
                    encontrado = True
                    break
            if not encontrado:
                registrar_log_(f"Busqueda de usuario '{nombre_buscar}' realizada, Resultado: No encontrado, Fecha: {fecha_actual}", "info")
                print("Usuario no encontrado.")

    except FileNotFoundError:
        registrar_log_(f"Buscar usuario fallido - Archivo de usuarios no encontrado, Fecha: {fecha_actual}", "error")
        print("No se encontró el archivo de usuarios")
    except PermissionError:
        registrar_log_(f"Buscar usuario fallido - Permisos insuficientes para leer el archivo, Fecha: {fecha_actual}", "error")
        print("No se tienen permisos para leer el archivo.")
    except Exception as error:
        registrar_log_(f"Buscar usuario fallido - Error inesperado: {error}, Fecha: {fecha_actual}", "error")
        print(f"Ocurrió un error inesperado: {error}")

def evitar_duplicados(nombre):
    try:
        ARCHIVO = "./usuarios.txt"
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                partes = linea.strip().split(",")
                if len(partes) != 3:
                    registrar_log_(f"Evitar duplicados - Formato de línea inválido: {linea.strip()}, Fecha: {fecha_actual}", "error")
                    continue
                nombre_existente, edad, fecha = partes
                if nombre_existente == nombre:
                    registrar_log_(f"Evitar duplicados - Usuario duplicado encontrado: {nombre}, Fecha: {fecha_actual}", "info")
                    return True
        return False
    except FileNotFoundError:
        registrar_log_(f"Evitar duplicados - Archivo de usuarios no encontrado, Fecha: {fecha_actual}", "error")
        return False
    except Exception as error:
        registrar_log_(f"Evitar duplicados - Error inesperado: {error}, Fecha: {fecha_actual}", "error")
        print(f"Ocurrió un error inesperado: {error}")
        return False


def menu():
    opcion = ""
    
    while opcion != "7":
        print("\n ==== USUARIOS ====")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario por nombre")
        print("4. Estadísticas de usuarios (cantidad y edad promedio)")
        print("5. Eliminar usuario por nombre")
        print("6. Mostrar usuarios con formato inválido")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            print("\n ==== Elija una opción ====")

            print("1. Saber la cantidad de usuarios registrados")
            print("2. Mostrar la edad promedio de los usuarios")
            print("3. Volver al menú principal")
            opcion_estadistica = input("Seleccione una opción: ")

            if opcion_estadistica == "1" or opcion_estadistica == "2":
                estadistica_usuarios(opcion_estadistica)
            elif opcion_estadistica == "3":
                continue
        elif opcion == "5":
            eliminar_usuario()
        elif opcion == "6":
            mostrar_usuarios_invalidos()
        elif opcion == "7":
            print("Programa finalizado.")
        else:
            print("Opción no válida. Intente nuevamente.")

menu()