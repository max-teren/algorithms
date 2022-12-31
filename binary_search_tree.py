class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


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
                return sub_root.value

        return find_tree(self.root, key)


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
    print(index.find("R"))
