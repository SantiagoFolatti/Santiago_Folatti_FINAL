from menu_pygame import mostrar_menu
from pantalla_configuracion import mostrar_configuracion
from pantalla_puntajes import mostrar_puntajes
from botones import inicializar_ventana
from juego_normal import jugar_pygame
from datos import leer_preguntas_csv
from configuracion import leer_configuracion
import pygame

def main():
    ventana,fondo,click_sonido,fuente = inicializar_ventana()
    pantalla_actual = "menu"

    while True:
        if pantalla_actual == "menu":
            pantalla_actual = mostrar_menu()
        elif pantalla_actual == "config":
            pantalla_actual = mostrar_configuracion(r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\config.json")
        elif pantalla_actual == "jugar":
            pretuntas = leer_preguntas_csv(r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\preguntas.csv")
            configuracion = leer_configuracion(r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\config.json")
            pantalla_actual = jugar_pygame(pretuntas,configuracion)
            
            
        elif pantalla_actual == "puntajes":
            pantalla_actual = mostrar_puntajes(r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\estadisticas.csv")
            
        elif pantalla_actual == "salir":
            break
        
    pygame.quit()
if __name__ == "__main__":
    main()
