import pygame
import sys
from datos import leer_preguntas_csv
from menu_pygame import dibujar_texto

# Inicializar Pygame
pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Preguntas y Respuestas")
fuente = pygame.font.SysFont("Arial", 28)
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)
COLOR_OPCION = (200, 220, 255)
COLOR_CORRECTO = (150, 255, 150)
COLOR_INCORRECTO = (255, 150, 150)


def mostrar_pregunta_pygame(pregunta, seleccion=None):
    pantalla.fill(COLOR_BLANCO)
    dibujar_texto("Categoría: " + pregunta["categoria"] + " | Dificultad: " + pregunta["dificultad"], 50, 30)
    dibujar_texto(pregunta["pregunta"], 50, 90)

    claves = ["A", "B", "C"]
    botones = {}
    i = 0
    for clave in claves:
        opcion_texto = clave + ": " + pregunta["opciones"][clave]
        y = 180 + i * 90
        rect = pygame.Rect(50, y, 700, 60)

        color = COLOR_OPCION
        if seleccion != None:
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
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                for clave in botones:
                    rect = botones[clave]
                    if rect.collidepoint(x, y):
                        return clave

def iniciar_juego_grafico(configuracion: dict):
    preguntas = leer_preguntas_csv("Santiago_Folatti_FINAL/preguntas.csv")
    preguntas = preguntas[:configuracion["cantidad_preguntas"]]

    vidas = configuracion["vidas"]
    indice = 0

    while indice < len(preguntas):
        pregunta = preguntas[indice]
        botones = mostrar_pregunta_pygame(pregunta)
        respuesta = obtener_respuesta_click(botones)

        mostrar_pregunta_pygame(pregunta, seleccion=respuesta)
        pygame.time.wait(2000)

        if respuesta != pregunta["respuesta_correcta"]:
            vidas -= 1
            if vidas == 0:
                break

        indice += 1

    pantalla.fill(COLOR_BLANCO)
    if vidas == 0:
        dibujar_texto("Te quedaste sin vidas", 250, 200)
    else:
        dibujar_texto("¡Completaste la partida!", 230, 200)
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()
    sys.exit()

