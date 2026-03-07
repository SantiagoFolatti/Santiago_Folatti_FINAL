import pygame
from Logica.configuracion import leer_configuracion, guardar_configuracion
from Juego.botones import botones_configuracion,repintar_boton,dibujar_lista_botones, detectar_click
from Juego.colores_enum import Color



def dibujar_texto(VENTANA:pygame.surface, FUENTE:pygame.font, texto:str, x:int, y:int, color: tuple[int, int, int]) -> None:
    render = FUENTE.render(texto, True, color)
    VENTANA.blit(render, (x, y))


def dibujar_texto_centrado(VENTANA:pygame.surface, FUENTE:pygame.font, texto:str, y:int, color: tuple[int, int, int]) -> None:
    render = FUENTE.render(texto, True, color)
    x = (VENTANA.get_width() - render.get_width()) // 2
    VENTANA.blit(render, (x, y))


def resaltar_dificultad(botones:dict, config:dict) -> None:
    for clave in ["Facil", "Media", "Dificil"]:
        if config["dificultad"] == clave:
            botones[clave]["ColorFondo"] = Color.GRIS_OSCURO.value
            botones[clave]["ColorBorde"] = Color.NEGRO.value
        else:
            botones[clave]["ColorFondo"] = Color.GRIS_CLARO.value
            botones[clave]["ColorBorde"] = Color.GRIS_CLARO.value

        repintar_boton(botones[clave])


def dibujar_configuracion(VENTANA:pygame.surface, FUENTE:pygame.font.Font, config:dict, botones:dict) -> None:
    FONDO = pygame.image.load(r"imagenes_sonidos\configuracion.png")
    FONDO = pygame.transform.scale(FONDO,(800,600))
    VENTANA.blit(FONDO,(0,0))
    
    dibujar_texto_centrado(VENTANA,FUENTE,"CONFIGURACIÓN DEL JUEGO",30,Color.TEXTO.value)
    dibujar_texto(VENTANA,FUENTE,f"PREGUNTAS:  {config['cantidad_preguntas']}",195,125,Color.TEXTO.value)
    dibujar_texto(VENTANA,FUENTE,f"TIEMPO: {config['tiempo_por_pregunta']} seg",195,205,Color.TEXTO.value)
    dibujar_texto(VENTANA,FUENTE,f"VIDAS:  {config['vidas']}",195,285,Color.TEXTO.value)
    
    resaltar_dificultad(botones,config)
    dibujar_lista_botones(botones.values())
    pygame.display.update()


###################################################################################


def accion_sumar(clave_config:str, config:dict, maximo:int) -> None:
    if config[clave_config] < maximo:
        config[clave_config] += 1

def accion_restar(clave_config:str, config:dict, minimo:int) -> None:
    if config[clave_config] > minimo:
        config[clave_config] -= 1

def accion_dificultad(config:dict, valor_dificultad:str) -> None:
    config["dificultad"] = valor_dificultad

def accion_guardar(path_config:str, config:dict)-> str:
    guardar_configuracion(path_config, config)
    return "guardar"

def accion_salir() -> None:
    return "salir"

def diccionario_acciones(config:dict, path_config:str) -> dict:
    return {
        "menos_preguntas" : (accion_restar,["cantidad_preguntas", config, 1]),
        "mas_preguntas" : (accion_sumar, ["cantidad_preguntas", config,12]),
        
        "menos_tiempo" : (accion_restar, ["tiempo_por_pregunta", config, 1]),
        "mas_tiempo" : (accion_sumar, ["tiempo_por_pregunta", config,30]),
        
        "menos_vidas" : (accion_restar, ["vidas", config, 1]),
        "mas_vidas" : (accion_sumar, ["vidas", config,6]),
        
        "Facil" : (accion_dificultad, [config, "Facil"]),
        "Media" : (accion_dificultad, [config, "Media"]),
        "Dificil" : (accion_dificultad, [config, "Dificil"]),
        
        "guardar" : (accion_guardar, [path_config, config]),
        "salir" : (accion_salir, [])
    }


###################################################################################


def mostrar_configuracion(VENTANA:pygame.surface, CLICK_SONIDO:pygame.mixer.Sound, FUENTE:pygame.font.Font, path_config:str) -> str:
    botones = botones_configuracion(VENTANA)  
    config = leer_configuracion(path_config)
    acciones = diccionario_acciones(config, path_config)
    
    while True:
        dibujar_configuracion(VENTANA,FUENTE,config, botones)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                boton = detectar_click(botones, evento, CLICK_SONIDO)
                for clave, valor in botones.items():
                    if boton is valor:
                        funcion, args = acciones[clave] # value de diccionario_acciones(funcion + parametros)
                        resultado = funcion(*args) # El * desempaqueta la lista en diccionario de acciones y pasa los valores como parametros 

                        if resultado  == "guardar" or resultado == "salir":
                            return "menu"

