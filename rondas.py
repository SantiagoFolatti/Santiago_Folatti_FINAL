import time
from ingresos import leer_respuesta

def verificar_respuesta(pregunta: dict,respuesta: str) -> bool:
    return respuesta == pregunta["respuesta_correcta"]

def calcular_tiempo_respuesta(funcion_entrada) -> (str | float):
    inicio = time.time()
    respuesta = funcion_entrada()
    fin = time.time()
    tiempo_utilizado = fin - inicio
    return respuesta, tiempo_utilizado

def jugar_ronda(pregunta: dict, tiempo_max: int):
    respuesta_usuario, tiempo_usado = calcular_tiempo_respuesta(leer_respuesta)
    resultado = evaluar_respuesta(pregunta, respuesta_usuario, tiempo_usado, tiempo_max)
    resultado["respuesta"] = respuesta_usuario
    resultado["tiempo_usado"] = tiempo_usado
    return resultado

def evaluar_respuesta(pregunta: dict, respuesta_usuario: str, tiempo_usado: float, tiempo_max: int) -> dict:
    resultado = {"puntos_obtenidos": 0, "respondida": False, "estado": ""}
    if tiempo_usado <= tiempo_max:
        resultado["respondida"] = True
        if verificar_respuesta(pregunta, respuesta_usuario):
            resultado["puntos_obtenidos"] = pregunta["puntos"]
            resultado["estado"] = "correcto"
        else:
            resultado["estado"] = "incorrecto"
    else:
        resultado["estado"] = "tiempo_agotado"
    return resultado