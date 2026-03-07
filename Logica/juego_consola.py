from Logica.jugar import jugar_preguntas_y_respuestas
from Logica.estadisticas import leer_estadisticas, mostrar_estadisticas, ordenar_estadisticas_por_puntaje
from Logica.ingresos import *
from Logica.minijuego import juego
from Logica.configuracion import cambiar_configuracion
from Logica.mostrar import mostrar_un_mensaje

def mostrar_menu():
    print("\n📋 MENÚ PRINCIPAL")
    print("1️⃣   Cambiar configuracion")
    print("2️⃣   Jugar Preguntas y Respuestas")
    print("3️⃣   Jugar Ta-Te-Ti")
    print("4️⃣   Ver Estadísticas")
    print("5️⃣   Ver Ranking de Jugadores")
    print("6️⃣   Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            cambiar_configuracion(r"Datos\config.json")
        elif opcion == "2":
            jugar_preguntas_y_respuestas()
        elif opcion == "3":
            mostrar_un_mensaje("\n🕹️ ¡Bienvenido al Ta-Te-Ti!")
            juego()
        elif opcion == "4":
            estadisticas = leer_estadisticas(r"Datos\estadisticas.csv")
            mostrar_estadisticas(estadisticas, "📊 --- Estadísticas Guardadas --- 📊")
        elif opcion == "5":
            estadisticas = leer_estadisticas(r"Datos\estadisticas.csv")
            ordenar_estadisticas_por_puntaje(estadisticas)
            mostrar_estadisticas(estadisticas,"📊 --- Ranking de Jugadores --- 📊")
        elif opcion == "6":
            mostrar_un_mensaje("¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            mostrar_un_mensaje("Opción inválida. Por favor, elija una opción del 1 al 5.")

