def verificar_filas(n,tablero,jugador):
    hay_victoria = False
    for i in range(n):
        fila_completa = True
        for j in range(n):
            if tablero[i][j] != jugador:
                fila_completa = False
                break
        if fila_completa:
            hay_victoria = True
    return hay_victoria

def verificar_columnas(n ,tablero,jugador):
    hay_victoria = False 
    for j in range(n):
        columna_completa = True
        for i in range(n):
            if tablero[i][j] != jugador:
                columna_completa = False
                break
        if columna_completa:
            hay_victoria = True
    return hay_victoria

def verificar_diagonal_principal(n, tablero,jugador):
    diagonal_principal = True
    for i in range(n):
        if tablero[i][i] != jugador:
            diagonal_principal = False
            break
    return diagonal_principal

def verificar_diagonal_secundaria(n,tablero,jugador):
    diagonal_secundaria = True
    for i in range(n):
        if tablero[i][n - 1 - i] != jugador:
            diagonal_secundaria = False
            break
    return diagonal_secundaria

def verificar_victoria(n, tablero, jugador):
    victoria = False
    if verificar_filas(n, tablero, jugador):
        victoria = True
    elif verificar_columnas(n, tablero, jugador):
        victoria = True
    elif verificar_diagonal_principal(n, tablero, jugador):
        victoria = True
    elif verificar_diagonal_secundaria(n, tablero, jugador):
        victoria = True
    return victoria