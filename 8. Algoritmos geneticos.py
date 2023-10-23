import random

# Función Objetivo: En este ejemplo, intentaremos maximizar la suma de los elementos de una lista.
def funcion_objetivo(solucion):
    return sum(solucion)

# Creación de una población inicial de soluciones aleatorias.
def generar_poblacion_inicial(poblacion_size, solucion_size):
    poblacion = []
    for _ in range(poblacion_size):
        solucion = [random.randint(0, 1) for _ in range(solucion_size)]
        poblacion.append(solucion)
    return poblacion

# Selección de padres para la reproducción.
def seleccionar_padres(poblacion, num_padres):
    padres = []
    poblacion_copia = list(poblacion)
    for _ in range(num_padres):
        indice = random.randint(0, len(poblacion_copia) - 1)
        padres.append(poblacion_copia.pop(indice))
    return padres

# Cruce (reproducción) de dos soluciones para crear una descendencia.
def cruzar(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)
    descendencia = padre1[:punto_cruce] + padre2[punto_cruce:]
    return descendencia

# Mutación de una solución.
def mutar(solucion, probabilidad_mutacion):
    for i in range(len(solucion)):
        if random.random() < probabilidad_mutacion:
            solucion[i] = 1 - solucion[i]  # Cambiar de 0 a 1 o de 1 a 0.
    return solucion

# Algoritmo Genético
def algoritmo_genetico(poblacion_size, solucion_size, num_generaciones, probabilidad_mutacion):
    poblacion = generar_poblacion_inicial(poblacion_size, solucion_size)
    for generacion in range(num_generaciones):
        poblacion = sorted(poblacion, key=funcion_objetivo, reverse=True)
        padres = seleccionar_padres(poblacion, poblacion_size // 2)
        descendientes = []
        while len(descendientes) < poblacion_size:
            padre1, padre2 = random.sample(padres, 2)
            descendiente = cruzar(padre1, padre2)
            descendiente = mutar(descendiente, probabilidad_mutacion)
            descendientes.append(descendiente)
        poblacion = descendientes

    mejor_solucion = max(poblacion, key=funcion_objetivo)
    mejor_valor = funcion_objetivo(mejor_solucion)
    return mejor_solucion, mejor_valor

# Ejemplo de uso:
random.seed(42)  # Fijar la semilla para reproducibilidad.

poblacion_size = 50
solucion_size = 10
num_generaciones = 100
probabilidad_mutacion = 0.1

mejor_solucion, mejor_valor = algoritmo_genetico(poblacion_size, solucion_size, num_generaciones, probabilidad_mutacion)
print(f"Mejor solución encontrada: {mejor_solucion}")
print(f"Mejor valor de la función objetivo: {mejor_valor}")
