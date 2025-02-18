class DirectedGraph:
    def __init__(self, vertices):
        self.vertices_count = vertices
        self.adj_matrix = [[0.0 for _ in range(vertices)] for _ in range(vertices)]

    def get_vertices_count(self):
        return self.vertices_count

    def get_edges_count(self):
        count = 0
        for i in range(self.vertices_count):
            for j in range(self.vertices_count):
                if self.adj_matrix[i][j] > 0:
                    count += 1
        return count

    def add_edge(self, u, v, trust):
        self.adj_matrix[u][v] = trust

    def has_edge(self, u, v):
        return self.adj_matrix[u][v] > 0

    def get_outgoing_edges_count(self, u):
        count = 0
        for i in range(self.vertices_count):
            if self.adj_matrix[u][i] > 0:
                count += 1
        return count

    def print_graph(self):
        for i in range(self.vertices_count):
            for j in range(self.vertices_count):
                if self.adj_matrix[i][j] > 0:
                    print(f"Edge from {i} to {j} with trust {self.adj_matrix[i][j]}")


def is_whole_number(s):
    return s.isdigit()


def main():
    exit_command = "exit"
    trust_value = 1.0

    n = input("Enter people number: ").strip()
    while not is_whole_number(n) or int(n) == 0:
        n = input("Invalid input. Try again: ").strip()

    people = int(n)
    trust = DirectedGraph(people)

    print("Enter people trusting relationships")
    while True:
        print(f"\nRelationship {trust.get_edges_count()}")

        u = input("Enter the starting vertex: ").strip()
        if u.lower() == exit_command:
            break

        while not is_whole_number(u) or int(u) >= trust.get_vertices_count():
            u = input("Invalid vertex. Please enter a valid starting vertex: ").strip()

        v = input("Enter the ending vertex: ").strip()
        if v.lower() == exit_command:
            break

        while (
            not is_whole_number(v)
            or int(v) >= trust.get_vertices_count()
            or int(v) == int(u)
        ):
            v = input("Invalid vertex. Please enter a valid ending vertex: ").strip()

        u, v = int(u), int(v)
        if trust.has_edge(u, v):
            print("This edge already exists.\n")
            continue

        trust.add_edge(u, v, trust_value)

    trust.print_graph()

    if trust.get_edges_count() < (people - 1):
        print("\nThere's no judge.")
    else:
        judge_found = False
        for i in range(people):
            if trust.get_outgoing_edges_count(i) == 0:
                judge = i
                trusting = 0
                for j in range(people):
                    if j == judge:
                        continue
                    if not trust.has_edge(j, judge):
                        break
                    trusting += 1
                if trusting == people - 1:
                    judge_found = True
                    break

        if not judge_found:
            print("\nThere's no judge.")
        else:
            print(f"\nJudge is person with number {judge}")


if __name__ == "__main__":
    main()
