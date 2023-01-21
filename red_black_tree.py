from binary_search_tree import BST

BLACK = False
RED = True


class ColorNode:

    def __init__(self, key, value, color=RED):
        self.key = key
        self.value = value
        self.color = color
        self.left: ColorNode = None
        self.right: ColorNode = None

    def is_red(self):
        return self.color == RED

    def __str__(self):
        return f"key-{self.key}; value-{self.value}; color-{self.color};\n left-{self.left};\n right-{self.right}"


class RedBlackTree(BST):
    def __init__(self):
        self.root = None

    def rotate_left(self, node: ColorNode):
        assert node.right.is_red()
        new_parent = node.right
        node.right = new_parent.left
        new_parent.left = node
        new_parent.color = node.color
        new_parent.left.color = RED
        return new_parent

    def rotate_right(self, node: ColorNode):
        assert node.left.is_red()
        new_parent = node.left
        node.left = new_parent.right
        new_parent.right = node
        new_parent.color = node.color
        new_parent.right.color = RED
        return new_parent

    def recolor(self, node: ColorNode):
        # assert not node.is_red()
        assert node.left.is_red()
        assert node.right.is_red()
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK
        return node

    def insert(self, key, value):
        def put(node: ColorNode, key, value):
            if not node:
                return ColorNode(key, value)
            elif key < node.key:
                node.left = put(node.left, key, value)
            elif key > node.key:
                node.right = put(node.right, key, value)
            else:
                node.value = value
            if node.right and node.right.is_red() and (not node.left or not node.left.is_red()):
                node = self.rotate_left(node)
            if node.left and node.left.left and node.left.is_red() and node.left.left.is_red():
                node = self.rotate_right(node)
            if node.right and node.left and node.left.is_red() and node.right.is_red():
                node = self.recolor(node)
            return node

        self.root = put(self.root, key, value)


if __name__ == '__main__':
    rb_tree = RedBlackTree()
    rb_tree.insert('S', 1)
    rb_tree.insert('E', 2)
    rb_tree.insert('A', 3)
    rb_tree.insert('R', 4)
    rb_tree.insert('C', 5)
    rb_tree.insert('H', 6)
    rb_tree.insert('X', 7)
    rb_tree.insert('M', 8)
    rb_tree.insert('P', 9)
    rb_tree.insert('L', 10)
    print(rb_tree.root)
