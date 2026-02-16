import pygame
from estadisticas import leer_estadisticas, ordenar_estadisticas_por_puntaje
from colores_enum import Color
from pantalla_configuracion import dibujar_texto


def dibujar_encabezados(VENTANA,FUENTE,):
    encabezados = ["Jugador", "Puntaje", "Correctas", "Vidas"]
    x = [120, 320, 480, 640]
    
    for i in range(len(encabezados)):
        dibujar_texto(VENTANA,FUENTE,encabezados[i],x[i],100,color=Color.AZUL_OSCURO.value)


def dibujar_fila(VENTANA,FUENTE,jugador,y):
    datos = [jugador["jugador"], str(jugador["puntaje_total"]), str(jugador["racha_maxima_correctas"]), str(jugador["vidas"])]
    x = [120, 320, 480, 640]
    
    for i in range(len(datos)):
        dibujar_texto(VENTANA,FUENTE,datos[i],x[i],y,color=Color.NEGRO.value)
        
def dibujar_jugadores(VENTANA,FUENTE,estadisticas):
    y = 140
    for jugador in estadisticas[:5]:
        dibujar_fila(VENTANA,FUENTE,jugador, y)
        y += 35
        
def dibujar_puntajes(VENTANA,FUENTE,estadisticas):
    dibujar_texto(VENTANA,FUENTE,"Ranking de Jugadores",x=260,y=20,color=Color.AZUL_OSCURO.value)
    dibujar_encabezados(VENTANA,FUENTE,)
    dibujar_jugadores(VENTANA,FUENTE,estadisticas)
    dibujar_texto(VENTANA,FUENTE,"Presioná cualquier tecla o click para volver",127,500,color=Color.NEGRO.value)
    

def mostrar_puntajes(VENTANA,FUENTE,path):
    estadisticas = leer_estadisticas(path)
    ordenar_estadisticas_por_puntaje(estadisticas)

    while True:
        VENTANA.fill(Color.LAVANDA.value)
        dibujar_puntajes(VENTANA,FUENTE,estadisticas)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"

            if evento.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                return "menu"

