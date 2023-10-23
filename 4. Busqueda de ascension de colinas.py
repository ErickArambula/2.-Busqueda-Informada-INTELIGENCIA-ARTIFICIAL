import random

def funcion_objetivo(x):
    # Esta es la función que queremos maximizar. Puedes personalizarla según tus necesidades.
    return -x ** 2  # En este ejemplo, estamos buscando el máximo de -x^2, por lo que utilizamos un signo negativo.

def busqueda_ascenso_de_colinas(funcion_objetivo, valor_inicial, paso, max_iter):
    x = valor_inicial
    mejor_x = x

    for _ in range(max_iter):
        vecinos = [x + paso, x - paso]  # Generar vecinos cercanos.

        # Elegir el vecino con el mejor valor de la función objetivo.
        mejor_vecino = max(vecinos, key=funcion_objetivo)

        if funcion_objetivo(mejor_vecino) > funcion_objetivo(x):
            x = mejor_vecino  # Moverse al mejor vecino si mejora la función objetivo.
            if funcion_objetivo(x) > funcion_objetivo(mejor_x):
                mejor_x = x  # Actualizar el mejor valor si es mejor que el anterior.

    return mejor_x

# Ejemplo de uso:
random.seed(42)  # Fijar la semilla para reproducibilidad.

valor_inicial = random.uniform(-10, 10)  # Valor inicial aleatorio en el rango [-10, 10].
paso = 0.1  # Tamaño del paso.
max_iter = 100  # Número máximo de iteraciones.

resultado = busqueda_ascenso_de_colinas(funcion_objetivo, valor_inicial, paso, max_iter)
print(f"El máximo local encontrado es {funcion_objetivo(resultado)} en x = {resultado}")
