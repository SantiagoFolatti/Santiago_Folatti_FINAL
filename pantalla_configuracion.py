import pygame
from configuracion import leer_configuracion, guardar_configuracion
from botones import *
from colores_enum import Color

VENTANA,fondo,click_sonido,fuente= inicializar_ventana()

def dibujar_texto(texto, x, y, color=Color.NEGRO.value):
    render = fuente.render(texto, True, color)
    VENTANA.blit(render, (x, y))

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

def crear_diccionario_acciones(config,path_config):
    return {
        "menos_preguntas" : (accion_restar,["cantidad_preguntas", config, 1]),
        "mas_preguntas" : (accion_sumar, ["cantidad_preguntas", config]),
        
        "menos_tiempo" : (accion_restar, ["tiempo_por_pregunta", config, 1]),
        "mas_tiempo" : (accion_sumar, ["tiempo_por_pregunta", config]),
        
        "menos_vidas" : (accion_restar, ["vidas", config, 1]),
        "mas_vidas" : (accion_sumar, ["vidas", config]),
        
        "facil" : (accion_dificultad, [config, "facil"]),
        "media" : (accion_dificultad, [config, "media"]),
        "dificil" : (accion_dificultad, [config, "dificil"]),
        
        "guardar" : (accion_guardar, [path_config, config]),
        "salir" : (accion_salir, [])

    }


def mostrar_configuracion(path_config):
    botones = crear_botones_configuracion(VENTANA)  
    config = leer_configuracion(path_config)
    acciones = crear_diccionario_acciones(config, path_config)
    
    
    while True:
        dibujar_configuracion(config, botones)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                boton = detectar_click(botones, evento, click_sonido)
                if boton:
                    for nombre, boton_dict in botones.items():
                        if boton is boton_dict:
                            funcion, args = acciones[nombre]
                            resultado = funcion(*args)

                            if resultado  == "guardar" or resultado == "salir":
                                return "menu"

