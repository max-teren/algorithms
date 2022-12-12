def sort(collection):
    for i in range(0, len(collection)):
        for j in range(i - 1, -1, -1):
            if collection[i] < collection[j]:
                exchange(collection, i, j)
                i = j
            else:
                break
    return collection


def exchange(col, i, j):
    temp = col[i]
    col[i] = col[j]
    col[j] = temp


if __name__ == '__main__':
    print(sort([7, 10, 5, 3, 8, 4, 2, 9, 6]))