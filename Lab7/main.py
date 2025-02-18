class Graph:
    def __init__(self, vertical, horizontal):
        self.v, self.h = vertical, horizontal
        self.edges = []
        self.parent = []
        self.size = []
        for i in range(self.v + 1):
            for j in range(self.h + 1):
                node = i * (self.h + 1) + j
                if j + 1 <= self.h:
                    self.edges.append((node, node + 1))
                if i + 1 <= self.v:
                    self.edges.append((node, node + self.h + 1))

    def init_union_find(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

    def greedy_removal(self):
        n = (self.v + 1) * (self.h + 1)
        self.init_union_find(n)
        removed = 0
        for u, v in sorted(self.edges):
            if self.find(u) != self.find(v):
                self.unite(u, v)
                removed += 1
        return removed


if __name__ == "__main__":
    vertical, horizontal = 50, 600
    graph = Graph(vertical, horizontal)
    total_edges = (vertical + 1) * horizontal + (horizontal + 1) * vertical
    removable_edges = total_edges - graph.greedy_removal()
    print(
        f"The maximum number of edges that can be removed without disconnecting the graph: {removable_edges}"
    )
