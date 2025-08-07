import pygame
import sys

# Inicialización
pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Menú Principal")
fuente = pygame.font.SysFont("Arial", 36)

# Colores
COLOR_FONDO = (255, 255, 255)
COLOR_TEXTO = (0, 0, 0)
COLOR_BOTON = (200, 220, 255)
COLOR_BORDE = (0, 0, 0)

# Botones
def dibujar_boton(texto, x, y, ancho, alto):
    rect = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(pantalla, COLOR_BOTON, rect)
    pygame.draw.rect(pantalla, COLOR_BORDE, rect, 2)

    texto_render = fuente.render(texto, True, COLOR_TEXTO)
    texto_rect = texto_render.get_rect(center=rect.center)
    pantalla.blit(texto_render, texto_rect)

    return rect

# Texto centrado
def dibujar_texto(texto, x, y):
    render = fuente.render(texto, True, COLOR_TEXTO)
    pantalla.blit(render, (x, y))
    
# Menú principal
def mostrar_menu():
    while True:
        pantalla.fill(COLOR_FONDO)
        dibujar_texto("Juego de Preguntas", 260, 80)

        boton_jugar = dibujar_boton("Jugar", 280, 200, 240, 60)
        boton_config = dibujar_boton("Configuración", 280, 290, 240, 60)
        boton_puntajes = dibujar_boton("Puntajes Máximos", 280, 380, 240, 60)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if boton_jugar.collidepoint(x, y):
                    return "jugar"
                elif boton_config.collidepoint(x, y):
                    return "configuracion"
                elif boton_puntajes.collidepoint(x, y):
                    return "puntajes"

