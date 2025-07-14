def listar_categoria(preguntas: list) -> list:
    categorias = set()
    for pregunta in preguntas:
        categorias.add(pregunta["categoria"])
    return list(categorias)

def seleccionar_pregunta_por_categoria(preguntas_restantes: list, categoria_elegida: str, dificultad:str) -> dict:
    pregunta_seleccionada = None
    nuevas_preguntas = []

    for pregunta in preguntas_restantes:
        if not pregunta_seleccionada and pregunta["categoria"].strip().lower() == categoria_elegida and pregunta["dificultad"].strip().lower() == dificultad.strip().lower():
            pregunta_seleccionada = pregunta
        else:
            nuevas_preguntas.append(pregunta)
            
    return pregunta_seleccionada, nuevas_preguntas