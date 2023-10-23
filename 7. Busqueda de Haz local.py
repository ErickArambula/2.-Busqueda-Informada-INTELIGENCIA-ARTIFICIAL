import random

def funcion_objetivo(solucion):
    # Esta es la función objetivo que queremos maximizar o minimizar. Personalízala según tus necesidades.
    return sum(solucion)

def generar_solucion_aleatoria(n):
    # Genera una solución aleatoria de n elementos.
    return [random.randint(0, 1) for _ in range(n)]

def generar_haz_inicial(k, n):
    # Genera k soluciones iniciales aleatorias.
    return [generar_solucion_aleatoria(n) for _ in range(k)]

def vecino_aleatorio(solucion):
    # Genera una solución vecina al cambiar un elemento de la solución actual de forma aleatoria.
    vecino = solucion[:]
    i = random.randint(0, len(solucion) - 1)
    vecino[i] = 1 - vecino[i]  # Cambiar de 0 a 1 o de 1 a 0.
    return vecino

def buscar_haz_local(k, n, max_iter):
    haz_actual = generar_haz_inicial(k, n)

    for _ in range(max_iter):
        vecinos = [vecino_aleatorio(solucion) for solucion in haz_actual]
        valores_vecinos = [funcion_objetivo(vecino) for vecino in vecinos]

        mejores_indices = sorted(range(len(valores_vecinos)), key=lambda i: valores_vecinos[i], reverse=True)[:k]
        haz_actual = [vecinos[i] for i in mejores_indices]

    mejor_solucion = max(haz_actual, key=funcion_objetivo)
    mejor_valor = funcion_objetivo(mejor_solucion)

    return mejor_solucion, mejor_valor

# Ejemplo de uso:
random.seed(42)  # Fijar la semilla para reproducibilidad.

n = 10  # Número de elementos en la solución.
k = 5  # Tamaño del haz.
max_iter = 100  # Número máximo de iteraciones.

mejor_solucion, mejor_valor = buscar_haz_local(k, n, max_iter)
print(f"Mejor solución encontrada: {mejor_solucion}")
print(f"Mejor valor de la función objetivo: {mejor_valor}")
