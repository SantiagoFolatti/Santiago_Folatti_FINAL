import pygame
from configuracion import leer_configuracion, guardar_configuracion
from botones import crear_botones_opciones,dibujar_lista_botones,inicializar_ventana
from menu_pygame import checkear_accion_botones
from colores_enum import *

VENTANA,fondo,click_sonido,fuente= inicializar_ventana()

def dibujar_texto(texto, x, y, color=Color.NEGRO.value):
    render = fuente.render(texto, True, color)
    VENTANA.blit(render, (x, y))

def accion_sumar(clave_config, config):
    config[clave_config] += 1

def accion_restar(clave_config, config, minimo):
    if config[clave_config] > minimo:
        config[clave_config] -= 1

def accion_dificultad(config, valor_dificultad):
    config["dificultad"] = valor_dificultad

def accion_guardar(path_config, config):
    guardar_configuracion(path_config, config)
    return "guardar"

def accion_salir():
    return "salir"


def dibujar_configuracion(config, botones):
    VENTANA.fill(Color.LAVANDA.value)
    dibujar_texto("CONFIGURACIÓN DEL JUEGO", 220, 30)
    dibujar_texto(f"Preguntas: {config['cantidad_preguntas']}", 290, 125)
    dibujar_texto(f"Tiempo por pregunta: {config['tiempo_por_pregunta']} seg", 220, 205)
    dibujar_texto(f"Vidas: {config['vidas']}", 310, 285)
    dibujar_texto(f"Dificultad: {config['dificultad'].capitalize()}", 290, 420)

    # Resaltar dificultad activa
    for clave in ["facil", "media", "dificil"]:
        if config["dificultad"] == clave:
            botones[clave]["ColorBorde"] = "black"
        else:
            botones[clave]["ColorBorde"] = "grey"

    dibujar_lista_botones(botones.values())
    pygame.display.update()

def manejar_click_config(botones, config, evento, path_config):
    resultado = None  
    checkear_accion_botones(botones, evento)

    if botones["menos_preguntas"]["Presionado"]:
        accion_restar("cantidad_preguntas", config, 1)
    elif botones["mas_preguntas"]["Presionado"]:
        accion_sumar("cantidad_preguntas", config)
    elif botones["menos_tiempo"]["Presionado"]:
        accion_restar("tiempo_por_pregunta", config, 5)
    elif botones["mas_tiempo"]["Presionado"]:
        accion_sumar("tiempo_por_pregunta", config)
    elif botones["menos_vidas"]["Presionado"]:
        accion_restar("vidas", config, 1)
    elif botones["mas_vidas"]["Presionado"]:
        accion_sumar("vidas", config)
    elif botones["facil"]["Presionado"]:
        accion_dificultad(config, "facil")
    elif botones["media"]["Presionado"]:
        accion_dificultad(config, "media")
    elif botones["dificil"]["Presionado"]:
        accion_dificultad(config, "dificil")
    elif botones["guardar"]["Presionado"]:
        guardar_configuracion(path_config, config)
        resultado = "guardar"
    elif botones["salir"]["Presionado"]:
        resultado = "salir"

    return resultado


def mostrar_configuracion(path_config):
    botones_opciones = crear_botones_opciones(VENTANA)  
    config = leer_configuracion(path_config)
    pantalla_siguiente = "menu"
    corriendo = True

    while corriendo:
        dibujar_configuracion(config, botones_opciones)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pantalla_siguiente = "salir"
                corriendo = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                resultado = manejar_click_config(botones_opciones, config, evento, path_config)
                if resultado == "guardar":
                    pantalla_siguiente = "menu"
                    corriendo = False
                elif resultado == "salir":
                    pantalla_siguiente = "menu"
                    corriendo = False

    return pantalla_siguiente