import numpy as np


class Graph:
    def __init__(self):
        self.matrix = np.array(
            [
                ["0", "n1", "n2", "n3", "n4", "n5", "n6"],
                ["n1", "0", "10", "0", "0", "8", "5"],
                ["n2", "10", "0", "0", "20", "12", "0"],
                ["n3", "0", "0", "0", "4", "0", "0"],
                ["n4", "0", "20", "4", "0", "15", "0"],
                ["n5", "8", "12", "0", "15", "0", "7"],
                ["n6", "5", "0", "0", "0", "7", "0"],
            ]
        )

    def print_adj_matrix(self):
        print("\n".join("\t".join(row) for row in self.matrix))

    def determine_nodes(self):
        nodes = {
            i: sum(1 for j in range(1, 7) if self.matrix[i][j] != "0")
            for i in range(1, 7)
        }
        labels = {
            "E": min(nodes, key=nodes.get),
            "B": max(nodes, key=nodes.get),
            "A": [k for k, v in nodes.items() if v == 2][0],
        }
        labels["D"] = next(j for j in range(1, 7) if self.matrix[labels["E"]][j] != "0")
        labels["F"] = next(j for j in range(1, 7)if self.matrix[labels["D"]][j] != "0" and j not in labels.values())
        labels["C"] = next(i for i in range(1, 7) if i not in labels.values())

        for k, v in labels.items():
            print(f"Node {k} = {self.matrix[v][0]}")
        print(f"\nDistance between B and C: {self.matrix[labels['B']][labels['C']]}")


if __name__ == "__main__":
    g = Graph()
    g.print_adj_matrix()
    g.determine_nodes()


