import re

def guardar_estadisticas(path: str, nombre_jugador: str, jugador: dict):
    try:
        with open(path, "a", encoding="utf8") as archivo:
            linea = f"{nombre_jugador}," \
                    f"{jugador['puntaje_total']}," \
                    f"{jugador['respondidas']}," \
                    f"{jugador['porcentaje_aciertos']:.2f}," \
                    f"{jugador['promedio_puntos']:.2f}," \
                    f"{jugador['vidas']}," \
                    f"{jugador['racha_maxima_correctas']}," \
                    f"{jugador['tiempo_total']:.2f}," \
                    f"{jugador['tiempo_promedio']:.2f}\n"
            archivo.write(linea)
    except Exception as e:
        print(f"Eror al guardar estadisticas: {e}")

def leer_estadisticas(path: str) -> list:
    try:
        estadisticas = []
        with open(path, "r", encoding="utf8") as archivo:
            for line in archivo:
                lectura = re.split(",|\n", line)
                estadistica = {}
                estadistica["jugador"] = lectura[0]
                estadistica["puntaje_total"] = int(lectura[1])
                estadistica["respondidas"] = int(lectura[2])
                estadistica["porcentaje_aciertos"] = float(lectura[3])
                estadistica["promedio_puntos"] = float(lectura[4])
                estadistica["vidas"] = int(lectura[5])
                estadistica["racha_maxima_correctas"] = int(lectura[6])
                estadistica["tiempo_total"] = float(lectura[7])
                estadistica["tiempo_promedio"] = float(lectura[8])
                estadisticas.append(estadistica)
                
    except FileNotFoundError:
        print(f"No se encontró el archivo de estadísticas en: {path}")
    except Exception as e:
        print(f"Error al leer estadísticas: {e}")
    return estadisticas

def mostrar_estadisticas(estadisticas: list,mensaje:str) -> None:
    print(mensaje)
    print(f"{'Jugador':<15} {'Puntaje':>10} {'Resp.':>7} {'% Aciertos':>12} {'Prom.':>8} {'Vidas':>7} {'RachaMax':>10} {'TiempoTot':>10} {'TiempoProm':>12}")
    print("-" * 95)
    for e in estadisticas:
        print(f"{e['jugador']:<15}"
            f"{e['puntaje_total']:>10}"
            f"{e['respondidas']:>7}"
            f"{e['porcentaje_aciertos']:>12.2f}"
            f"{e['promedio_puntos']:>8.2f}"
            f"{e['vidas']:>7}"
            f"{e['racha_maxima_correctas']:>10}"
            f"{e['tiempo_total']:>10.2f}"
            f"{e['tiempo_promedio']:>12.2f}")
    print("-" * 95)

def swap(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def ordenar_estadisticas_por_puntaje(estadisticas: list) -> list:
    for i in range(len(estadisticas) - 1):
        for j in range(i + 1, len(estadisticas)):
            if estadisticas[i]["puntaje_total"] < estadisticas[j]["puntaje_total"]:
                swap(estadisticas, i, j)