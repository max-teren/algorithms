class MBH:

    def __init__(self):
        self.heap: [int] = [None, ]
        self.k = 1

    def insert(self, element):
        self.heap.append(element)
        self.swim(self.k)
        self.k += 1

    def pull_max(self):
        self.exchange(1, self.k - 1)
        heap_max = self.heap.pop(self.k - 1)
        self.k -= 1
        self.sink(1)
        return heap_max

    def size(self):
        return len(self.heap) - 1

    def swim(self, index):
        parent_index = int(index / 2)
        if parent_index > 0 and self.heap[index] > self.heap[parent_index]:
            self.exchange(index, parent_index)
            self.swim(parent_index)

    def sink(self, index):
        if index * 2 + 1 < self.k and self.heap[index * 2 + 1] > self.heap[index * 2]:
            max_child_index = index * 2 + 1
        elif index * 2 < self.k:
            max_child_index = index * 2
        else:
            return
        if self.heap[index] < self.heap[max_child_index]:
            self.exchange(index, max_child_index)
            self.sink(max_child_index)

    def exchange(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp


if __name__ == '__main__':
    max_binary_heap = MBH()
    max_binary_heap.insert('T')
    max_binary_heap.insert('P')
    max_binary_heap.insert('R')
    max_binary_heap.insert('N')
    max_binary_heap.insert('H')
    max_binary_heap.insert('O')
    max_binary_heap.insert('A')
    max_binary_heap.insert('E')
    max_binary_heap.insert('I')
    max_binary_heap.insert('G')
    max_binary_heap.insert('S')
    print(max_binary_heap.pull_max())
    print(max_binary_heap.heap[1:])
    print(max_binary_heap.pull_max())
    print(max_binary_heap.heap[1:])
    max_binary_heap.insert('S')
    print(max_binary_heap.heap[1:])
