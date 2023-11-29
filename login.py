import json
import sys

# Función para cargar los usuarios desde el archivo JSON
def cargar_usuarios():
    with open('usuarios.json') as archivo:
        datos = json.load(archivo)
        return datos['usuarios']

# Función para guardar los usuarios en el archivo JSON
def guardar_usuarios(usuarios):
    datos = {'usuarios': usuarios}
    with open('usuarios.json', 'w') as archivo:
        json.dump(datos, archivo)

# Función para mostrar la lista de usuarios en orden ascendente o descendente
def mostrar_lista(usuarios, ascendente=True):
    usuarios_ordenados = sorted(usuarios, key=lambda u: u['Alumno'], reverse=not ascendente)
    for i, usuario in enumerate(usuarios_ordenados):
        print(f"{i+1}. Alumno: {usuario['Alumno']}, Nombre: {usuario['nombre']}, Apellido: {usuario['apellido']}, Edad: {usuario['edad']}, Contraseña: {usuario['contrasena']}")
    print()

# Función para realizar el registro de un nuevo usuario
def realizar_registro():
    while True:
        print("\n------ Nuevo Registro ------")
        print("\n(Presione 'x' para regresar al menú principal)")
        Alumno = input("\nIngrese el nombre de usuario: ")
        if Alumno.lower() == 'x':
            return
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        edad = int(input("Ingrese su edad: "))
        contrasena = input("Ingrese su contraseña: ")

        usuarios = cargar_usuarios()

        # Verificar si el usuario ya existe
        for usuario in usuarios:
            if usuario['Alumno'] == Alumno:
                print("\nEl nombre de usuario ya existe. Por favor, elija otro.")
                return

        # Agregar el nuevo usuario a la lista
        nuevo_usuario = {
            'Alumno': Alumno,
            'nombre': nombre,
            'apellido': apellido,
            'edad': edad,
            'contrasena': contrasena
        }
        usuarios.append(nuevo_usuario)

        # Guardar los usuarios actualizados en el archivo JSON
        guardar_usuarios(usuarios)

        print(f"\nRegistro exitoso. ¡Bienvenido, {nombre} {apellido}!")

        menu_sesion(Alumno)

# Función para realizar el inicio de sesión
def realizar_login():
    intentos = 0
    while intentos < 3:
        print("\n------ Inicio de Sesión ------")
        print("\n(Presione 'x' para regresar al menú principal)")
        Alumno = input("\nIngrese su nombre de usuario: ")
        if Alumno.lower() == 'x':
            return
        else:
            contrasena = input("Ingrese su contraseña: ")

            usuarios = cargar_usuarios()

            # Verificar las credenciales de inicio de sesión
            for usuario in usuarios:
                if usuario['Alumno'] == Alumno and usuario['contrasena'] == contrasena:
                    print(f"\nInicio de sesión exitoso. ¡Bienvenido, {usuario['nombre']} {usuario['apellido']}!")
                    menu_sesion(Alumno)
                    return

            intentos += 1
            if intentos < 3:
                print("\nCredenciales incorrectas. Por favor, intente nuevamente.")
            else:
                print("\nHa excedido el número máximo de intentos. Por favor, cree un nuevo usuario.")
                realizar_registro()
                return

# Función para mostrar el menú principal después del inicio de sesión
def menu_sesion(Alumno):
    while True:
        print("\n----- Menú de Sesión -----")
        print("\n1. Buscar alumnos de mi grupo")
        print("2. Mis datos")
        print("3. Ordenar los datos de mi grupo")
        print("4. Cerrar sesión")

        opcion = input("\nIngrese el número de opción: ")

        if opcion == '1':
            buscar_amigo()
        elif opcion == '2':
            mostrar_datos_usuario(Alumno)
        elif opcion == '3':
            ordenar_datos_usuario(Alumno)
        elif opcion == '4':
            print("\n----sesión cerrada! -----")
            ejecutar_programa()
        else:
            print("\nOpción inválida. Por favor, ingrese un número válido.")

# Función para buscar usuarios registrados por nombre o apellidos
def buscar_amigo():
    usuarios = cargar_usuarios()
    print("\n----- Búsqueda de Amigos -----")
    print("\n(Presione 'x' para regresar al menú de sesión)")
    busqueda = input("\nIngrese el nombre o apellidos del alumno que desea buscar: ")
    if busqueda.lower() == 'x':
        return
    resultados = []
    for usuario in usuarios:
        if busqueda.lower() in usuario['nombre'].lower() or busqueda.lower() in usuario['apellido'].lower():
            resultados.append(usuario)
    if len(resultados) > 0:
        print("\n----- Resultados de la Búsqueda -----")
        for i, resultado in enumerate(resultados):
            print(f"\n{i+1}. Alumno: {resultado['Alumno']}, Nombre: {resultado['nombre']}, Apellido: {resultado['apellido']}, Edad: {resultado['edad']}")
    else:
        print("\nNo se encontraron resultados para la búsqueda.")

# Función para mostrar los datos personales del usuario
def mostrar_datos_usuario(Alumno):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario['Alumno'] == Alumno:
            print("\n----- Mis Datos -----")
            print(f"\nAlumno: {usuario['Alumno']}, Nombre: {usuario['nombre']}, Apellido: {usuario['apellido']}, Edad: {usuario['edad']}")
            return

# Función para ordenar los datos del usuario en orden ascendente o descendente
def ordenar_datos_usuario(Alumno):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario['Alumno'] == Alumno:
            print("\n----- Ordenar datos de mi grupo -----")
            print("\n1. Ordenar Ascendente")
            print("2. Ordenar Descendente")
            print("x. Retroceder al menú de sesión")
            subopcion = input("\nIngrese el número de opción: ")
            if subopcion == '1':
                mostrar_lista(usuarios, ascendente=True)
            elif subopcion == '2':
                mostrar_lista(usuarios, ascendente=False)
            elif subopcion.lower() == 'x':
                return
            else:
                print("\nOpción inválida. Por favor, ingrese un número válido.")
            return

# Función para mostrar el mensaje de bienvenida y apertura del sistema
def mostrar_mensaje_bienvenida():
    print("\n--- SISTEMA DE USUARIOS ---")
    print("--- GRUPO 2 ALGORITMOS ---")
    print("--- COMPUTACIONALES ZEGEL ---")
    print("--- I CICLO - 2023 ---")

# Ejecutar el programa
def ejecutar_programa():
    mostrar_mensaje_bienvenida()
    while True:
        print("\n1. Iniciar Sesión")
        print("2. Registrar Nuevo Usuario")
        print("3. Salir del Sistema")
        opcion_sistema = input("\nIngrese el número de opción: ")
        if opcion_sistema == '1':
            realizar_login()
        elif opcion_sistema == '2':
            realizar_registro()
        elif opcion_sistema == '3':
            confirmacion = input("\n¿Está seguro de que desea salir del sistema? (SI/NO): ")
            if confirmacion.lower() == 'SI':
                print("\n----- Saliendo del Sistema -----")
                sys.exit()
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
            print("\n--- SISTEMA DE USUARIOS ---")
            print("--- GRUPO 2 ALGORITMOS ---")
            print("--- COMPUTACIONALES ZEGEL ---")
            print("--- I CICLO - 2023 ---")

# Ejecutar el programa
ejecutar_programa()