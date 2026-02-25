import pygame
from botones import botones_opciones,dibujar_lista_botones,detectar_click,repintar_boton
from colores_enum import Color
from pantalla_configuracion import dibujar_texto,dibujar_texto_centrado
from funcion_jugar import calcular_estadisticas, actualizar_puntajes,dividir_preguntas
from estado_jugador import inicializar_jugador,aplicar_multiplicador,procesar_estado_mensaje
from rondas import evaluar_respuesta
from estadisticas import guardar_estadisticas
from funciones_categorias import seleccionar_preguntas_dificultad

####################################################
def dibujar_pregunta(VENTANA, FUENTE, pregunta):
    dibujar_texto_centrado(VENTANA,FUENTE,f"Categoría: {pregunta['categoria']} | Dificultad: {pregunta['dificultad']}",90,Color.TEXTO.value)
    dibujar_texto_centrado(VENTANA,FUENTE,pregunta["pregunta"],150,Color.TEXTO.value)

def dibujar_botones_respuesta(botones: dict, pregunta: dict, seleccion=None):
    for clave, boton in botones.items():
        if seleccion is not None:
            if clave == pregunta["respuesta_correcta"]:
                boton["ColorFondo"] = Color.VERDE.value
                boton["ColorBorde"] = Color.VERDE.value
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
    FONDO = pygame.image.load(r"imagenes_sonidospygame\FONDO PREGUNTAS.png")
    VENTANA.blit(FONDO,(0,0))
    
    dibujar_pregunta(VENTANA,FUENTE,pregunta)
    dibujar_botones_respuesta(botones, pregunta, seleccion)
    dibujar_corazones(VENTANA,jugador["vidas"],configuracion["vidas"])
    dibujar_tiempo(VENTANA,FUENTE,tiempo_restante,Color.VERDE.value)
    dibujar_texto_centrado(VENTANA,FUENTE,f"Turno {jugador["nombre"]}",15,Color.TEXTO.value)
    pygame.display.flip()

def dibujar_ganador(VENTANA,FUENTE,jugadores):
    if jugadores[0]["puntaje_total"] > jugadores[1]["puntaje_total"]:
        dibujar_texto_centrado(VENTANA,FUENTE,f"¡GANADOR! - {jugadores[0]['nombre']}",190,Color.TEXTO.value)
    elif jugadores[1]["puntaje_total"] > jugadores[0]["puntaje_total"]:
        dibujar_texto_centrado(VENTANA,FUENTE,f"¡GANADOR! - {jugadores[1]['nombre']}",190,Color.TEXTO.value)
    else:
        dibujar_texto_centrado(VENTANA,FUENTE,f"EMPATE",190,Color.TEXTO.value)

def dibujar_pantalla_final(VENTANA,FUENTE,jugadores):
    FONDO = pygame.image.load(r"imagenes_sonidospygame\FONDO PUNTAJES.png")
    FONDO = pygame.transform.scale(FONDO,(800,600))
    VENTANA.blit(FONDO,(0,0))
    
    dibujar_ganador(VENTANA,FUENTE,jugadores)
    
    y = 235
    for jugador in jugadores:
        dibujar_texto_centrado(VENTANA,FUENTE,f"{jugador['nombre']} - Puntaje: {jugador['puntaje_total']}",y,Color.TEXTO.value)
        y += 40
    pygame.display.flip()


def finalizar_juego(VENTANA,FUENTE,jugadores: list, limite_preguntas: int):
    for jugador in jugadores:
        calcular_estadisticas(jugador, limite_preguntas)
        guardar_estadisticas("estadisticas.csv",jugador["nombre"], jugador)
    dibujar_pantalla_final(VENTANA,FUENTE, jugadores)

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
                    for clave, boton_dict in botones.items():
                        if boton is boton_dict:
                            return clave, tiempo_usado
        
        dibujar_juego(VENTANA, FUENTE,pregunta, botones,configuracion, jugador,tiempo_restante)
        reloj.tick(60)

def esperar_salida_final():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            if evento.type == pygame.MOUSEBUTTONDOWN:
                return "menu"

######################################################

def obtener_parametros_juego(configuracion: dict):
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

def jugar_turno_pygame(VENTANA, CLICK_SONIDO, FUENTE,jugador, pregunta,tiempo_max, configuracion):
    botones = botones_opciones(VENTANA, pregunta)

    respuesta, tiempo_usado = obtener_respuesta(VENTANA, FUENTE, CLICK_SONIDO,botones, pregunta,jugador, configuracion,tiempo_max)

    if respuesta == "salir":
        return "salir"

    resultado = evaluar_respuesta(pregunta, respuesta, tiempo_usado, tiempo_max)

    dibujar_juego(VENTANA, FUENTE,pregunta, botones,configuracion, jugador,tiempo_restante=0,seleccion=respuesta)
    pygame.time.wait(1200)

    actualizar_estado_jugador(jugador, pregunta, resultado, tiempo_usado)



def puede_jugar(jugador,limite_preguntas):
    puede = jugador["vidas"] > 0 and jugador["respondidas"] < limite_preguntas and jugador["respondidas"] < len(jugador["preguntas"])
    return puede


def juego_activo(jugadores,limite_preguntas):
    activo = False
    for jugador in jugadores:
        if puede_jugar(jugador,limite_preguntas):
            activo = True
    return activo


def jugar_pygame(VENTANA, CLICK_SONIDO, FUENTE, preguntas: list, configuracion: dict,nombres):
    limite_preguntas, tiempo_max, dificultad = obtener_parametros_juego(configuracion)
    preguntas_validas = seleccionar_preguntas_dificultad(preguntas,dificultad)
    preguntas_divididas = dividir_preguntas(preguntas_validas)
    
    jugadores = [inicializar_jugador(configuracion),inicializar_jugador(configuracion)]

    for i in range(len(jugadores)):
        jugadores[i]["preguntas"] = preguntas_divididas[i]

    for i in range(len(jugadores)):
        jugadores[i]["nombre"] = nombres[i]

    turno = 0

    while juego_activo(jugadores,limite_preguntas):

        jugador = jugadores[turno]

        if not puede_jugar(jugador,limite_preguntas):
            turno = (turno + 1) % 2
            continue

        pregunta = jugador["preguntas"][jugador["respondidas"]]

        estado_turno = jugar_turno_pygame(VENTANA,CLICK_SONIDO,FUENTE,jugador,pregunta,tiempo_max,configuracion)

        if estado_turno == "salir":
            return "salir"

        turno = (turno + 1) % 2

    finalizar_juego(VENTANA, FUENTE, jugadores, limite_preguntas)
    return esperar_salida_final()

