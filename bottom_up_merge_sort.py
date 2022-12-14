def sort(collection):
    for i in range(0, len(collection) - 2, 2):
        if collection[i + 1] < collection[i]:
            exchange(collection, i, i + 1)
    step = 4
    while step < len(collection) * 2:
        for start in range(0, len(collection), step):
            merge(collection, start, start + step - 1)
        step *= 2
    return collection


def merge(col, start, end):
    aux = col[start: end + 1]
    i = 0
    j = int(((end - start) / 2) + 1)
    for k in range(0, len(aux)):
        if j <= len(aux) - 1 and aux[j] < aux[i]:
            col[start + k] = aux[j]
            j += 1
        else:
            col[start + k] = aux[i]
            i += 1


def exchange(col, i, j):
    temp = col[i]
    col[i] = col[j]
    col[j] = temp


if __name__ == '__main__':
    print(sort([22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
