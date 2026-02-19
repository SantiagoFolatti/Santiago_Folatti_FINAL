import pygame
import random
from botones import botones_opciones,dibujar_lista_botones,detectar_click,repintar_boton
from colores_enum import Color
from pantalla_configuracion import dibujar_texto,dibujar_texto_centrado
from funcion_jugar import calcular_estadisticas, actualizar_puntajes
from estado_jugador import inicializar_jugador,aplicar_multiplicador,procesar_estado_mensaje
from rondas import evaluar_respuesta
from estadisticas import guardar_estadisticas

####################################################
def dibujar_pregunta(VENTANA, FUENTE, pregunta):
    dibujar_texto_centrado(VENTANA,FUENTE,f"Categoría: {pregunta['categoria']} | Dificultad: {pregunta['dificultad']}",90,Color.TEXTO.value)
    dibujar_texto_centrado(VENTANA,FUENTE,pregunta["pregunta"],150,Color.BLANCO.value)

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

def dibujar_corazones(VENTANA, vidas_actuales, vidas_maximas):
    corazon = pygame.image.load(r"imagenes_sonidospygame\corazon.png")
    corazon = pygame.transform.scale(corazon,(40,40))
    corazon_roto = pygame.image.load(r"imagenes_sonidospygame\corazonroto.webp")
    corazon_roto = pygame.transform.scale(corazon_roto,(40,40))
    
    for i in range(vidas_maximas):
        pos_x = VENTANA.get_width() - 50 - (i * 40)
        if i < vidas_actuales:
            VENTANA.blit(corazon,(pos_x,10))
        else:
            VENTANA.blit(corazon_roto,(pos_x,10))

def dibujar_tiempo(VENTANA,FUENTE,tiempo_restante,color):
    if tiempo_restante <= 0:
        tiempo_restante = 0
    
    if tiempo_restante <= 5:
        color = Color.ROJO.value
        
    dibujar_texto(VENTANA,FUENTE,f"{int(tiempo_restante)}s",10,10,color)

def dibujar_juego(VENTANA,FUENTE,pregunta: dict, botones: dict,configuracion,jugador,tiempo_restante, seleccion=None):
    VENTANA.fill(Color.FONDO.value)
    
    dibujar_pregunta(VENTANA,FUENTE,pregunta)
    dibujar_botones_respuesta(botones, pregunta, seleccion)
    dibujar_corazones(VENTANA,jugador["vidas"],configuracion["vidas"])
    dibujar_tiempo(VENTANA,FUENTE,tiempo_restante,Color.VERDE.value)
    
    pygame.display.flip()


######################################################
def obtener_respuesta(VENTANA, FUENTE, CLICK_SONIDO,botones, pregunta,jugador, configuracion,tiempo_max):
    inicio = pygame.time.get_ticks()
    reloj = pygame.time.Clock()

    while True:
        tiempo_usado = (pygame.time.get_ticks() - inicio) / 1000
        tiempo_restante = tiempo_max - tiempo_usado

        if tiempo_restante <= 0:
            return None, tiempo_usado

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir", tiempo_usado

            if evento.type == pygame.MOUSEBUTTONDOWN:
                boton = detectar_click(botones, evento, CLICK_SONIDO)
                if boton:
                    for clave, b in botones.items():
                        if b is boton:
                            return clave, tiempo_usado
        
        dibujar_juego(VENTANA, FUENTE,pregunta, botones,configuracion, jugador,tiempo_restante)
        reloj.tick(60)

def esperar_salida_final():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            if evento.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                return "menu"

######################################################

def obtener_parametros_juego(configuracion: dict) -> tuple:
    limite_preguntas = configuracion["cantidad_preguntas"]
    tiempo_max = configuracion["tiempo_por_pregunta"]
    dificultad = configuracion["dificultad"]
    return limite_preguntas, tiempo_max, dificultad

def actualizar_estado_jugador(jugador:dict, pregunta:dict, resultado:dict,tiempo_usado:float) -> dict:
    estado = resultado["estado"]
    jugador = procesar_estado_mensaje(jugador, estado)
    puntos = aplicar_multiplicador(pregunta["puntos"], estado, jugador["multiplicador"])
    actualizar_puntajes(jugador, puntos, resultado["respondida"])
    jugador["tiempo_total"] += tiempo_usado
    
    return jugador


def dibujar_pantalla_final(VENTANA,FUENTE,jugador):
    VENTANA.fill(Color.FONDO.value)

    if jugador["vidas"] <= 0:
        dibujar_texto_centrado(VENTANA,FUENTE,"Te quedaste sin vidas",220,Color.ROJO.value)
    else:
        dibujar_texto_centrado(VENTANA,FUENTE,"Partida terminada",220,Color.VERDE_OSCURO.value)

    dibujar_texto_centrado(VENTANA,FUENTE,f"Puntaje final: {jugador['puntaje_total']}",280,Color.TEXTO.value)
    dibujar_texto_centrado(VENTANA,FUENTE,"Presiona una tecla o click para volver",350,Color.TEXTO.value)
    
    pygame.display.flip()


def finalizar_juego(VENTANA,FUENTE,jugador: dict, limite_preguntas: int):
    jugador = calcular_estadisticas(jugador, limite_preguntas)
    guardar_estadisticas("estadisticas.csv", "Jugador", jugador)
    dibujar_pantalla_final(VENTANA,FUENTE, jugador)


def jugar_turno_pygame(VENTANA, CLICK_SONIDO, FUENTE,jugador, pregunta,tiempo_max, configuracion):
    botones = botones_opciones(VENTANA, pregunta)

    respuesta, tiempo_usado = obtener_respuesta(VENTANA, FUENTE, CLICK_SONIDO,botones, pregunta,jugador, configuracion,tiempo_max)

    if respuesta == "salir":
        return "salir"

    resultado = evaluar_respuesta(pregunta, respuesta, tiempo_usado, tiempo_max)

    dibujar_juego(VENTANA, FUENTE,pregunta, botones,configuracion, jugador,tiempo_restante=0,seleccion=respuesta)

    pygame.time.wait(1200)

    actualizar_estado_jugador(jugador, pregunta, resultado, tiempo_usado)

    return "continuar"


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

        estado_turno = jugar_turno_pygame(VENTANA,CLICK_SONIDO,FUENTE,jugador, pregunta, tiempo_max,configuracion)
        if estado_turno == "salir":
            return "salir"
        
        indice += 1

    finalizar_juego(VENTANA,FUENTE,jugador, limite_preguntas)
    
    return esperar_salida_final()