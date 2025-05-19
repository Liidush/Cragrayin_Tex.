import matplotlib.pyplot as plt
import networkx as nx


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cameras = 0
        self.node_status = {}

    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 1

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                self.cameras += 1
                self.node_status[node] = "Camera"
                return 2

            if left == 2 or right == 2:
                self.node_status[node] = "Root"
                return 1

            self.node_status[node] = "Node"
            return 0

        if dfs(root) == 0:
            self.cameras += 1
            self.node_status[root] = "Camera"

        self.draw_tree(root)
        return self.cameras

    def draw_tree(self, root):
        """Պատկերում է ծառը `networkx`-ի միջոցով"""
        G = nx.DiGraph()
        pos = {}
        labels = {}

        def build_graph(node, x=0, y=0, level=1):
            """Կառուցում է ծառի գրաֆը"""
            if node:
                G.add_node(node)
                pos[node] = (x, -y)
                labels[node] = self.node_status.get(node, "X")

                if node.left:
                    G.add_edge(node, node.left)
                    build_graph(node.left, x - 2.0 / (level + 1), y + 1, level + 1)

                if node.right:
                    G.add_edge(node, node.right)
                    build_graph(node.right, x + 2.0 / (level + 1), y + 1, level + 1)

        build_graph(root)

        plt.figure(figsize=(8, 5))
        nx.draw(
            G,
            pos,
            with_labels=False,
            node_size=2000,
            node_color="lightblue",
            edge_color="gray",
        )
        nx.draw_networkx_labels(G, pos, labels, font_size=12, font_color="black")

        plt.title("Տեսախցիկներով ծառ")
        plt.show()


root = TreeNode(0)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(0)
root.left.left.right = TreeNode(0)

sol = Solution()
print("📷 Պահանջվող տեսախցիկների քանակը:", sol.minCameraCover(root))
print("B-C")
