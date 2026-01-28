import random
import os
from PIL import Image

datosPoliperros = {
    "nombre": [],
    "huellaDactilar": [],
    "foto": []
}

def menu():
    print("\n\t\t*** POLIPERROS ***\n")
    print("1) Registrar poliperros")
    print("2) Mostrar poliperros")
    print("3) Imprimir BDD")
    print("4) Salir")
    return int(input("Seleccione una opción: "))


def registrarPoliperros(numPerros):
    os.makedirs("BDDPERROS", exist_ok=True)

    with open("poliperros.txt", "a", encoding="utf-8") as archivo:
        for i in range(numPerros):
            print(f"\nIngrese los datos del poliperro {i + 1}")

            nombre = input("Nombre: ")
            huella = input("Huella dactilar: ")
            tiene_foto = input("¿Tiene foto? (si/no): ").lower()

            if tiene_foto == "si":
                ruta_original = input("Ruta de la imagen: ")
                imagen = Image.open(ruta_original)
            else:
                imagen = Image.open("dog.png")

            ruta_guardada = f"BDDPERROS/poliperro_{random.randint(1,1000)}.png"
            imagen.save(ruta_guardada)

            datosPoliperros["nombre"].append(nombre)
            datosPoliperros["huellaDactilar"].append(huella)
            datosPoliperros["foto"].append(ruta_guardada)

            archivo.write(f"{nombre}--{huella}--{ruta_guardada}\n")

def mostrarPoliperros():
    for i in range(len(datosPoliperros["nombre"])):
        print("\n------------------------------")
        print(f"Poliperro {i + 1}")
        print("Nombre:", datosPoliperros["nombre"][i])
        print("Huella:", datosPoliperros["huellaDactilar"][i])
        print("Foto:", datosPoliperros["foto"][i])

        Image.open(datosPoliperros["foto"][i]).show()

def imprimirArchivo():
    with open("poliperros.txt", "r", encoding="utf-8") as archivo:
        print("\n--- BASE DE DATOS ---")
        print(archivo.read())

def main():
    opcion = menu()

    while opcion != 4:
        if opcion == 1:
            n = int(input("¿Cuántos poliperros desea registrar?: "))
            registrarPoliperros(n)
        elif opcion == 2:
            mostrarPoliperros()
        elif opcion == 3:
            imprimirArchivo()
        else:
            print("Opción inválida")

        opcion = menu()

    print("\nGracias por usar el sistema POLIPERROS 🐶")

main()