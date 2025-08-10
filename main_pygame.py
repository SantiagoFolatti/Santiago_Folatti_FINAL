from menu_pygame import mostrar_menu
from pantalla_configuracion import mostrar_configuracion
import pygame

def main():
    pantalla_actual = "menu"
    corriendo = True

    while corriendo:
        if pantalla_actual == "menu":
            pantalla_actual = mostrar_menu()
        elif pantalla_actual == "config":
            pantalla_actual = mostrar_configuracion("Santiago_Folatti_FINAL\\config.json")
        elif pantalla_actual == "salir":
            corriendo = False

    pygame.quit()
if __name__ == "__main__":
    main()
