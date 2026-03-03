import pygame
from estadisticas import leer_estadisticas, ordenar_estadisticas_por_puntaje
from colores_enum import Color
from pantalla_configuracion import dibujar_texto,dibujar_texto_centrado



def dibujar_encabezados(VENTANA:pygame.surface, FUENTE:pygame.font) -> None:
    encabezados = ["Jugador", "Puntaje", "Correctas", "Vidas"]
    x = [120, 320, 480, 640]
    
    for i in range(len(encabezados)):
        dibujar_texto(VENTANA,FUENTE,encabezados[i],x[i],100,Color.TEXTO.value)


def dibujar_nombre_podio(VENTANA,FUENTE,datos,x,y,puesto):
    colores_podio = [Color.DORADO.value, Color.PLATA.value, Color.BRONCE.value]
    
    if puesto < len(colores_podio):
        color_nombre = colores_podio[puesto]
    else:
        color_nombre = Color.TEXTO.value
    
    dibujar_texto(VENTANA,FUENTE,datos[0],x[0],y,color_nombre)


def dibujar_fila(VENTANA,FUENTE,jugador,y,puesto):
    datos = [jugador["jugador"], str(jugador["puntaje_total"]), str(jugador["racha_maxima_correctas"]), str(jugador["vidas"])]
    x = [120, 320, 480, 640]
    
    dibujar_nombre_podio(VENTANA,FUENTE,datos,x,y,puesto)
    
    for i in range(1,len(datos)):
        dibujar_texto(VENTANA,FUENTE,datos[i],x[i],y,Color.TEXTO.value)


def dibujar_jugadores(VENTANA,FUENTE,estadisticas):
    y = 140
    puesto = 0
    for jugador in estadisticas[:5]:
        dibujar_fila(VENTANA,FUENTE,jugador, y,puesto)
        y += 35
        puesto += 1


def dibujar_puntajes(VENTANA,FUENTE,estadisticas):
    FONDO = pygame.image.load(r"imagenes_sonidospygame\FONDO TOPS (2).png")
    FONDO = pygame.transform.scale(FONDO,(800,600))
    VENTANA.blit(FONDO,(0,0))
    dibujar_texto_centrado(VENTANA,FUENTE,"Ranking de Jugadores",20,Color.TEXTO.value)
    dibujar_encabezados(VENTANA,FUENTE)
    dibujar_jugadores(VENTANA,FUENTE,estadisticas)
    dibujar_texto_centrado(VENTANA,FUENTE,"Presioná cualquier tecla o click para volver",500,Color.TEXTO.value)
    pygame.display.update()
    

def mostrar_puntajes(VENTANA,FUENTE,path):
    estadisticas = leer_estadisticas(path)
    ordenar_estadisticas_por_puntaje(estadisticas)

    while True:
        dibujar_puntajes(VENTANA,FUENTE,estadisticas)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"

            if evento.type == pygame.MOUSEBUTTONDOWN:
                return "menu"

