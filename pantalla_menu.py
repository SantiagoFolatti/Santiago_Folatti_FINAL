import pygame
from botones import botones_menu,detectar_click, centrar_botones_en_x, dibujar_lista_botones

def mostrar_menu(VENTANA,CLICK_SONIDO,FONDO):
    botones = botones_menu(VENTANA)
    centrar_botones_en_x([botones["boton_jugar"],botones["boton_minijuego"],botones["boton_configuracion"],botones["boton_puntajes"]])


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                boton = detectar_click(botones, evento,CLICK_SONIDO)
                
                if boton is botones["boton_jugar"]:
                    return "jugar"
                
                if boton is botones["boton_minijuego"]:
                    return "minijuego"
                
                elif boton is botones["boton_configuracion"]:
                    return "config"
                
                elif boton is botones["boton_puntajes"]:
                    return "puntajes"

    
        VENTANA.blit(FONDO, (0, 0))
        dibujar_lista_botones(botones.values())
        pygame.display.update()



