def inicializar_jugador(configuracion:dict) -> dict:
    jugador = {
        "puntaje_total": 0,
        "respondidas": 0,
        "respuestas_correctas" : 0,
        "porcentaje_aciertos": 0.0,
        "promedio_puntos": 0.0,
        "tiempo_total": 0.0,
        "vidas": configuracion["vidas"],
        "racha_correctas": 0,
        "racha_incorrectas": 0,
        "racha_maxima_correctas": 0,
        "multiplicador": 1,
        "tiempo_promedio": 0.0
    }
    return jugador

def actualizar_estado_correcto(jugador: dict) -> dict:
    jugador["respuestas_correctas"] += 1
    jugador["racha_correctas"] += 1
    jugador["racha_incorrectas"] = 0

    if jugador["racha_correctas"] >= 3:
        jugador["multiplicador"] = 2
    else:
        jugador["multiplicador"] = 1
        
    #esto hay que modularizarlo:
    if jugador["racha_correctas"] > jugador["racha_maxima_correctas"]:
        jugador["racha_maxima_correctas"] = jugador["racha_correctas"]
    return jugador

def actualizar_estado_incorrecto(jugador: dict) -> dict:
    jugador["vidas"] -= 1
    jugador["racha_correctas"] = 0 
    jugador["racha_incorrectas"] += 1

    if jugador["racha_incorrectas"] == 2:
        jugador["multiplicador"] = -2
    elif jugador["multiplicador"] != -2:
        jugador["multiplicador"] = 1
    return jugador


def mostrar_mensaje_bonus(jugador: dict):
    if jugador["racha_correctas"] == 3:
        print("\n🔥 Bonus activado: ¡Multiplicador x2 en la siguiente pregunta!")
    elif jugador["multiplicador"] == 2:
        print("\n🔥 ¡Mantienes el multiplicador x2!")

def mostrar_mensaje_penalizacion(jugador: dict):
    if jugador["racha_incorrectas"] == 2:
        print("\n⚠️ Penalización activada: la siguiente pregunta resta doble si fallas.")
    elif jugador["multiplicador"] == -2:
        print("\n⚠️ ¡Penalización aún activa!")


def aplicar_multiplicador(puntos: int, estado:str, multiplicador:int) -> int:
    puntos_finales = 0
    if estado == "correcto":
        puntos_finales = multiplicar_correcto(puntos,estado,multiplicador)
    elif estado == "incorrecto" or estado == "tiempo_agotado":
        puntos_finales = multiplicar_incorrecto(puntos,estado,multiplicador)
    return puntos_finales

def multiplicar_correcto(puntos: int, estado:str, multiplicador:int) -> int:
    puntos_finales = 0
    if estado == "correcto":
        if multiplicador > 1:
            puntos_finales = puntos * multiplicador
        else:
            puntos_finales = puntos
    return puntos_finales

def multiplicar_incorrecto(puntos: int, estado:str, multiplicador:int) -> int:
    puntos_finales = 0
    if estado == "incorrecto" or estado == "tiempo_agotado":
        if multiplicador < 0:
            puntos_finales = puntos * multiplicador
    return puntos_finales

def procesar_estado_mensaje(jugador: dict, estado: str) -> dict:
    if estado == "correcto":
        jugador = actualizar_estado_correcto(jugador)
        mostrar_mensaje_bonus(jugador)
    elif estado == "incorrecto" or estado == "tiempo_agotado":
        jugador = actualizar_estado_incorrecto(jugador)
        mostrar_mensaje_penalizacion(jugador)
    return jugador


