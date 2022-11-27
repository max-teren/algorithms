class Queue:
    def enqueue(self, item: str):
        pass

    def dequeue(self) -> str:
        pass

    def is_empty(self) -> bool:
        pass


class LinkedListQueue(Queue):
    class Node:
        def __init__(self):
            self.item = None
            self.next = None

    def __init__(self):
        self.first: LinkedListQueue.Node = None
        self.last: LinkedListQueue.Node = None

    def enqueue(self, item: str):
        new_node = LinkedListQueue.Node()
        new_node.item = item
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self) -> str:
        result = self.first.item
        self.first = self.first.next
        return result

    def is_empty(self) -> bool:
        return self.first is None

    def print_node(self, node: Node):
        print(f"Queue node {node.item}")
        if node.next:
            self.print_node(node.next)

    def print(self):
        self.print_node(self.first)


class ArrayQueue(Queue):
    def __init__(self):
        self.data = [None] * 2
        self.first = 0
        self.last = 0
        self.size = 0

    def enqueue(self, item: str):
        if self.last == len(self.data):
            new_arr = [None] * self.last * 2
            for i in range(0, self.last - self.first):
                new_arr[i] = self.data[self.first + i]
            self.data = new_arr
            self.first = 0
            self.last = self.size
        self.data[self.last] = item
        self.last += 1
        self.size += 1

    def dequeue(self) -> str:
        if self.size <= len(self.data) / 4:
            new_arr = [None] * int(len(self.data) / 2)
            for i in range(0, self.last - self.first):
                new_arr[i] = self.data[self.first + i]
            self.data = new_arr
            self.first = 0
            self.last = self.size
        result = self.data[self.first]
        self.data[self.first] = None
        self.first += 1
        self.size -= 1
        return result


def LLQ_test():
    queue = LinkedListQueue()
    queue.enqueue("1")
    queue.enqueue("2")
    queue.print()
    print(queue.dequeue())
    queue.enqueue("3")
    queue.enqueue("4")
    queue.enqueue("5")
    queue.print()
    queue.enqueue("6")
    queue.enqueue("7")
    queue.enqueue("8")
    queue.print()
    print(queue.dequeue())
    queue.enqueue("9")
    queue.enqueue("10")
    queue.enqueue("11")
    queue.enqueue("12")
    print(queue.dequeue())
    queue.print()


def AQ_test():
    queue = ArrayQueue()
    queue.enqueue("1")
    queue.enqueue("2")
    print(queue.data)
    print(queue.dequeue())
    queue.enqueue("3")
    queue.enqueue("4")
    queue.enqueue("5")
    print(queue.data)
    queue.enqueue("6")
    queue.enqueue("7")
    queue.enqueue("8")
    print(queue.data)
    print(queue.dequeue())
    print(queue.data)
    queue.enqueue("9")
    queue.enqueue("10")
    queue.enqueue("11")
    queue.enqueue("12")
    print(queue.data)
    print(queue.dequeue())
    print(queue.data)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.data)


if __name__ == '__main__':
    AQ_test()
