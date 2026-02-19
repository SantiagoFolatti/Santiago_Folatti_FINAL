import pygame
from minijuego import crear_matriz,cambiar_jugador
from recorrido import verificar_victoria,verificar_empate
from pantalla_configuracion import dibujar_texto
from colores_enum import Color
from pantalla_juego import esperar_salida_final


def parametros_minijuego():
    FONDO_MINIJUEGO = pygame.image.load(r"imagenes_sonidospygame\tictactoe_background.png")

    circulo = pygame.image.load(r"imagenes_sonidospygame\circle.png")
    circulo = pygame.transform.scale(circulo, (130, 130))
    equis = pygame.image.load(r"imagenes_sonidospygame\x (1).png")
    equis = pygame.transform.scale(equis, (130, 130))

    coor = [[(115, 80), (335, 80), (555, 80)],
            [(115, 250), (335, 250), (555, 250)],
            [(115, 420), (335, 420), (555, 420)]]
    
    return FONDO_MINIJUEGO, circulo, equis, coor

def graficar_tablero(VENTANA,FONDO,equis,circulo,coor,tablero):
    VENTANA.blit(FONDO, (0, 0))
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == "X":
                dibujar_x_o(VENTANA,equis,coor,i,j)
            elif tablero[i][j] == "O":
                dibujar_x_o(VENTANA,circulo,coor,i,j)

def dibujar_x_o(VENTANA,ficha,coor,i, j):
    VENTANA.blit(ficha, coor[i][j])

def obtener_celda(event):
    mouse_x, mouse_y = event.pos

    if not (90 <= mouse_x < 680 and 60 <= mouse_y < 540):
        return None,None
        
    fila = (mouse_y - 60) // 170
    columna = (mouse_x - 70) // 220

    return fila,columna

def mostrar_resultado(VENTANA, FONDO, equis, circulo, coor, tablero, FUENTE, mensaje):
    graficar_tablero(VENTANA,FONDO,equis,circulo,coor,tablero)
    dibujar_texto(VENTANA,FUENTE,mensaje, x=340, y=10, color=Color.BLANCO.value)
    pygame.display.update()
    return esperar_salida_final()

def mostrar_minijuego(VENTANA,FUENTE):
    FONDO_MINIJUEGO, circulo, equis, coor = parametros_minijuego()
    FONDO = pygame.transform.scale(FONDO_MINIJUEGO, VENTANA.get_size())
    tablero = crear_matriz(3, 3, " ")
    jugador = "X"
    clock = pygame.time.Clock()
    
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    fila,columna = obtener_celda(event)
                    if fila is None:
                        continue

                    if tablero[fila][columna] == " ":
                        tablero[fila][columna] = jugador
                        
                        if verificar_victoria(len(tablero), tablero, jugador):
                            return mostrar_resultado(VENTANA, FONDO, equis, circulo, coor, tablero, FUENTE, f"Ganó {jugador}")
                        
                        if verificar_empate(tablero):
                            return mostrar_resultado(VENTANA, FONDO, equis, circulo, coor, tablero, FUENTE,"¡Empate!")

                        jugador = cambiar_jugador(jugador)

        graficar_tablero(VENTANA,FONDO,equis,circulo,coor,tablero)
        pygame.display.update()

