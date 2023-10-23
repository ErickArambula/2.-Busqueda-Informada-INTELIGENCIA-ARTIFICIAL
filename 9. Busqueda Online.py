import random

# Función que simula la generación de un nuevo estado en un entorno en línea.
def generar_estado_aleatorio():
    return random.randint(1, 100)

# Función objetivo que define el objetivo que queremos encontrar.
def funcion_objetivo(estado):
    return estado == 42  # Buscamos el estado 42 como objetivo.

# Búsqueda en línea.
def busqueda_en_linea():
    intentos = 0
    estado_actual = generar_estado_aleatorio()

    while not funcion_objetivo(estado_actual):
        intentos += 1
        estado_actual = generar_estado_aleatorio()

    return estado_actual, intentos

# Ejemplo de uso:
random.seed(42)  # Fijar la semilla para reproducibilidad.

resultado, intentos = busqueda_en_linea()
print(f"Resultado encontrado: {resultado}")
print(f"Intentos necesarios: {intentos}")

