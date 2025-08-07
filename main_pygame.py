from menu_pygame import mostrar_menu
from configuracion import leer_configuracion
from pantalla_configuracion import mostrar_configuracion
from pantalla_puntajes import mostrar_puntajes
from juego_normal import iniciar_juego_grafico


def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "jugar":
            config = leer_configuracion("Santiago_Folatti_FINAL/config.json")
            iniciar_juego_grafico(config)
        elif opcion == "configuracion":
            mostrar_configuracion("Santiago_Folatti_FINAL/config.json")
        elif opcion == "puntajes":
            mostrar_puntajes("Santiago_Folatti_FINAL/estadisticas.csv")

if __name__ == "__main__":
    main()
