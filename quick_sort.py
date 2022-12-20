def sort(collection):
    q_sort(collection, 0, len(collection) - 1)
    return collection


def q_sort(collection, start, end):
    pointer = partition(collection, start, end)
    if pointer - 1 > start:
        q_sort(collection, start, pointer - 1)
    if pointer + 1 < end:
        q_sort(collection, pointer + 1, end)


def partition(collection, start, end):
    i = start + 1
    while i <= end:
        while collection[i] < collection[start]:
            i += 1
        while collection[end] > collection[start]:
            end -= 1
        if i < end:
            exchange(collection, i, end)
    exchange(collection, start, end)
    return end


def exchange(col, i, j):
    temp = col[i]
    col[i] = col[j]
    col[j] = temp


if __name__ == '__main__':
    coll = [23, 26, 16, 17, 11, 24, 7, 3, 22, 9]
    print(sort(coll))
