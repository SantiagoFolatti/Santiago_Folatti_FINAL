import pygame
from botones import *

VENTANA,fondo,click_sonido,fuente = inicializar_ventana()
botones_menu= crear_botones_menu(VENTANA)

centrar_botones_en_x([
    botones_menu["boton_jugar"],
    botones_menu["boton_opciones"],
    botones_menu["boton_puntajes"]
])

def mostrar_menu():
    boton_opciones = botones_menu["boton_opciones"]
    pantalla_siguiente = "menu"
    flag_run = True

    while flag_run:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pantalla_siguiente = "salir"
                flag_run = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                checkear_accion_botones(botones_menu, evento)

        if boton_opciones["Presionado"]:
            boton_opciones["Presionado"] = False
            pantalla_siguiente = "config"
            flag_run = False

        VENTANA.blit(fondo, (0, 0))
        dibujar_lista_botones(botones_menu.values())
        pygame.display.update()

    return pantalla_siguiente


def checkear_accion_botones(botones, evento):
    # Resetea todos
    resetear_botones(botones)
    # Marca solo el presionado
    for boton in botones.values():
        if boton["Rectangulo"].collidepoint(evento.pos):
            boton["Presionado"] = True
            click_sonido.play()
            break 
def resetear_botones(botones):
    for boton in botones.values():
        boton["Presionado"] = False


def ir_a_configuracion():
    return "configuracion"

def ir_a_opciones():
    return "opciones"

def ir_a_puntajes():
    return "puntajes"

def ir_a_menu():
    return "menu"

def ir_a_jugar():
    return "jugar"
