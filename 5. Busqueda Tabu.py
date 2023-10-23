import random

def funcion_objetivo(solucion):
    # Esta es la función objetivo que queremos maximizar o minimizar. Personalízala según tus necesidades.
    return sum(solucion)

def generar_solucion_inicial(n):
    # Genera una solución inicial aleatoria de n elementos.
    return [random.randint(0, 1) for _ in range(n)]

def vecindario(solucion):
    # Genera soluciones vecinas al cambiar un elemento de la solución actual.
    vecinos = []
    for i in range(len(solucion)):
        vecino = solucion[:]
        vecino[i] = 1 - vecino[i]  # Cambiar de 0 a 1 o de 1 a 0.
        vecinos.append(vecino)
    return vecinos

def busqueda_tabu(n, max_iter):
    mejor_solucion = generar_solucion_inicial(n)
    mejor_valor = funcion_objetivo(mejor_solucion)
    solucion_actual = mejor_solucion
    valor_actual = mejor_valor
    lista_tabu = []

    for _ in range(max_iter):
        vecinos = vecindario(solucion_actual)
        mejor_vecino = None
        mejor_valor_vecino = float('-inf')

        for vecino in vecinos:
            valor_vecino = funcion_objetivo(vecino)

            if valor_vecino > mejor_valor_vecino and vecino not in lista_tabu:
                mejor_vecino = vecino
                mejor_valor_vecino = valor_vecino

        if mejor_vecino is not None:
            solucion_actual = mejor_vecino
            valor_actual = mejor_valor_vecino

            if valor_actual > mejor_valor:
                mejor_solucion = solucion_actual
                mejor_valor = valor_actual

            lista_tabu.append(solucion_actual)

            if len(lista_tabu) > 10:  # Longitud máxima de la lista tabú.
                lista_tabu.pop(0)

    return mejor_solucion, mejor_valor

# Ejemplo de uso:
random.seed(42)  # Fijar la semilla para reproducibilidad.

n = 10  # Número de elementos en la solución.
max_iter = 100  # Número máximo de iteraciones.

mejor_solucion, mejor_valor = busqueda_tabu(n, max_iter)
print(f"Mejor solución encontrada: {mejor_solucion}")
print(f"Mejor valor de la función objetivo: {mejor_valor}")
