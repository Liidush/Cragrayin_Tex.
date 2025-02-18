class UndirectedGraph:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(f"Vertex {vertex}: {edges}")


def validate_handshake_lemma(degrees):
    return sum(1 for degree in degrees if degree % 2 != 0) % 2 == 0


def main():
    vertices = 30
    degrees = [0] * vertices
    graph = UndirectedGraph(vertices)

    for i, edge_count in zip(range(30), [3] * 9 + [4] * 11 + [5] * 10):
        for j in range(1, edge_count + 1):
            graph.add_edge(i, (i + j) % vertices)
            degrees[i] += 1
            degrees[(i + j) % vertices] += 1

    graph.print_graph()
    for i, degree in enumerate(degrees):
        print(f"Vertex {i} has degree {degree}")

    print(f"Total degree of the graph: {sum(degrees)}")

    if validate_handshake_lemma(degrees):
        print("The graph satisfies the handshake lemma.")
    else:
        print("Such a graph is impossible according to the handshake lemma.")


if __name__ == "__main__":
    main()
