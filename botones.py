import pygame
from colores_enum import Color

def inicializar_ventana(ancho=800, alto=600, titulo="TRIVIA PELÍCULAS", 
    ruta_fondo=r"imagenes_sonidospygame\FONDO1.png",
    ruta_icono=r"imagenes_sonidospygame\utn_icono.jpg", 
    ruta_sonido_click=r"imagenes_sonidospygame\mouse-click-290204.mp3",
    tipo_fuente="Comic Sans", tamaño_fuente=28):

    pygame.init()

    fondo = pygame.image.load(ruta_fondo)
    fondo = pygame.transform.scale(fondo, (ancho, alto))

    VENTANA = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(titulo)

    icono = pygame.image.load(ruta_icono)
    pygame.display.set_icon(icono)
    
    click_sonido = pygame.mixer.Sound(ruta_sonido_click)
    fuente = pygame.font.SysFont(tipo_fuente, tamaño_fuente)

    return VENTANA, fondo, click_sonido, fuente


def crear_boton(ventana,dimensiones,posicion,color_fondo=None,color_borde=None,fuente=None,texto=None,color_texto = None,imagen=None):
    boton = {
        "Ventana": ventana,
        "Dimensiones": dimensiones,
        "Posicion": posicion,
        "ColorFondo": color_fondo,
        "ColorBorde": color_borde,
        "Presionado": False,
        "Hover": False,
        "Fuente": fuente,
        "Texto": texto,
        "Esimagen": imagen is not None,
        "ColorTexto": color_texto
    }
    if imagen:
        img = pygame.image.load(imagen)
        boton["Superficie"] = pygame.transform.scale(img, dimensiones)
    else:
        tipo, tamaño = fuente
        fuente_render = pygame.font.SysFont(tipo, tamaño)
        texto_renderizado = fuente_render.render(texto, True, boton["ColorTexto"])

        superficie_boton = pygame.Surface(dimensiones)
        
        if color_fondo:
            superficie_boton.fill(color_fondo)

        if color_borde:
            pygame.draw.rect(superficie_boton, color_borde, superficie_boton.get_rect(), 2)
            
        rect_texto = texto_renderizado.get_rect(center=(dimensiones[0] // 2, dimensiones[1] // 2))
        superficie_boton.blit(texto_renderizado, rect_texto)
        
        boton["Superficie"] = superficie_boton
    boton["Rectangulo"] = boton["Superficie"].get_rect(topleft=posicion)

    return boton


def dibujar_boton(boton:dict) -> None:
    boton["Ventana"].blit(boton["Superficie"], boton["Posicion"])


def dibujar_lista_botones(botones:list) -> None:
    mouse_pos = pygame.mouse.get_pos()
    for boton in botones:
        dibujar_boton(boton)
        actualizar_hover_boton(boton, mouse_pos)


########################################################################################################


def detectar_click(botones:dict, evento,click_sonido) -> dict|None:
    resetear_botones(botones)
    for boton in botones.values():
        if boton["Rectangulo"].collidepoint(evento.pos):
            boton["Presionado"] = True
            click_sonido.play() 
            return boton
        
    return None


def resetear_botones(botones:dict) -> None:
    for boton in botones.values():
        boton["Presionado"] = False


def actualizar_hover_boton(boton:dict, mouse_pos) -> None:
    if boton["Rectangulo"].collidepoint(mouse_pos) and not boton["Esimagen"]:
        pygame.draw.rect(boton["Ventana"], "black", boton["Rectangulo"], 4)  
        boton["Hover"] = True
    elif boton["ColorBorde"]:
        pygame.draw.rect(boton["Ventana"], boton["ColorBorde"], boton["Rectangulo"], 2)
        boton["Hover"] = False


def repintar_boton(boton:dict) -> None:
    superficie = pygame.Surface(boton["Dimensiones"])
    superficie.fill(boton["ColorFondo"])

    tipo, tamaño = boton["Fuente"]
    fuente = pygame.font.SysFont(tipo, tamaño)

    texto_render = fuente.render(boton["Texto"], True, boton["ColorTexto"])
    rect_texto = texto_render.get_rect(center=(boton["Dimensiones"][0] // 2, boton["Dimensiones"][1] // 2))

    superficie.blit(texto_render, rect_texto)

    boton["Superficie"] = superficie


########################################################################################################


def botones_menu(VENTANA) -> dict:
    botones_menu ={
    "boton_jugar" :         crear_boton(VENTANA,(300, 80),(250, 100),"grey","grey",("comic sans", 40),"Jugar","white"),
    "boton_minijuego" :     crear_boton(VENTANA,(300, 80),(250, 200),"grey","grey",("comic sans", 40),"Minijuego","white"),
    "boton_configuracion" : crear_boton(VENTANA,(300, 80),(250, 300),"grey","grey",("comic sans", 40),"Configuracion","white"),
    "boton_puntajes" :      crear_boton(VENTANA,(300, 80),(250, 400),"grey","grey",("comic sans", 40),"Puntajes","white")
    }
    return botones_menu


def botones_configuracion(VENTANA) -> dict:
    botones_config = {
        "menos_preguntas": crear_boton(VENTANA,(45, 45), (490, 125),imagen=r"imagenes_sonidospygame\-.png"),
        "mas_preguntas":   crear_boton(VENTANA,(45, 45), (550, 125),imagen=r"imagenes_sonidospygame\+.png"),
        "menos_tiempo":    crear_boton(VENTANA,(45, 45), (490, 205),imagen=r"imagenes_sonidospygame\-.png"),
        "mas_tiempo":      crear_boton(VENTANA,(45, 45), (550, 205),imagen=r"imagenes_sonidospygame\+.png"),
        "menos_vidas":     crear_boton(VENTANA,(45, 45), (490, 285),imagen=r"imagenes_sonidospygame\-.png"),
        "mas_vidas":       crear_boton(VENTANA,(45, 45), (550, 285),imagen=r"imagenes_sonidospygame\+.png"),
        "guardar":         crear_boton(VENTANA,(180, 60), (580, 500),"grey","grey",("comic sans", 35),"Guardar","white"),
        "salir":           crear_boton(VENTANA,(180, 60), (20, 500),"grey","grey",("comic sans", 35),"Salir","white"),
        "Facil":           crear_boton(VENTANA,(150, 50), (150, 380),"grey","grey",("comic sans", 30),"Fácil","white"),
        "Media":           crear_boton(VENTANA,(150, 50), (325, 380),"grey","grey",("comic sans", 30),"Media","white"),
        "Dificil":         crear_boton(VENTANA,(150, 50), (500, 380),"grey","grey",("comic sans", 30),"Difícil","white"),
    }
    return botones_config


def botones_opciones(VENTANA,pregunta:dict) -> dict:
    botones_opciones = {
        "A": crear_boton(VENTANA,(520, 60), (140, 260),"white","white",("comic sans", 35),"A: " + pregunta["opciones"]["A"],Color.AZUL_OSCURO.value),
        "B": crear_boton(VENTANA,(520, 60), (140, 340),"white","white",("comic sans", 35),"B: " + pregunta["opciones"]["B"],Color.AZUL_OSCURO.value),
        "C": crear_boton(VENTANA,(520, 60), (140, 420),"white","white",("comic sans", 35),"C: " + pregunta["opciones"]["C"],Color.AZUL_OSCURO.value),
    }
    return botones_opciones


def botones_input(VENTANA) -> dict:
    botones_input = {
        "jugar" :  crear_boton(VENTANA,(180, 60), (600, 500),"grey","grey",("comic sans", 35),"Jugar","white"),
        "volver":   crear_boton(VENTANA,(180, 60), (20, 500),"grey","grey",("comic sans", 35),"Volver","white")
    }
    return botones_input