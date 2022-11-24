class UQF:
    def __init__(self, size: int):
        self.ids = list(range(0, size))

    def union(self, node1: int, node2: int):
        val1 = self.ids[node1]
        val2 = self.ids[node2]
        for i in range(0, len(self.ids)):
            if self.ids[i] == val1:
                self.ids[i] = val2
        print(self.ids)

    def connected(self, node1: int, node2: int) -> bool:
        return self.ids[node1] == self.ids[node2]


class QUF:
    def __init__(self, size: int):
        self.ids = list(range(0, size))

    def union(self, node1: int, node2: int):
        self.ids[self.get_root(node1)] = node2
        print(self.ids)

    def connected(self, node1: int, node2: int) -> bool:
        return self.get_root(node1) == self.get_root(node2)

    def get_root(self, node: int) -> int:
        if self.ids[node] == node:
            return node
        else:
            return self.get_root(self.ids[node])


class WQUF:
    def __init__(self, size: int):
        self.ids = list(range(0, size))
        self.weights = [1] * size

    def union(self, node1: int, node2: int):
        node1_root = self.get_root(node1)
        node2_root = self.get_root(node2)
        if self.weights[node1_root] >= self.weights[node2_root]:
            self.ids[node2_root] = node1_root
            self.weights[node1_root] += self.weights[node2_root]
        else:
            self.ids[node1_root] = node2_root
            self.weights[node2_root] += self.weights[node1_root]
        print(self.ids)

    def connected(self, node1: int, node2: int) -> bool:
        return self.get_root(node1) == self.get_root(node2)

    def get_root(self, node: int) -> int:
        self.ids[node] = self.ids[self.ids[node]]  # path compression
        if self.ids[node] == node:
            return node
        else:
            return self.get_root(self.ids[node])


if __name__ == '__main__':
    n = int(input("Enter number of elements:"))
    uf = WQUF(n)
    print(uf.ids)
    print(len(uf.ids))
    connection = input("Add connections:\n")
    while connection:
        p, q = map(int, connection.split(" "))
        if not uf.connected(p, q):
            uf.union(p, q)
        connection = input("")
    check_connection = input("Check connections:\n")
    while check_connection:
        p, q = map(int, check_connection.split(" "))
        print(uf.connected(p, q))
        check_connection = input("")
