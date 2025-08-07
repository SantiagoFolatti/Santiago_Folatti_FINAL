import pygame

def inicializar_ventana(ancho=800, alto=600, titulo="TRIVIA PELÍCULAS", ruta_fondo=r"Santiago_Folatti_FINAL\imagenes_sonidospygame\fondo.jpg",
    ruta_icono=r"Santiago_Folatti_FINAL\imagenes_sonidospygame\utn_icono.jpg", ruta_sonido_click=r"Santiago_Folatti_FINAL\imagenes_sonidospygame\mouse-click-290204.mp3",
    tipo_fuente="Arial", tamaño_fuente=28):
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


def crear_boton(dimensiones, posicion, ventana,color_fondo=None, color_borde=None, imagen=None, fuente=None, texto=None):
    boton = {}
    boton["Ventana"] = ventana
    boton["Dimensiones"] = dimensiones
    boton["Posicion"] = posicion
    boton["ColorBorde"] = color_borde
    boton["Presionado"] = False
    boton["Hover"] = False

    if imagen != None:
        img = pygame.image.load(imagen)
        boton["Superficie"] = pygame.transform.scale(img, boton["Dimensiones"])
    else:
        tipo, tamaño = fuente
        fuente_render = pygame.font.SysFont(tipo, tamaño)
        texto_renderizado = fuente_render.render(texto, True, "black")

        if color_fondo != None:
            superficie_boton = pygame.Surface(dimensiones)
            superficie_boton.fill(color_fondo)

        # centrar texto
        rect_texto = texto_renderizado.get_rect(center=(dimensiones[0] // 2, dimensiones[1] // 2))
        superficie_boton.blit(texto_renderizado, rect_texto)
        
        if color_borde != None:
            pygame.draw.rect(superficie_boton, color_borde, superficie_boton.get_rect(), 2)

        boton["Superficie"] = superficie_boton

    boton["Rectangulo"] = boton["Superficie"].get_rect()
    boton["Rectangulo"].topleft = posicion

    return boton

def crear_botones(VENTANA):
    boton_configuracion = crear_boton(dimensiones=(70, 70),posicion=(20, 20),ventana=VENTANA,imagen=r"Santiago_Folatti_FINAL\imagenes_sonidospygame\ruedita.png")
    boton_jugar = crear_boton(dimensiones=(300, 80),posicion=(0, 200),ventana=VENTANA,fuente=("comic sans", 40),texto="Jugar",color_borde="grey",color_fondo="grey")
    boton_opciones = crear_boton(dimensiones=(300, 80),posicion=(0, 300),ventana=VENTANA,fuente=("comic sans", 40),texto="Opciones",color_borde="grey",color_fondo="grey")
    boton_puntajes = crear_boton(dimensiones=(300, 80),posicion=(0, 400),ventana=VENTANA,fuente=("comic sans", 40),texto="Puntajes",color_borde="grey",color_fondo="grey")
    boton_menos_preg = crear_boton((70, 70), (150, 110), VENTANA,imagen=r"Santiago_Folatti_FINAL\imagenes_sonidospygame\-.webp")
    boton_mas_preg = crear_boton((70, 70), (580, 110), VENTANA,imagen=r"Santiago_Folatti_FINAL\imagenes_sonidospygame\+.webp")
    boton_menos_tiempo = crear_boton((70, 70), (150, 190), VENTANA,imagen=r"Santiago_Folatti_FINAL\imagenes_sonidospygame\-.webp")
    boton_mas_tiempo = crear_boton((70, 70), (580, 190), VENTANA,imagen=r"Santiago_Folatti_FINAL\imagenes_sonidospygame\+.webp")
    boton_menos_vidas = crear_boton((70, 70), (150, 270), VENTANA,imagen=r"Santiago_Folatti_FINAL\imagenes_sonidospygame\-.webp")
    boton_mas_vidas = crear_boton((70, 70), (580, 270), VENTANA,imagen=r"Santiago_Folatti_FINAL\imagenes_sonidospygame\+.webp")
    boton_guardar = crear_boton( dimensiones=(300, 80), posicion=(250, 500), ventana=VENTANA, fuente=("comic sans", 40), texto="Guardar", color_borde="grey",color_fondo="white")
    
    lista_botones_menu = [boton_configuracion, boton_jugar, boton_opciones, boton_puntajes]
    lista_botones_opciones = [boton_menos_preg, boton_mas_preg,boton_menos_tiempo, boton_mas_tiempo,boton_menos_vidas, boton_mas_vidas,boton_guardar]

    return lista_botones_menu,lista_botones_opciones

def dibujar_boton(boton):
    boton["Ventana"].blit(boton["Superficie"], boton["Posicion"])

def actualizar_hover_boton(boton, mouse_pos):
    if boton["Rectangulo"].collidepoint(mouse_pos):
        pygame.draw.rect(boton["Ventana"], "black", boton["Rectangulo"], 4)  
        boton["Hover"] = True
    else:
        if boton["ColorBorde"] != None:
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



