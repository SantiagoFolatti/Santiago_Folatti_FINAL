import pygame
from pantalla_menu import mostrar_menu
from pantalla_configuracion import mostrar_configuracion
from pantalla_puntajes import mostrar_puntajes
from pantalla_juego import jugar_pygame
from datos import leer_preguntas_csv
from configuracion import leer_configuracion
from patalla_minijuego import mostrar_minijuego
from botones import inicializar_ventana


def main():
    VENTANA,FONDO,CLICK_SONIDO,FUENTE= inicializar_ventana()
    pantalla_actual = "menu"

    while True:
        if pantalla_actual == "menu":
            pantalla_actual = mostrar_menu(VENTANA,CLICK_SONIDO,FONDO)
            
        elif pantalla_actual == "config":
            pantalla_actual = mostrar_configuracion(VENTANA,CLICK_SONIDO,FUENTE,r"config.json")
            
        elif pantalla_actual == "jugar":
            pretuntas = leer_preguntas_csv(r"preguntas.csv")
            configuracion = leer_configuracion(r"config.json")
            pantalla_actual = jugar_pygame(VENTANA,CLICK_SONIDO,FUENTE,pretuntas, configuracion)
            
        elif pantalla_actual == "minijuego":
            pantalla_actual = mostrar_minijuego(VENTANA,FUENTE)
            
        elif pantalla_actual == "puntajes":
            pantalla_actual = mostrar_puntajes(VENTANA,FUENTE,r"estadisticas.csv")
            
        elif pantalla_actual == "salir":
            break
        
    pygame.quit()
if __name__ == "__main__":
    main()
