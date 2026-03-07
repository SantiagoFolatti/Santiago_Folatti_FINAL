import pygame
from Juego.pantalla_menu import mostrar_menu
from Juego.pantalla_configuracion import mostrar_configuracion
from Juego.pantalla_puntajes import mostrar_puntajes
from Juego.pantalla_juego import jugar_pygame
from Logica.datos import leer_preguntas_csv
from Logica.configuracion import leer_configuracion
from Juego.pantalla_minijuego import mostrar_minijuego
from Juego.botones import inicializar_ventana
from Juego.pantalla_input import mostrar_input



def main():
    VENTANA,FONDO,CLICK_SONIDO,FUENTE= inicializar_ventana()
    pantalla_actual = "menu"

    while True:
        if pantalla_actual == "menu":
            pantalla_actual = mostrar_menu(VENTANA,CLICK_SONIDO,FONDO)
        
        elif pantalla_actual == "config":
            pantalla_actual = mostrar_configuracion(VENTANA,CLICK_SONIDO,FUENTE,r"Datos\config.json")
            
        elif pantalla_actual == "jugar":
            accion,nombres = mostrar_input(VENTANA,FUENTE,FONDO)
            if accion == "menu":
                pantalla_actual = "menu"
            elif accion == "salir":
                pantalla_actual = "salir"
            elif accion == "jugar":
                pretuntas = leer_preguntas_csv(r"Datos\preguntas.csv")
                configuracion = leer_configuracion(r"Datos\config.json")
                pantalla_actual = jugar_pygame(VENTANA,CLICK_SONIDO,FUENTE,pretuntas, configuracion,nombres)
            
        elif pantalla_actual == "minijuego":
            pantalla_actual = mostrar_minijuego(VENTANA,FUENTE)
            
        elif pantalla_actual == "puntajes":
            pantalla_actual = mostrar_puntajes(VENTANA,FUENTE,r"Datos\estadisticas.csv")
            
        elif pantalla_actual == "salir":
            break
        
    pygame.quit()
