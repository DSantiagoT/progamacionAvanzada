from utils import *

while True:
    print("\n--- Gestor de Notas ---")
    print("1. Crear nota")
    print("2. Leer nota")
    print("3. Listar notas")
    print("4. Buscar palabra")
    print("5. Editar nota")
    print("6. Eliminar nota")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la nota: ")
        contenido = input("Contenido: ")
        crear_nota(nombre, contenido)

    elif opcion == "2":
        nombre = input("Nombre de la nota: ")
        leer_nota(nombre)

    elif opcion == "3":
        listar_notas()

    elif opcion == "4":
        clave = input("Palabra clave: ")
        buscar_palabra(clave)

    elif opcion == "5":
        nombre = input("Nombre de la nota: ")
        nuevo = input("Nuevo contenido: ")
        editar_nota(nombre, nuevo)

    elif opcion == "6":
        nombre = input("Nombre de la nota: ")
        eliminar_nota(nombre)

    elif opcion == "7":
        break

    else:
        print("Opción no válida.")
