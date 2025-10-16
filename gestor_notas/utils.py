import os
from datetime import datetime
import shutil

notas = "notas"
if not os.path.exists(notas):
    os.makedirs(notas)


def crear_nota(nombre, contenido):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ruta = os.path.join(notas, f"{nombre}.txt")
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(f"Fecha: {fecha}\n\n")
        archivo.write(contenido)


def leer_nota(nombre):
    ruta = os.path.join(notas, f"{nombre}.txt")
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            print(archivo.read())
    else:
        print("Nota no encontrada.")


def listar_notas():
    print("\nNotas disponibles:")
    for archivo in os.listdir(notas):
        if archivo.endswith(".txt"):
            print(f"- {archivo[:-4]}")


def buscar_palabra(clave):
    encontrados = []
    for archivo in os.listdir(notas):
        ruta = os.path.join(notas, archivo)
        with open(ruta, "r", encoding="utf-8") as f:
            if clave.lower() in f.read().lower():
                encontrados.append(archivo)
    print("\nCoincidencias encontradas:")
    for n in encontrados:
        print(f"- {n[:-4]}")


def editar_nota(nombre, nuevo_contenido):
    ruta = os.path.join(notas, f"{nombre}.txt")
    if os.path.exists(ruta):
        respaldo = os.path.join(notas, f"{nombre}_bak.txt")
        shutil.copy(ruta, respaldo)
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(nuevo_contenido)
        print("Nota actualizada y respaldo creado.")
    else:
        print("Nota no encontrada.")


def eliminar_nota(nombre):
    ruta = os.path.join(notas, f"{nombre}.txt")
    if os.path.exists(ruta):
        os.remove(ruta)
        print("Nota eliminada.")
    else:
        print("Nota no encontrada.")
