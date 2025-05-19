from collections import defaultdict


def minTime(n, edges, hasApple):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    def dfs(node, parent):
        total_time = 0
        for child in tree[node]:
            if child == parent:
                continue
            child_time = dfs(child, node)
            if child_time > 0 or hasApple[child]:
                total_time += child_time + 2
        return total_time

    return dfs(0, -1)


test_n = 7
test_edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
test_hasApple = [False, False, True, False, True, True, False]

print(minTime(test_n, test_edges, test_hasApple))
