import pygame
from botones import botones_menu,detectar_click, dibujar_lista_botones



def mostrar_menu(VENTANA:pygame.surface, CLICK_SONIDO:pygame.mixer.Sound, FONDO: pygame.Surface):
    botones = botones_menu(VENTANA)

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

    
        VENTANA.blit(FONDO,(0,0))
        dibujar_lista_botones(botones.values())
        pygame.display.update()



