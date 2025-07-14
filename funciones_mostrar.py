from funciones_categorias import listar_categoria
import os

def mostrar_pregunta(pregunta:dict):
    print(f"\nCategoria : {pregunta["categoria"]} | Dificultad : {pregunta["dificultad"]}")
    print(f'\n{pregunta["pregunta"]}')
    for clave, valor in pregunta["opciones"].items():
        print(f"{clave} : {valor}")
        
def mostrar_estado_jugador(jugador:dict,tiempo_max: int):
    print(f"\n❤️ Vidas restantes: {jugador['vidas']}")
    print(f"⏱️ Tienes {tiempo_max} segundos para responder.")

def mostrar_estado_partida(preguntas_restantes: list, respondidas: int, limite_preguntas: int) -> list:
    categorias_disponibles = listar_categoria(preguntas_restantes)
    cantidad_preguntas_restantes = limite_preguntas - respondidas
    print(f"\n📌Preguntas restantes: {cantidad_preguntas_restantes}")
    
    return categorias_disponibles

def mostrar_resultado_respuesta(pregunta: dict, estado: str, puntos_obtenidos: int):
    if estado == "correcto":
        print("✅ Respuesta correcta!")
        print(f"📈 Sumaste {puntos_obtenidos} puntos")
    elif estado == "incorrecto":
        print(f"❌ Respuesta incorrecta. La correcta era: {pregunta['respuesta_correcta']}")
        print(f"📉 No sumaste puntos, la pregunta valía {pregunta['puntos']} puntos")
    elif estado == "tiempo_agotado":
        print("⏰ Tiempo agotado. No se suma puntaje.")


def mostrar_detalle_ronda(pregunta:dict,resultado_ronda:dict):
    print(f"\nTu respuesta: {resultado_ronda['respuesta']}")
    print(f"Tiempo utilizado: {int(resultado_ronda['tiempo_usado'])} segundos")
    mostrar_resultado_respuesta(pregunta, resultado_ronda["estado"], resultado_ronda["puntos_obtenidos"])

def mostrar_inicio():
    print("\n¡Bienvenido al juego de preguntas y respuestas!")
    print("Puedes elegir entre las siguientes categorías:")
    
    
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
    
def pausar_y_limpiar(mensaje):
    input(mensaje)
    limpiar_pantalla()
    
def mostrar_un_mensaje(mensaje:str):
    print(mensaje)
    
def mostrar_estadisticas_jugador(nombre: str, jugador: dict):
    print(f"👤 {nombre}")
    print(f"   ✅ Correctas: {jugador['respuestas_correctas']}")
    print(f"   📈 Puntaje total: {jugador['puntaje_total']}")
    print(f"   ⏱️ Tiempo total: {jugador['tiempo_total']:.2f} seg")
    print(f"   🧮 Tiempo promedio: {jugador['tiempo_promedio']:.2f} seg/pregunta")
    print(f"   🔥 Racha máxima: {jugador['racha_maxima_correctas']}")
    print("-" * 50)

def mostrar_ganador(nombre1: str, jugador1: dict, nombre2: str, jugador2: dict):
    if jugador1["puntaje_total"] > jugador2["puntaje_total"]:
        print(f"🏆 ¡Gana {nombre1} con {jugador1['puntaje_total']} puntos!")
    elif jugador2["puntaje_total"] > jugador1["puntaje_total"]:
        print(f"🏆 ¡Gana {nombre2} con {jugador2['puntaje_total']} puntos!")
    else:
        print("🤝 ¡Empate! Ambos jugadores tienen el mismo puntaje.")

def mostrar_resultado_final(nombre1: str, jugador1: dict, nombre2: str, jugador2: dict):
    print("\n📊 RESULTADO FINAL 📊")
    print("-" * 50)

    mostrar_estadisticas_jugador(nombre1, jugador1)
    mostrar_estadisticas_jugador(nombre2, jugador2)

    mostrar_ganador(nombre1, jugador1, nombre2, jugador2)