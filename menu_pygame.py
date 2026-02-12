import pygame
from botones import *

VENTANA,fondo,click_sonido,fuente = inicializar_ventana()

def mostrar_menu():
    botones = crear_botones_menu(VENTANA)
    
    centrar_botones_en_x([botones["boton_jugar"],botones["boton_configuracion"],botones["boton_puntajes"]])


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                boton = detectar_click(botones, evento,click_sonido)
                
                if boton is botones["boton_jugar"]:
                    return "jugar"
                
                elif boton is botones["boton_configuracion"]:
                    return "config"
                
                elif boton is botones["boton_puntajes"]:
                    return "puntajes"

    
        VENTANA.blit(fondo, (0, 0))
        dibujar_lista_botones(botones.values())
        pygame.display.update()



