import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, vertice1, vertice2, costo):
        self.grafo[vertice1].append((vertice2, costo))
        self.grafo[vertice2].append((vertice1, costo))

def a_estrella(grafo, inicio, objetivo, heuristica):
    cola_prioridad = [(0, inicio)]  # Cola de prioridad para mantener el costo acumulado y el nodo.
    costo_acumulado = {inicio: 0}  # Diccionario para mantener el costo acumulado desde el inicio.
    camino = {}  # Diccionario para registrar el camino desde el inicio.

    while cola_prioridad:
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == objetivo:
            # Reconstruir el camino desde el objetivo hasta el inicio.
            camino_recuperado = []
            while nodo_actual is not None:
                camino_recuperado.insert(0, nodo_actual)
                nodo_actual = camino.get(nodo_actual, None)
            return camino_recuperado

        for vecino, costo_arista in grafo.grafo[nodo_actual]:
            nuevo_costo = costo_acumulado[nodo_actual] + costo_arista
            if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_costo
                heuristico = nuevo_costo + heuristica[vecino]
                heapq.heappush(cola_prioridad, (heuristico, vecino))
                camino[vecino] = nodo_actual

    return None  # No se encontró un camino al objetivo

# Ejemplo de uso:
grafo_ejemplo = Grafo()
grafo_ejemplo.agregar_vertice('A')
grafo_ejemplo.agregar_vertice('B')
grafo_ejemplo.agregar_vertice('C')
grafo_ejemplo.agregar_vertice('D')
grafo_ejemplo.agregar_arista('A', 'B', 1)
grafo_ejemplo.agregar_arista('A', 'C', 3)
grafo_ejemplo.agregar_arista('B', 'D', 5)
grafo_ejemplo.agregar_arista('C', 'D', 2)

inicio = 'A'
objetivo = 'D'
heuristica = {'A': 4, 'B': 2, 'C': 3, 'D': 0}  # Valores heurísticos para cada nodo

resultado = a_estrella(grafo_ejemplo, inicio, objetivo, heuristica)
if resultado:
    print(f"Camino más corto de {inicio} a {objetivo}: {resultado}")
else:
    print(f"No se encontró un camino de {inicio} a {objetivo}")
