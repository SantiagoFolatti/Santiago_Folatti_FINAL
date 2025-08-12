import pygame
import sys
from estadisticas import leer_estadisticas, ordenar_estadisticas_por_puntaje
from pantalla_configuracion import dibujar_texto

# Inicializar pygame (si aún no lo hiciste en main)
pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ranking de Jugadores")
fuente = pygame.font.SysFont("Arial", 26)
COLOR_BLANCO = (255, 255, 255)
COLOR_TEXTO = (0, 0, 0)
COLOR_TITULO = (50, 50, 200)


def mostrar_puntajes(path):
    estadisticas = leer_estadisticas(path)
    ordenar_estadisticas_por_puntaje(estadisticas)

    corriendo = True
    while corriendo:
        pantalla.fill(COLOR_BLANCO)
        dibujar_texto("Ranking de Jugadores", 240, 30)

        y = 80
        dibujar_texto("Jugador     Puntaje     Correctas    Vidas", 100, y)
        y += 30

        tope = 5 if len(estadisticas) >= 5 else len(estadisticas)

        for i in range(tope):
            jugador = estadisticas[i]
            linea = f"{jugador['jugador']:<12} {jugador['puntaje_total']:<10} {jugador['racha_maxima_correctas']:<12} {jugador['vidas']}"
            dibujar_texto(linea, 100, y)
            y += 30

        dibujar_texto("Presioná cualquier tecla para volver", 200, 500)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                corriendo = False
