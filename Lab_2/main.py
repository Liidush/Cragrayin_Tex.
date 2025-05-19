# Red-Black Tree implementation in Python with insert, delete, select (k-th smallest), and findOverlapping

class Color:
    RED = 0
    BLACK = 1

class Node:
    def __init__(self, start, end=None, color=Color.RED, parent=None):
        self.start = start
        self.end = end if end is not None else start
        self.color = color
        self.left = None
        self.right = None
        self.parent = parent
        self.size = 1  # for order-statistics
        self.max_end = self.end  # for interval overlapping

class RBTree:
    def __init__(self):
        self.NIL = Node(0, 0, color=Color.BLACK)
        self.NIL.size = 0
        self.NIL.max_end = float('-inf')
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        self.update_size(x)
        self.update_size(y)
        self.update_max_end(x)
        self.update_max_end(y)

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
        self.update_size(y)
        self.update_size(x)
        self.update_max_end(y)
        self.update_max_end(x)

    def update_size(self, node):
        if node == self.NIL:
            return
        node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)

    def update_max_end(self, node):
        if node == self.NIL:
            return
        node.max_end = max(node.end, node.left.max_end if node.left else float('-inf'),
                                     node.right.max_end if node.right else float('-inf'))

    def insert(self, start, end=None):
        new_node = Node(start, end, parent=None)
        new_node.left = new_node.right = self.NIL
        new_node.max_end = new_node.end
        y = None
        x = self.root

        while x != self.NIL:
            y = x
            x.size += 1
            x.max_end = max(x.max_end, new_node.end)
            if new_node.start < x.start:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.start < y.start:
            y.left = new_node
        else:
            y.right = new_node

        new_node.color = Color.RED
        self.fix_insert(new_node)

    def fix_insert(self, z):
        while z.parent and z.parent.color == Color.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.left_rotate(z.parent.parent)
        self.root.color = Color.BLACK

    def inorder(self, node=None, res=None):
        if res is None:
            res = []
        if node is None:
            node = self.root
        if node != self.NIL:
            self.inorder(node.left, res)
            res.append((node.start, node.end))
            self.inorder(node.right, res)
        return res

    def select(self, k):
        def _select(node, k):
            if node == self.NIL:
                return None
            left_size = node.left.size
            if k == left_size + 1:
                return node
            elif k <= left_size:
                return _select(node.left, k)
            else:
                return _select(node.right, k - left_size - 1)
        result = _select(self.root, k)
        return (result.start, result.end) if result else None

    def find_overlapping(self, start, end):
        result = []

        def _overlap(a_start, a_end, b_start, b_end):
            return a_start <= b_end and b_start <= a_end

        def _search(node):
            if node == self.NIL:
                return
            if _overlap(node.start, node.end, start, end):
                result.append((node.start, node.end))
            if node.left != self.NIL and node.left.max_end >= start:
                _search(node.left)
            if node.right != self.NIL and node.start <= end:
                _search(node.right)

        _search(self.root)
        return result

# Usage Example
rb = RBTree()
intervals = [(20, 30), (10, 15), (25, 35), (12, 20), (5, 8), (17, 19)]
for start, end in intervals:
    rb.insert(start, end)

inorder_result = rb.inorder()
kth_smallest = rb.select(3)
overlapping = rb.find_overlapping(13, 26)

inorder_result, kth_smallest, overlapping

