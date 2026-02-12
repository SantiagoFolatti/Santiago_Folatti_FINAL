from funciones_mostrar import *
from funciones_categorias import seleccionar_pregunta_por_categoria
from rondas import jugar_ronda
from estado_jugador import aplicar_multiplicador, procesar_estado_mensaje, inicializar_jugador
from ingresos import ingresar_nombre_jugador, obtener_dificultad
from estadisticas import guardar_estadisticas
from datos import leer_preguntas_csv
from configuracion import leer_configuracion
import random

def actualizar_puntajes(jugador: dict, puntos: int, respondida: bool):
    jugador["puntaje_total"] += puntos
    if respondida:
        jugador["respondidas"] += 1

def calcular_estadisticas(jugador: dict,limite_preguntas:int) -> dict:
    if jugador["respondidas"] > 0:
        jugador["porcentaje_aciertos"] = (jugador["respuestas_correctas"] / limite_preguntas) * 100  
        jugador["promedio_puntos"] = jugador["puntaje_total"] / jugador["respondidas"]
        jugador["tiempo_promedio"] = jugador["tiempo_total"] / jugador["respondidas"]
    return jugador

################################################################################################################################################

def realizar_turno(jugador:dict, pregunta:dict, tiempo_max: int) -> dict:
    mostrar_estado_jugador(jugador,tiempo_max)
    mostrar_pregunta(pregunta)

    resultado_ronda = jugar_ronda(pregunta, tiempo_max)
    estado = resultado_ronda["estado"]
    base_puntos = pregunta["puntos"]

    jugador = procesar_estado_mensaje(jugador,estado)
    puntos_finales = aplicar_multiplicador(base_puntos, estado, jugador["multiplicador"])
    resultado_ronda["puntos_obtenidos"] = puntos_finales

    mostrar_detalle_ronda(pregunta,resultado_ronda)
    actualizar_puntajes(jugador, resultado_ronda["puntos_obtenidos"], resultado_ronda["respondida"])
    jugador["tiempo_total"] += resultado_ronda["tiempo_usado"]

    pausar_y_limpiar("🔄 Presione ENTER para continuar...")
    
    return jugador

def verificar_vidas(jugador: dict):
    if jugador["vidas"] == 0:
        mostrar_un_mensaje("💔 Has perdido todas tus vidas. Fin del juego.")


def jugar(preguntas: list, configuracion: dict, dificultad: str) -> dict:
    preguntas_restantes = preguntas.copy()
    limite_preguntas = configuracion["cantidad_preguntas"]
    tiempo_max = configuracion["tiempo_por_pregunta"]
    jugador = inicializar_jugador(configuracion)

    while preguntas_restantes and jugador["respondidas"] < limite_preguntas and jugador["vidas"] > 0:
        categorias_disponibles = mostrar_estado_partida(preguntas_restantes, jugador["respondidas"], limite_preguntas)
        categoria_aleatoria = random.choice(categorias_disponibles).lower().strip()
        pregunta, nuevas_preguntas = seleccionar_pregunta_por_categoria(preguntas_restantes, categoria_aleatoria, dificultad)

        if pregunta:
            jugador = realizar_turno(jugador, pregunta, tiempo_max)
        else:
            mostrar_un_mensaje(f"❌ No hay preguntas disponibles en la categoría {categoria_aleatoria}")

        preguntas_restantes = nuevas_preguntas
    
    verificar_vidas(jugador)

    jugador = calcular_estadisticas(jugador,limite_preguntas)
    return jugador

###############################################################################################################################################

def dividir_preguntas(preguntas: list) -> tuple:
    random.shuffle(preguntas)
    mitad = len(preguntas) // 2
    preguntas_jugador_1 = preguntas[:mitad]
    preguntas_jugador_2 = preguntas[mitad:]
    return preguntas_jugador_1, preguntas_jugador_2


def iniciar_juego_individual(nombre: str, preguntas: list, configuracion: dict, dificultad: str) -> dict:
    mostrar_un_mensaje(f"🕹️ Turno del jugador {nombre}")
    jugador = jugar(preguntas, configuracion, dificultad)
    guardar_estadisticas(r"estadisticas.csv", nombre, jugador)
    return jugador

def jugar_preguntas_y_respuestas():
    mostrar_inicio()
    nombre_jugador_1 = ingresar_nombre_jugador()
    nombre_jugador_2 = ingresar_nombre_jugador()
    preguntas = leer_preguntas_csv(r"preguntas.csv")
    configuracion = leer_configuracion(r"config.json")
    dificultad = obtener_dificultad()
    
    preguntas_jugador_1, preguntas_jugador_2 = dividir_preguntas(preguntas)
    
    jugador_1 = iniciar_juego_individual(nombre_jugador_1, preguntas_jugador_1, configuracion, dificultad)
    pausar_y_limpiar("🔄 Presione ENTER para continuar con el segundo jugador...")
    jugador_2 = iniciar_juego_individual(nombre_jugador_2, preguntas_jugador_2, configuracion, dificultad)
    
    mostrar_resultado_final(nombre_jugador_1, jugador_1, nombre_jugador_2, jugador_2)
    