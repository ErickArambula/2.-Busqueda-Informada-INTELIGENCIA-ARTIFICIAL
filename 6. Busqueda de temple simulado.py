import random
import math

def funcion_objetivo(solucion):
    # Esta es la función objetivo que queremos maximizar o minimizar. Personalízala según tus necesidades.
    return sum(solucion)

def generar_solucion_inicial(n):
    # Genera una solución inicial aleatoria de n elementos.
    return [random.randint(0, 1) for _ in range(n)]

def vecino_aleatorio(solucion):
    # Genera una solución vecina al cambiar un elemento de la solución actual de forma aleatoria.
    vecino = solucion[:]
    i = random.randint(0, len(solucion) - 1)
    vecino[i] = 1 - vecino[i]  # Cambiar de 0 a 1 o de 1 a 0.
    return vecino

def temple_simulado(n, temperatura_inicial, factor_enfriamiento, max_iter):
    solucion_actual = generar_solucion_inicial(n)
    valor_actual = funcion_objetivo(solucion_actual)
    mejor_solucion = solucion_actual
    mejor_valor = valor_actual

    for i in range(max_iter):
        temperatura = temperatura_inicial / (1 + i)  # Enfriamiento lineal.

        vecino = vecino_aleatorio(solucion_actual)
        valor_vecino = funcion_objetivo(vecino)

        if valor_vecino > valor_actual or random.random() < math.exp((valor_vecino - valor_actual) / temperatura):
            solucion_actual = vecino
            valor_actual = valor_vecino

        if valor_actual > mejor_valor:
            mejor_solucion = solucion_actual
            mejor_valor = valor_actual

    return mejor_solucion, mejor_valor

# Ejemplo de uso:
random.seed(42)  # Fijar la semilla para reproducibilidad.

n = 10  # Número de elementos en la solución.
temperatura_inicial = 10.0  # Temperatura inicial.
factor_enfriamiento = 0.9  # Factor de enfriamiento.
max_iter = 1000  # Número máximo de iteraciones.

mejor_solucion, mejor_valor = temple_simulado(n, temperatura_inicial, factor_enfriamiento, max_iter)
print(f"Mejor solución encontrada: {mejor_solucion}")
print(f"Mejor valor de la función objetivo: {mejor_valor}")
