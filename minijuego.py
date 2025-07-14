from funciones_mostrar import mostrar_un_mensaje
from ingresos import ingresar_nombre_jugador
from recorrido import verificar_victoria

def crear_matriz(filas, columnas, valor_inicial):
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def imprimir_tablero(tablero):
    mostrar_un_mensaje("\n   0   1   2")
    mostrar_un_mensaje("  -----------")
    for i in range(3):
        linea = f"{i}|"
        for j in range(3):
            linea += f" {tablero[i][j]} |"
        mostrar_un_mensaje(linea)
        mostrar_un_mensaje("  -----------")

def pedir_entero(texto: str) -> int:
    numero_valido = False
    while not numero_valido:
        entrada = input(texto)
        if entrada != "":
            if entrada >= "0" and entrada <= "9":
                numero_valido = True
                numero = int(entrada)  
    return numero

def pedir_posicion(tablero, jugador, nombre):
    mostrar_un_mensaje(f"\n🎮 Turno de {nombre} ({jugador})")
    fila = pedir_entero("Fila (0-2): ")
    columna = pedir_entero("Columna (0-2): ")

    fuera_de_rango = fila < 0 or fila > 2 or columna < 0 or columna > 2
    casilla_ocupada = not fuera_de_rango and tablero[fila][columna] != " "

    if fuera_de_rango:
        mostrar_un_mensaje("❌ Fuera del tablero.")
        posicion = pedir_posicion(tablero, jugador, nombre)
    elif casilla_ocupada:
        mostrar_un_mensaje("❌ Casilla ocupada.")
        posicion = pedir_posicion(tablero, jugador, nombre)
    else:
        posicion = fila, columna
    return posicion

def movimientos_disponibles(tablero):
    disponibles = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                disponibles += [[i, j]]
    return disponibles

def swap(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def ordenar_movimientos(movs, i=0):
    if i == len(movs) - 1:
        return movs
    j = i + 1
    while j < len(movs):
        if movs[i][0] > movs[j][0]:
            swap(movs, i, j)
        elif movs[i][0] == movs[j][0] and movs[i][1] > movs[j][1]:
            swap(movs, i, j)
        j += 1
    return ordenar_movimientos(movs, i + 1)


def mostrar_resultado(tablero, ganador, nombre_x, nombre_o):
    imprimir_tablero(tablero)
    if ganador is not None:
        nombre = nombre_x if ganador == "X" else nombre_o
        mostrar_un_mensaje(f"\n🏆 ¡Ganó {nombre}! ({ganador})")
    else:
        mostrar_un_mensaje("\n🤝 ¡Empate! ")

def asignar_nombre(jugador, nombre_x, nombre_o):
    if jugador == "X":
        nombre = nombre_x
    else:
        nombre = nombre_o
    return nombre

def cambiar_jugador(jugador):
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"
    return jugador
        
def mosrar_movimientos_disponibles(tablero,disponibles):
    for mov in disponibles:
        mostrar_un_mensaje(f"[{mov[0]}, {mov[1]}]")
        
def juego():
    nombre_x = ingresar_nombre_jugador()
    nombre_o = ingresar_nombre_jugador()
    tablero = crear_matriz(3, 3, " ")
    jugador = "X"
    turnos = 0
    ganador = None

    while turnos < 9 and ganador is None:
        imprimir_tablero(tablero)
        mostrar_un_mensaje("📍 Movimientos disponibles:")
        disponibles = ordenar_movimientos(movimientos_disponibles(tablero))
        mosrar_movimientos_disponibles(tablero, disponibles)
        
        nombre = asignar_nombre(jugador, nombre_x, nombre_o)
        fila, columna = pedir_posicion(tablero, jugador, nombre)
        tablero[fila][columna] = jugador

        if verificar_victoria(len(tablero),tablero, jugador):
            ganador = jugador
            
        jugador = cambiar_jugador(jugador)
        turnos += 1

    mostrar_resultado(tablero, ganador, nombre_x, nombre_o)
