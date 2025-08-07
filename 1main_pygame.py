import pygame
from botones import *
from pantalla_configuracion import mostrar_configuracion

VENTANA,fondo,click_sonido,fuente = inicializar_ventana(titulo="Opciones")
lista_botones_menu, lista_botones_opciones = crear_botones(VENTANA)

centrar_botones_en_x([lista_botones_menu[1],lista_botones_menu[2],lista_botones_menu[3]])

def mostrar_menu():
    boton_opciones = lista_botones_menu[2]
    flag_run = True
    while flag_run:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_run = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                checkear_accion_botones(lista_botones_menu,evento)
        
        if boton_opciones["Presionado"] == True:
            mostrar_configuracion("Santiago_Folatti_FINAL\config.json")
            boton_opciones["Presionado"] = False
            

        VENTANA.blit(fondo, (0, 0))
        dibujar_lista_botones(lista_botones_menu)
        pygame.display.update()

    pygame.quit()

def checkear_accion_botones(lista_botones, evento):
    for boton in lista_botones:
        if boton["Rectangulo"].collidepoint(evento.pos):
            boton["Presionado"] = True
            click_sonido.play()



mostrar_menu()