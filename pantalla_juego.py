import pygame
import random
from botones import botones_opciones,dibujar_lista_botones,detectar_click,repintar_boton
from colores_enum import Color
from pantalla_configuracion import dibujar_texto
from funcion_jugar import calcular_estadisticas, actualizar_puntajes
from estado_jugador import inicializar_jugador,aplicar_multiplicador,procesar_estado_mensaje
from rondas import evaluar_respuesta
from estadisticas import guardar_estadisticas

def dibujar_pregunta(VENTANA,FUENTE,pregunta: dict):
    VENTANA.fill(Color.BLANCO.value)
    dibujar_texto(VENTANA,FUENTE,f"Categoria: {pregunta['categoria']} | Dificultad: {pregunta['dificultad']}",40,30)
    dibujar_texto(VENTANA,FUENTE,pregunta["pregunta"], 40, 85)


def dibujar_botones_respuesta(botones: dict, pregunta: dict, seleccion=None):
    for clave, boton in botones.items():
        boton["ColorFondo"] = Color.GRIS.value

        if seleccion is not None:
            if clave == pregunta["respuesta_correcta"]:
                boton["ColorFondo"] = Color.VERDE.value
            elif clave == seleccion:
                boton["ColorFondo"] = Color.ROJO.value

        repintar_boton(boton)

    dibujar_lista_botones(botones.values())
    pygame.display.flip()

def mostrar_pregunta(VENTANA,FUENTE,pregunta: dict, botones: dict, seleccion=None):
    dibujar_pregunta(VENTANA,FUENTE,pregunta)
    dibujar_botones_respuesta(botones, pregunta, seleccion)

def obtener_respuesta(CLICK_SONIDO,botones: dict, tiempo_max: int):
    inicio = pygame.time.get_ticks()
    reloj = pygame.time.Clock()

    while True:
        tiempo_usado = (pygame.time.get_ticks() - inicio) / 1000

        if tiempo_usado >= tiempo_max:
            return None, tiempo_usado

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir", tiempo_usado

            if evento.type == pygame.MOUSEBUTTONDOWN:
                boton_clickeado = detectar_click(botones, evento, CLICK_SONIDO)
                if boton_clickeado:
                    for clave, boton in botones.items():
                        if boton is boton_clickeado:
                            return clave, tiempo_usado

        reloj.tick(60)

def esperar_salida_final():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            if evento.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                return "menu"


def jugar_pygame(VENTANA,CLICK_SONIDO,FUENTE,preguntas: list, configuracion: dict):
    preguntas_restantes = preguntas.copy()
    random.shuffle(preguntas_restantes)

    limite_preguntas, tiempo_max, dificultad = obtener_parametros_juego(configuracion)
    jugador = inicializar_jugador(configuracion)
    
    indice = 0

    while indice < len(preguntas_restantes)and jugador["respondidas"] < limite_preguntas and jugador["vidas"] > 0:
        pregunta = preguntas_restantes[indice]

        if pregunta["dificultad"] != dificultad:
            indice += 1
            continue

        estado_turno = jugar_turno_pygame(VENTANA,CLICK_SONIDO,FUENTE,jugador, pregunta, tiempo_max)
        if estado_turno == "salir":
            return "salir"
        
        indice += 1

    finalizar_juego(VENTANA,FUENTE,jugador, limite_preguntas)
    
    return esperar_salida_final()


def obtener_parametros_juego(configuracion: dict) -> tuple:
    limite_preguntas = configuracion["cantidad_preguntas"]
    tiempo_max = configuracion["tiempo_por_pregunta"]
    dificultad = configuracion["dificultad"]
    return limite_preguntas, tiempo_max, dificultad

def jugar_turno_pygame(VENTANA,CLICK_SONIDO,FUENTE,jugador: dict, pregunta: dict, tiempo_max: int) -> dict:
    botones = botones_opciones(VENTANA, pregunta)
    mostrar_pregunta(VENTANA,FUENTE,pregunta, botones)

    respuesta, tiempo_usado = obtener_respuesta(CLICK_SONIDO,botones, tiempo_max)

    if respuesta == "salir":
        return "salir"

    resultado = evaluar_respuesta(pregunta, respuesta, tiempo_usado, tiempo_max)
    mostrar_pregunta(VENTANA,FUENTE,pregunta, botones, seleccion=respuesta)
    pygame.time.wait(1200)
    
    jugador = actualizar_estado_jugador(jugador, pregunta, resultado, tiempo_usado)
    
    return "continuar"


def actualizar_estado_jugador(jugador:dict, pregunta:dict, resultado:dict,tiempo_usado:float) -> dict:
    estado = resultado["estado"]
    jugador = procesar_estado_mensaje(jugador, estado)
    puntos = aplicar_multiplicador(pregunta["puntos"], estado, jugador["multiplicador"])
    actualizar_puntajes(jugador, puntos, resultado["respondida"])
    jugador["tiempo_total"] += tiempo_usado
    return jugador
    


def dibujar_pantalla_final(VENTANA,FUENTE,jugador):
    VENTANA.fill(Color.BLANCO.value)

    if jugador["vidas"] <= 0:
        dibujar_texto(VENTANA,FUENTE,"Te quedaste sin vidas",250,220,color=Color.ROJO.value)
    else:
        dibujar_texto(VENTANA,FUENTE,"Partida terminada",280,220,color=Color.VERDE_OSCURO.value)

    dibujar_texto(VENTANA,FUENTE,f"Puntaje final: {jugador['puntaje_total']}",280,280)
    dibujar_texto(VENTANA,FUENTE,"Presiona una tecla o click para volver",160,350)
    
    pygame.display.flip()
    
    
def finalizar_juego(VENTANA,FUENTE,jugador: dict, limite_preguntas: int):
    jugador = calcular_estadisticas(jugador, limite_preguntas)
    guardar_estadisticas("estadisticas.csv", "Jugador", jugador)
    dibujar_pantalla_final(VENTANA,FUENTE, jugador)