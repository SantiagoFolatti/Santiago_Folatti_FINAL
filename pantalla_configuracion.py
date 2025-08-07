import pygame
import sys
from configuracion import leer_configuracion, guardar_configuracion
from botones import crear_botones,dibujar_lista_botones,inicializar_ventana
from colores_enum import *

VENTANA,fondo,click_sonido,fuente= inicializar_ventana()
COLOR_BLANCO = Color.BLANCO.value
COLOR_TEXTO = Color.NEGRO.value

lista_botones_menu, lista_botones_opciones = crear_botones(VENTANA)


def dibujar_texto(texto, x, y, color=COLOR_TEXTO):
    render = fuente.render(texto, True, color)
    VENTANA.blit(render, (x, y))

def mostrar_configuracion(path_config):
    config = leer_configuracion(path_config)
    
    boton_menos_preg = lista_botones_opciones[0]
    boton_mas_preg = lista_botones_opciones[1]
    boton_menos_tiempo =lista_botones_opciones[2]
    boton_mas_tiempo = lista_botones_opciones[3]
    boton_menos_vidas = lista_botones_opciones[4]
    boton_mas_vidas = lista_botones_opciones[5]
    boton_guardar = lista_botones_opciones[6]
    
    corriendo = True
    while corriendo:
        VENTANA.fill(Color.LAVANDA.value)

        dibujar_texto("CONFIGURACIÓN DEL JUEGO", 220, 30)
        dibujar_texto(f"Preguntas: {config['cantidad_preguntas']}", 290, 125)
        dibujar_texto(f"Tiempo por pregunta: {config['tiempo_por_pregunta']} seg", 220, 205)
        dibujar_texto(f"Vidas: {config['vidas']}", 310, 285)
        dibujar_lista_botones(lista_botones_opciones)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                
                boton_resta(boton_menos_preg, "cantidad_preguntas", config, 1, evento)
                boton_suma(boton_mas_preg, "cantidad_preguntas", config, evento)
                boton_resta(boton_menos_tiempo, "tiempo_por_pregunta", config, 5, evento)
                boton_suma(boton_mas_tiempo, "tiempo_por_pregunta", config, evento)
                boton_resta(boton_menos_vidas, "vidas", config, 1, evento)
                boton_suma(boton_mas_vidas, "vidas", config, evento)

                if boton_guardar["Rectangulo"].collidepoint(x, y):
                    guardar_configuracion(path_config, config)
                    corriendo = False
                    click_sonido.play()


def boton_suma(boton, clave_config, config, evento):
    if boton["Rectangulo"].collidepoint(evento.pos):
        config[clave_config] += 1
        click_sonido.play()

def boton_resta(boton, clave_config, config, minimo, evento):
    if boton["Rectangulo"].collidepoint(evento.pos) and config[clave_config] > minimo:
        config[clave_config] -= 1
        click_sonido.play()

