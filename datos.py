import re
def leer_preguntas_csv(path:str) -> list:
    try:
        lista = []
        with open(path, "r", encoding="UTF8") as archivo:
            archivo.readline()
            for line in archivo:
                lectura = re.split(",|\n", line)
                pregunta = {}
                pregunta["categoria"] = lectura[0]
                pregunta["dificultad"] = lectura[1]
                pregunta["pregunta"] = lectura[2]
                pregunta["opciones"] = {
                    "A": lectura[3],
                    "B": lectura[4],
                    "C": lectura[5]
                }
                pregunta["respuesta_correcta"] = lectura[6]
                pregunta["puntos"] = int(lectura[7])
                lista.append(pregunta)
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo de preguntas en: {path}")
    return lista
