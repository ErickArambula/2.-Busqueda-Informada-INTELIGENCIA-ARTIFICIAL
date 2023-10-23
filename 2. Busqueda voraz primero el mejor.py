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

def busqueda_voraz(grafo, inicio, objetivo, heuristica):
    cola_prioridad = [(heuristica[inicio], inicio)]  # Cola de prioridad para mantener el valor heurístico y el nodo.
    visitados = set()  # Conjunto para llevar un registro de los nodos visitados.

    while cola_prioridad:
        valor_heuristico, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == objetivo:
            return visitados  # Devolver la lista de nodos visitados como resultado.

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino, costo_arista in grafo.grafo[nodo_actual]:
                if vecino not in visitados:
                    heapq.heappush(cola_prioridad, (heuristica[vecino], vecino))

    return None  # No se encontró un camino al objetivo

# Ejemplo de uso:
grafo_ejemplo = Grafo()
grafo_ejemplo.agregar_vertice('A')
grafo_ejemplo.agregar_vertice('B')
grafo_ejemplo.agregar_vertice('C')
grafo_ejemplo.agregar_vertice('D')
grafo_ejemplo.agregar_arista('A', 'B', 4)
grafo_ejemplo.agregar_arista('A', 'C', 2)
grafo_ejemplo.agregar_arista('B', 'D', 5)
grafo_ejemplo.agregar_arista('C', 'D', 1)

inicio = 'A'
objetivo = 'D'
heuristica = {'A': 7, 'B': 3, 'C': 1, 'D': 0}  # Valores heurísticos para cada nodo

resultado = busqueda_voraz(grafo_ejemplo, inicio, objetivo, heuristica)
if resultado:
    print(f"Nodos visitados en el camino de {inicio} a {objetivo}: {resultado}")
else:
    print(f"No se encontró un camino de {inicio} a {objetivo}")
