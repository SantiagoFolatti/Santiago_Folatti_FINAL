import json
from ingresos import pedir_numero
def leer_configuracion(path: str) -> dict:
    try:
        with open(path, 'r') as archivo:
            configuracion = json.load(archivo)
    except FileNotFoundError:
        print(f"No se encontro el archivo de configuracion en: {path}")
    except json.JSONDecodeError:
        print(f"Error al leer el archivo Json de configuracion")
    return configuracion

def mostrar_configuracion(config:dict):
    print("\nCONFIGURACIÓN ACTUAL:")
    print(f"1️⃣  Cantidad de preguntas: {config['cantidad_preguntas']}")
    print(f"2️⃣  Tiempo por pregunta (segundos): {config['tiempo_por_pregunta']}")
    print(f"3️⃣  Vidas por jugador: {config['vidas']}")
    

def pedir_nueva_configuracion(config: dict) -> dict:
    print("\n🛠️ Configurar nueva partida (ENTER para mantener valores actuales)\n")

    config["cantidad_preguntas"] = pedir_numero("Cantidad de preguntas", config["cantidad_preguntas"])
    config["tiempo_por_pregunta"] = pedir_numero("Tiempo por pregunta en segundos", config["tiempo_por_pregunta"])
    config["vidas"] = pedir_numero("Vidas por jugador", config["vidas"])

    return config

def guardar_configuracion(path: str, config: dict):
    try:
        with open(path, 'w') as archivo:
            json.dump(config, archivo, indent=4)
    except Exception as e:
        print(f"❌ Error al guardar la configuración: {e}")
        

def cambiar_configuracion(path: str):
    config = leer_configuracion(path)
    mostrar_configuracion(config)
    config = pedir_nueva_configuracion(config)
    guardar_configuracion(path, config)
