class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def sum_values(self):
        return self._sum_values(self.root)

    def _sum_values(self, node):
        if node is None:
            return 0
        return node.val + self._sum_values(node.left) + self._sum_values(node.right)

# Example Usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)

    total_sum = bst.sum_values()
    print(f"Сума всіх значень у дереві: {total_sum}")

    bst_empty = BinarySearchTree()
    total_sum_empty = bst_empty.sum_values()
    print(f"Сума всіх значень у порожньому дереві: {total_sum_empty}")
