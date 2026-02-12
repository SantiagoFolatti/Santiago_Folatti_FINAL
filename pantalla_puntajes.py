import pygame
from estadisticas import leer_estadisticas, ordenar_estadisticas_por_puntaje
from colores_enum import Color
from botones import inicializar_ventana


def dibujar_titulo(ventana, fuente):
    texto = fuente.render("Ranking de Jugadores", True, Color.NEGRO.value)
    rect = texto.get_rect(center=(ventana.get_width() // 2, 40))
    ventana.blit(texto, rect)


def dibujar_encabezado(ventana, fuente, y):
    encabezados = ["Jugador", "Puntaje", "Correctas", "Vidas"]
    x_positions = [120, 320, 480, 640]

    for texto, x in zip(encabezados, x_positions):
        render = fuente.render(texto, True, Color.NEGRO.value)
        ventana.blit(render, (x, y))


def dibujar_fila(ventana, fuente, jugador, y):
    datos = [
        jugador["jugador"],
        str(jugador["puntaje_total"]),
        str(jugador["racha_maxima_correctas"]),
        str(jugador["vidas"])
    ]
    x_positions = [120, 320, 480, 640]

    for dato, x in zip(datos, x_positions):
        render = fuente.render(dato, True, Color.NEGRO.value)
        ventana.blit(render, (x, y))


def mostrar_puntajes(path):
    ventana, fondo, _, fuente = inicializar_ventana()
    estadisticas = leer_estadisticas(path)
    ordenar_estadisticas_por_puntaje(estadisticas)

    while True:
        ventana.blit(fondo, (0, 0))
        ventana.fill(Color.BLANCO.value)

        dibujar_titulo(ventana, fuente)
        dibujar_encabezado(ventana, fuente, 100)

        y = 140
        for jugador in estadisticas[:5]:
            dibujar_fila(ventana, fuente, jugador, y)
            y += 35

        texto_volver = fuente.render(
            "Presioná cualquier tecla o click para volver",
            True,
            Color.NEGRO.value
        )
        rect_volver = texto_volver.get_rect(center=(ventana.get_width() // 2, 520))
        ventana.blit(texto_volver, rect_volver)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"

            if evento.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                return "menu"

