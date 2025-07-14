def obtener_dificultad() -> str:
    dificultad = input("Ingrese la dificultad (Facil, Media, Difcil): ").strip().capitalize()
    while dificultad != "Facil" and dificultad != "Media" and dificultad != "Dificil":
        dificultad = input("Dificultad invalida, ingrese (Facil, Media, Dificil): ").strip().capitalize()
    return dificultad
    
def leer_respuesta():
    respuesta = input("Ingrese su respuesta [A,B,C]: ").upper()
    while respuesta != "A" and respuesta != "B" and respuesta != "C":
        respuesta = input("Elija una opcion correcta [A,B,C]: ").upper()
    return respuesta

def ingresar_nombre_jugador() -> str:
    nombre_jugador = input("\nIngrese su nombre de usuario: ").strip()
    return nombre_jugador

def pedir_numero(mensaje: str, valor_actual: int) -> int:
    entrada = input(f"{mensaje}: ").strip()
    nuevo_valor = valor_actual
    if entrada.isdigit() and int(entrada) > 0:
        nuevo_valor = int(entrada)
    return nuevo_valor
