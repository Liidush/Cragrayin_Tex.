import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def draw_graph(graph, exclude=-1):
    G = nx.Graph()
    for u, neighbors in enumerate(graph):
        if u != exclude:
            G.add_edges_from((u, v) for v in neighbors if v != exclude)
    nx.draw(G, with_labels=True, node_color="lightblue", node_size=1000, font_size=10)
    plt.title(f"Graph (excluding city {exclude})" if exclude != -1 else "Initial Graph")
    plt.show()


def is_connected(graph, n, exclude):
    visited = set()
    start = next((i for i in range(n) if i != exclude), None)
    if start is None:
        return True
    q = deque([start])
    while q:
        node = q.popleft()
        visited.add(node)
        q.extend(v for v in graph[node] if v != exclude and v not in visited)
    return len(visited) == n - 1


def main():
    n, m = map(int, input("Enter number of cities and roads: ").split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    draw_graph(graph)

    if not is_connected(graph, n, exclude=-1):
        false = False
        print(false)

    for i in range(n):
        if is_connected(graph, n, i):
            draw_graph(graph, exclude=i)
            return
    print("No single city can be removed to keep the graph connected.")


if __name__ == "__main__":
    main()
