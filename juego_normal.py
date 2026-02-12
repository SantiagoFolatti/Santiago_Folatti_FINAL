import pygame
import sys
import random
from funcion_jugar import calcular_estadisticas, actualizar_puntajes
from estado_jugador import inicializar_jugador, aplicar_multiplicador,procesar_estado_mensaje
from pantalla_opciones import dibujar_texto

# --- Colores y pantalla ---
ANCHO, ALTO = 800, 600
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)
COLOR_OPCION = (200, 220, 255)
COLOR_CORRECTO = (150, 255, 150)
COLOR_INCORRECTO = (255, 150, 150)

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Preguntas y Respuestas")
fuente = pygame.font.SysFont("Arial", 28)


# -------------------------
# FUNCIONES DE VISTA
# -------------------------
def mostrar_pregunta_pygame(pregunta, seleccion=None):
    """Dibuja la pregunta y opciones en pantalla"""
    pantalla.fill(COLOR_BLANCO)
    dibujar_texto(f"Categoría: {pregunta['categoria']} | Dificultad: {pregunta['dificultad']}", 50, 30)
    dibujar_texto(pregunta["pregunta"], 50, 90)

    claves = ["A", "B", "C"]
    botones = {}
    i = 0
    for clave in claves:
        opcion_texto = f"{clave}: {pregunta['opciones'][clave]}"
        y = 180 + i * 90
        rect = pygame.Rect(50, y, 700, 60)

        color = COLOR_OPCION
        if seleccion is not None:
            if clave == seleccion:
                if clave == pregunta["respuesta_correcta"]:
                    color = COLOR_CORRECTO
                else:
                    color = COLOR_INCORRECTO
            elif clave == pregunta["respuesta_correcta"]:
                color = COLOR_CORRECTO

        pygame.draw.rect(pantalla, color, rect)
        pygame.draw.rect(pantalla, COLOR_NEGRO, rect, 2)
        dibujar_texto(opcion_texto, 60, y + 15)
        botones[clave] = rect
        i += 1

    pygame.display.flip()
    return botones


def obtener_respuesta_click(botones):
    """Devuelve la opción seleccionada por click"""
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                for clave in botones:
                    if botones[clave].collidepoint(x, y):
                        return clave


# -------------------------
# FUNCIÓN PRINCIPAL DEL JUEGO
# -------------------------
def jugar_pygame(preguntas: list, configuracion: dict, dificultad: str) -> dict:
    """Lógica del juego, conectada con la vista en Pygame"""
    preguntas_restantes = preguntas.copy()
    random.shuffle(preguntas_restantes)
    limite_preguntas = configuracion["cantidad_preguntas"]

    jugador = inicializar_jugador(configuracion)

    indice = 0
    while indice < len(preguntas_restantes) and jugador["respondidas"] < limite_preguntas and jugador["vidas"] > 0:
        pregunta = preguntas_restantes[indice]

        # Dibujar pregunta
        botones = mostrar_pregunta_pygame(pregunta)

        # Esperar respuesta
        respuesta = obtener_respuesta_click(botones)

        # Mostrar con colores correctos/incorrectos
        mostrar_pregunta_pygame(pregunta, seleccion=respuesta)
        pygame.time.wait(2000)

        # Procesar respuesta
        estado = "correcta" if respuesta == pregunta["respuesta_correcta"] else "incorrecta"
        jugador = procesar_estado_mensaje(jugador, estado)

        puntos = aplicar_multiplicador(pregunta["puntos"], estado, jugador["multiplicador"])
        actualizar_puntajes(jugador, puntos, True)

        indice += 1

    # Calcular estadísticas finales
    jugador = calcular_estadisticas(jugador, limite_preguntas)

    # Pantalla final
    pantalla.fill(COLOR_BLANCO)
    if jugador["vidas"] == 0:
        dibujar_texto("💀 Te quedaste sin vidas", 250, 200)
    else:
        dibujar_texto("🎉 ¡Completaste la partida!", 230, 200)
    pygame.display.flip()
    pygame.time.wait(3000)

    return jugador
