class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

    def __str__(self):
        return f"key-{self.key}; value-{self.value}; size-{self.count}; left-{self.left}; right-{self.right}"


class BST:
    root = None

    def insert(self, key, value):
        def insert_tree(sub_root: Node, key, value):
            if not sub_root or not sub_root.key:
                return Node(key, value)
            elif sub_root.key > key:
                sub_root.left = insert_tree(sub_root.left, key, value)
            elif sub_root.key < key:
                sub_root.right = insert_tree(sub_root.right, key, value)
            else:
                sub_root.value = value
            sub_root.count = 1 + self.size_tree(sub_root.left) + self.size_tree(sub_root.right)
            return sub_root

        self.root = insert_tree(self.root, key, value)

    def find(self, key):
        def find_tree(sub_root: Node, key):
            if not sub_root.key:
                return None
            elif sub_root.key > key:
                return find_tree(sub_root.left, key)
            elif sub_root.key < key:
                return find_tree(sub_root.right, key)
            else:
                return sub_root

        return find_tree(self.root, key)

    def floor(self, key):
        def find_floor_tree(sub_root: Node, key):  # Biggest left tree element
            if sub_root and key == sub_root.key:
                return sub_root.value
            elif sub_root and key < sub_root.key:
                return find_floor_tree(sub_root.left, key)
            elif sub_root and key > sub_root.key:
                right_floor = find_floor_tree(sub_root.right, key)
                if right_floor:
                    return right_floor
                else:
                    return sub_root.value
            else:
                return None

        return find_floor_tree(self.root, key)

    def ceiling(self, key):
        def find_ceiling_tree(sub_root: Node, key):  # Smallest right tree element
            if sub_root and key == sub_root.key:
                return sub_root.value
            elif sub_root and key > sub_root.key:
                return find_ceiling_tree(sub_root.right, key)
            elif sub_root and key < sub_root.key:
                left_ceiling = find_ceiling_tree(sub_root.left, key)
                if left_ceiling:
                    return left_ceiling
                else:
                    return sub_root.value
            else:
                return None

        return find_ceiling_tree(self.root, key)

    def size(self):
        return self.size_tree(self.root)

    def size_tree(self, node: Node):
        if not node:
            return 0
        else:
            return node.count

    def rank(self, key):
        def find_rank_tree(node: Node, key):
            if not node:
                return 0
            elif node and node.key > key:
                return find_rank_tree(node.left, key)
            elif node and node.key < key:
                return 1 + self.size_tree(node.left) + find_rank_tree(node.right, key)
            else:
                return self.size_tree(node.left) + 1

        return find_rank_tree(self.root, key)

    def keys(self):
        keys = []

        def ordered_keys(node: Node):
            if not node:
                return
            ordered_keys(node.left)
            keys.append(node.key)
            ordered_keys(node.right)

        ordered_keys(self.root)
        return keys

    def delete_min(self):
        self.delete_min_tree(self.root)

    def delete_min_tree(self, node: Node):
        if not node.left:
            return node.right
        node.left = self.delete_min_tree(node.left)
        node.count = 1 + self.size_tree(node.left) + self.size_tree(node.right)
        return node

    def delete(self, key):
        def delete_tree(node: Node, key):
            if key == node.key:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    successor = self.get_min(node.right)
                    self.delete_min_tree(node.right)
                    successor.left = node.left
                    successor.right = node.right
                    return successor
            elif key > node.key:
                node.right = delete_tree(node.right, key)
                node.count = 1 + self.size_tree(node.left) + self.size_tree(node.right)
            elif key < node.key:
                node.left = delete_tree(node.left, key)
                node.count = 1 + self.size_tree(node.left) + self.size_tree(node.right)
            return node

        delete_tree(self.root, key)

    def get_min(self, node: Node):
        if not node.left:
            return node
        else:
            return self.get_min(node.left)


if __name__ == '__main__':
    index = BST()
    index.insert("S", 1)
    index.insert("E", 2)
    index.insert("X", 3)
    index.insert("A", 4)
    index.insert("R", 5)
    index.insert("C", 6)
    index.insert("H", 7)
    index.insert("M", 8)
    print(index.ceiling("N"))
    print(index.find("X"))
    print(index.rank("M"))
    print(index.keys())
    index.delete_min()
    print(index.keys())
    print(index.find("E"))
    index.delete("E")
    print(index.keys())
    print(index.root)
