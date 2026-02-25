import pygame
from colores_enum import Color
from pantalla_configuracion import dibujar_texto_centrado
from botones import botones_input,dibujar_lista_botones

def crear_input(VENTANA, FUENTE, color_activo, color_inactivo, posicion, dimension):
    input = {}
    input["Ventana"] = VENTANA
    input["Fuente"] = pygame.font.SysFont(FUENTE[0],FUENTE[1])
    input["ColorActivo"] = color_activo
    input["ColorInactivo"] = color_inactivo
    input["Posicion"] = posicion
    input["Dimenciones"] = dimension
    input["Texto"] = ""
    input["Activo"] = False
    input["Rectangulo"] = pygame.Rect(posicion,dimension)
    input["ColorActual"] = input["ColorInactivo"]

    return input

def escribir(input, evento):
    if evento.key == pygame.K_ESCAPE:
        input["Texto"] = "" 
    elif evento.key == pygame.K_BACKSPACE:
        input["Texto"] = input["Texto"][:-1]
    else:
        input["Texto"] += evento.unicode

###################################################################################

def dibujar_input(input):
    texto = input["Fuente"].render(input["Texto"], False, input["ColorActual"])
    x = input["Rectangulo"].x
    y = input["Rectangulo"].y
    input["Ventana"].blit(texto, (x+5, y+7))
    input["Rectangulo"].w = max(100,texto.get_width() + 10)
    pygame.draw.rect(input["Ventana"], input["ColorActual"], input["Rectangulo"], 3)

def definir_color_activo(inputs):
    for input in inputs:
        if input["Activo"]:
            input["ColorActual"] = input["ColorActivo"]
        else:
            input["ColorActual"] = input["ColorInactivo"]
            
        dibujar_input(input)

def dibujar_pantalla_input(VENTANA,FONDO,FUENTE,inputs,botones):
    VENTANA.blit(FONDO,(0,0))
    dibujar_lista_botones(botones.values())
    dibujar_texto_centrado(VENTANA,FUENTE,"Ingrese el nombre del jugador 1", 200,Color.TEXTO.value)
    dibujar_texto_centrado(VENTANA,FUENTE,"Ingrese el nombre del jugador 2", 300,Color.TEXTO.value)
    definir_color_activo(inputs)
    pygame.display.update()

###################################################################################

def mostrar_input(VENTANA,FUENTE,FONDO):
    botones = botones_input(VENTANA)
    input1 =crear_input(VENTANA, ("consolas", 20),Color.AZUL_OSCURO.value,"red",(340, 250),(150,30))
    input2 = crear_input(VENTANA, ("consolas", 20),Color.AZUL_OSCURO.value,"red",(340, 350),(150,30))
    inputs = [input1,input2]
    
    while True:
        dibujar_pantalla_input(VENTANA,FONDO,FUENTE,inputs,botones)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir",[None,None]

            if evento.type == pygame.MOUSEBUTTONDOWN:
                for input in inputs:
                    input["Activo"] = input["Rectangulo"].collidepoint(evento.pos)

                if botones["volver"]["Rectangulo"].collidepoint(evento.pos):
                    return "menu",[None,None]
                
                if botones["jugar"]["Rectangulo"].collidepoint(evento.pos):
                    if input1["Texto"].strip() != "" and input2["Texto"].strip() != "":
                        return "jugar",[input1["Texto"],input2["Texto"]]
                
            if evento.type == pygame.KEYDOWN:
                for input in inputs:
                    if input["Activo"]:
                        escribir(input, evento)