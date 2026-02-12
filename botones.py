import pygame

def inicializar_ventana(ancho=800, alto=600, titulo="TRIVIA PELÍCULAS", 
    ruta_fondo=r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\imagenes_sonidospygame\fondo.jpg",
    ruta_icono=r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\imagenes_sonidospygame\utn_icono.jpg", 
    ruta_sonido_click=r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\imagenes_sonidospygame\mouse-click-290204.mp3",
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


def crear_boton(dimensiones, posicion, ventana, color_fondo=None, color_borde=None, imagen=None, fuente=None, texto=None):
    boton = {
        "Ventana": ventana,
        "Dimensiones": dimensiones,
        "Posicion": posicion,
        "ColorBorde": color_borde,
        "ColorFondo": color_fondo,
        "Presionado": False,
        "Hover": False,
        "Esimagen": imagen is not None
    }
    if imagen:
        img = pygame.image.load(imagen)
        boton["Superficie"] = pygame.transform.scale(img, dimensiones)
    else:
        tipo, tamaño = fuente
        fuente_render = pygame.font.SysFont(tipo, tamaño)
        texto_renderizado = fuente_render.render(texto, True, "white")

        superficie_boton = pygame.Surface(dimensiones)
        if color_fondo:
            superficie_boton.fill(color_fondo)

        rect_texto = texto_renderizado.get_rect(center=(dimensiones[0] // 2, dimensiones[1] // 2))
        superficie_boton.blit(texto_renderizado, rect_texto)
        
        if color_borde:
            pygame.draw.rect(superficie_boton, color_borde, superficie_boton.get_rect(), 2)

        boton["Superficie"] = superficie_boton

    boton["Rectangulo"] = boton["Superficie"].get_rect(topleft=posicion)

    return boton

def dibujar_boton(boton):
    boton["Ventana"].blit(boton["Superficie"], boton["Posicion"])


def actualizar_hover_boton(boton, mouse_pos):
    if boton["Rectangulo"].collidepoint(mouse_pos) and not boton["Esimagen"]:
        pygame.draw.rect(boton["Ventana"], "black", boton["Rectangulo"], 4)  
        boton["Hover"] = True
    else:
        if boton["ColorBorde"]:
            pygame.draw.rect(boton["Ventana"], boton["ColorBorde"], boton["Rectangulo"], 2)
            boton["Hover"] = False

def dibujar_lista_botones(lista):
    mouse_pos = pygame.mouse.get_pos()
    for boton in lista:
        dibujar_boton(boton)
        actualizar_hover_boton(boton, mouse_pos)

def centrar_botones_en_x(lista_botones):
    for boton in lista_botones:
        ancho_ventana = boton["Ventana"].get_width()
        ancho_boton = boton["Dimensiones"][0]
        nueva_pos_x = (ancho_ventana - ancho_boton) // 2
        boton["Posicion"] = (nueva_pos_x, boton["Posicion"][1])
        boton["Rectangulo"].topleft = boton["Posicion"]
        

def detectar_click(botones, evento,click_sonido):
    resetear_botones(botones)
    
    for boton in botones.values():
        if boton["Rectangulo"].collidepoint(evento.pos):
            boton["Presionado"] = True
            click_sonido.play() 
            return boton
        
    return None

def resetear_botones(botones):
    for boton in botones.values():
        boton["Presionado"] = False

def crear_botones_menu(VENTANA):
    botones_menu ={
    "boton_opciones" : crear_boton(dimensiones=(70, 70),posicion=(20, 20),ventana=VENTANA,imagen=r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\imagenes_sonidospygame\ruedita.png"),
    "boton_jugar" : crear_boton(dimensiones=(300, 80),posicion=(0, 200),ventana=VENTANA,fuente=("comic sans", 40),texto="Jugar",color_borde="grey",color_fondo="grey"),
    "boton_configuracion" : crear_boton(dimensiones=(300, 80),posicion=(0, 300),ventana=VENTANA,fuente=("comic sans", 40),texto="Configuracion",color_borde="grey",color_fondo="grey"),
    "boton_puntajes" : crear_boton(dimensiones=(300, 80),posicion=(0, 400),ventana=VENTANA,fuente=("comic sans", 40),texto="Puntajes",color_borde="grey",color_fondo="grey")
    }
    return botones_menu

def crear_botones_opciones(VENTANA):
    botones_opciones = {
        "menos_preguntas": crear_boton((70, 70), (150, 110), VENTANA, imagen=r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\imagenes_sonidospygame\-.webp"),
        "mas_preguntas":   crear_boton((70, 70), (580, 110), VENTANA, imagen=r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\imagenes_sonidospygame\+.webp"),
        "menos_tiempo":    crear_boton((70, 70), (150, 190), VENTANA, imagen=r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\imagenes_sonidospygame\-.webp"),
        "mas_tiempo":      crear_boton((70, 70), (580, 190), VENTANA, imagen=r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\imagenes_sonidospygame\+.webp"),
        "menos_vidas":     crear_boton((70, 70), (150, 270), VENTANA, imagen=r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\imagenes_sonidospygame\-.webp"),
        "mas_vidas":       crear_boton((70, 70), (580, 270), VENTANA, imagen=r"C:\Users\user\Downloads\Santiago_Folatti_FINAL-main\Santiago_Folatti_FINAL-main\imagenes_sonidospygame\+.webp"),
        "guardar":         crear_boton((200, 60), (580, 500), VENTANA,fuente=("comic sans", 35), texto="Guardar",color_borde="grey", color_fondo="grey"),
        "salir":            crear_boton((200, 60), (20, 500), VENTANA, fuente=("comic sans", 35), texto="Salir", color_borde="grey", color_fondo="grey"),
        "facil":           crear_boton((150, 50), (150, 350), VENTANA, fuente=("comic sans", 30), texto="Fácil", color_borde="grey", color_fondo="grey"),
        "media":           crear_boton((150, 50), (325, 350), VENTANA, fuente=("comic sans", 30), texto="Media", color_borde="grey", color_fondo="grey"),
        "dificil":         crear_boton((150, 50), (500, 350), VENTANA, fuente=("comic sans", 30), texto="Difícil", color_borde="grey", color_fondo="grey"),
    }
    return botones_opciones
