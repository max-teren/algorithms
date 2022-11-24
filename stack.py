class Stack:
    def push(self, item: str):
        pass

    def pop(self) -> str:
        pass

    def is_empty(self) -> bool:
        pass


class ListStack(Stack):
    class Node:
        def __init__(self):
            self.item = None
            self.next = None

    def __init__(self):
        self.data = ListStack.Node()
        self.size = 0

    def push(self, item: str):
        new_node = ListStack.Node()
        new_node.item = item
        new_node.next = self.data
        self.data = new_node
        self.size += 1

    def pop(self) -> str:
        result = self.data.item
        self.data = self.data.next
        self.size -= 1
        return result

    def is_empty(self) -> bool:
        return self.data.item is None

    def print_node(self, node: Node):
        if node.item:
            print(f"Stack {node.item}")
            self.print_node(node.next)


class ArrayStack(Stack):
    def __init__(self):
        self.data = [None] * 2
        self.size = 0

    def push(self, item: str):
        if self.size == len(self.data):
            print("Scale up array")
            bigger_arr = [None] * self.size * 2
            for i in range(0, self.size):
                bigger_arr[i] = self.data[i]
            self.data = bigger_arr
        self.data[self.size] = item
        self.size += 1

    def pop(self) -> str:
        if self.size <= len(self.data) / 4:
            print("Scale down array")
            smaller_array = [None] * len(self.data) / 2
            for i in range(0, self.size):
                smaller_array[i] = self.data[i]
            self.data = smaller_array
        result = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return result

    def is_empty(self) -> bool:
        return self.size == 0
