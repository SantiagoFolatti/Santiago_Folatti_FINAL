import pygame
from funcion_jugar import jugar_preguntas_y_respuestas
from estadisticas import leer_estadisticas, mostrar_estadisticas
from ingresos import *
from Parcial2.minijuego.minijuego import juego
from configuracion import cambiar_configuracion
from funciones_mostrar import mostrar_un_mensaje

# Inicialización
pygame.init()
ANCHO, ALTO = 1600, 900
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("MOVIE TRIVIA TIME!")

# Cargar fondo e íconos
fondo = pygame.image.load("Parcial2/imagenes_sonidospygame/fondopelicula.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
icono = pygame.image.load("Parcial2/imagenes_sonidospygame/utn_icono.jpg")
pygame.display.set_icon(icono)

# Fuente
fuente_titulo = pygame.font.SysFont("Comic Sans", 90)
fuente_boton = pygame.font.SysFont("Comic Sans", 50)

# Colores
BLANCO = (255, 255, 255)
GRIS = (100, 100, 100)

# Función para crear botón y detectar clic
def crear_boton(texto, x, y, ancho, alto):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect = pygame.Rect(x, y, ancho, alto)

    # Hover
    color = GRIS if rect.collidepoint(mouse) else BLANCO
    pygame.draw.rect(ventana, color, rect, border_radius=10)

    texto_render = fuente_boton.render(texto, True, (0, 0, 0))
    ventana.blit(texto_render, texto_render.get_rect(center=rect.center))

    if rect.collidepoint(mouse) and click[0]:
        pygame.time.wait(200)  # Evita doble clic rápido
        return True
    return False

# Bucle principal
bandera = True
while bandera:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False

    ventana.blit(fondo, (0, 0))

    # Título
    texto_titulo = fuente_titulo.render("MENÚ PRINCIPAL", True, BLANCO)
    ventana.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, 80))

    # Botones
    if crear_boton("Configuración", 600, 250, 400, 60):
        cambiar_configuracion("Parcial2/config.json")

    if crear_boton("Preguntas y Respuestas", 600, 330, 400, 60):
        jugar_preguntas_y_respuestas()

    if crear_boton("Ta-Te-Ti", 600, 410, 400, 60):
        mostrar_un_mensaje("¡Bienvenido al Ta-Te-Ti!")
        juego()

    if crear_boton("Estadísticas", 600, 490, 400, 60):
        estadisticas = leer_estadisticas("Parcial2/estadisticas.csv")
        mostrar_estadisticas(estadisticas)

    if crear_boton("Salir", 600, 570, 400, 60):
        mostrar_un_mensaje("¡Gracias por jugar! Hasta la próxima.")
        bandera = False

    pygame.display.update()

pygame.quit()

import pygame

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
fuente = pygame.font.SysFont("arial", 30)

botones = {
    "configuracion": pygame.Rect(300, 100, 200, 50),
    "preguntas": pygame.Rect(300, 180, 200, 50),
    "tateti": pygame.Rect(300, 260, 200, 50),
    "estadisticas": pygame.Rect(300, 340, 200, 50),
    "salir": pygame.Rect(300, 420, 200, 50),
}

def dibujar_menu():
    pantalla.fill((30, 30, 30))
    for texto, rect in botones.items():
        pygame.draw.rect(pantalla, (70, 130, 180), rect)
        render = fuente.render(texto.capitalize(), True, (255, 255, 255))
        pantalla.blit(render, (rect.x + 20, rect.y + 10))
    pygame.display.flip()

running = True
while running:
    dibujar_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for key, rect in botones.items():
                if rect.collidepoint(x, y):
                    print(f"Botón presionado: {key}")  # luego aquí redireccionas a otra pantalla
pygame.quit()
