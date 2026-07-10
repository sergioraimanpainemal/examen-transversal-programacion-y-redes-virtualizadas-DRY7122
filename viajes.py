integrantes = [
    "Florencia Moya",
    "Sergio Raiman",
    "Juan Veas"
]

print("========================================")
print(" Lista de Integrantes del Grupo - DRY7122")
print("========================================")


for integrante in integrantes:
    print(f"• {integrante}"
:100:
Haz clic para reaccionar
:thumbsdown:
Haz clic para reaccionar
:thumbsup:
Haz clic para reaccionar
Añadir reacción
Responder
Reenviar
Más
[20:13]jueves, 9 de julio de 2026 20:13
INTEGRANTES
:100:
Haz clic para reaccionar
:thumbsdown:
Haz clic para reaccionar
:thumbsup:
Haz clic para reaccionar
Añadir reacción
Responder
Reenviar
Más
[20:13]jueves, 9 de julio de 2026 20:13
import sys



def calcular_viaje():

    print("=========================================")

    print("  Calculador de Rutas Chile - Argentina  ")

    print("=========================================")



    origen = input("Ciudad de Origen (Chile) [o 's' para salir]: ").strip()

    if origen.lower() == 's': sys.exit()



    destino = input("Ciudad de Destino (Argentina): ").strip()



    print("\nMedios de transporte disponibles:")

    print("1. Auto / Vehículo particular")

    print("2. Autobús / Bus de larga distancia")

    print("3. Avión")

    transporte = input("Seleccione una opción (1-3): ").strip()



    km = 360.0 

    millas = km * 0.621371



    if transporte == "1":

        medio = "Auto"

        duracion = "6 horas 30 minutos (sujeto a aduana en Paso Libertadores)"

    elif transporte == "2":

        medio = "Autobús"

        duracion = "8 horas"

    elif transporte == "3":

        medio = "Avión"

        duracion = "45 minutos"

        km = 180.0

        millas = km * 0.621371

    else:

        print("Opción inválida.")

        return



    print("\n================ RESULTADOS ================")

    print(f"Ruta: Desde {origen} hasta {destino}")

    print(f"Medio de transporte: {medio}")

    print(f"Distancia en Kilómetros: {km:.2f} km")

    print(f"Distancia en Millas: {millas:.2f} mi")

    print(f"Duración estimada del viaje: {duracion}")

    print("\nNarrativa del viaje:")

    print(f"El viaje comienza en la ciudad chilena de {origen}. Si viajas en transporte terrestre, ")

    print(f"cruzarás la imponente Cordillera de los Andes disfrutando de paisajes de alta montaña.")

    print(f"Recuerda realizar los trámites migratorios correspondientes en el complejo fronterizo")

    print(f"antes de descender hacia tu destino final en {destino}, Argentina.")

    print("============================================\n")



while True:

    calcular_viaje()
