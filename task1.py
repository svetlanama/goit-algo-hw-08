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

    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root)

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.val

# Example Usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)

    min_value = bst.find_min()
    if min_value is not None:
        print(f"Найменше значення у дереві: {min_value}")
    else:
        print("Дерево порожнє.")

    bst_empty = BinarySearchTree()
    min_value_empty = bst_empty.find_min()
    if min_value_empty is not None:
        print(f"Найменше значення у порожньому дереві: {min_value_empty}")
    else:
        print("Порожнє дерево. Очікувано.")
