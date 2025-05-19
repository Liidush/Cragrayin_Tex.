import heapq


def dijkstra(graph, start):
    dist = {v: float("inf") for v in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, weight in graph[u].items():
            if d + weight < dist[v]:
                dist[v] = d + weight
                heapq.heappush(pq, (dist[v], v))

    return dist


graph = {
    "A": {"B": 5, "D": 12, "G": 25},
    "B": {"D": 8},
    "D": {"C": 2},
    "C": {"E": 4, "G": 10, "F": 5},
    "E": {"G": 5},
    "F": {"G": 10},
    "G": {},
}

distances = dijkstra(graph, "A")
print("Shortest distance from A to G:", distances["G"])
