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
    v = collection[start]
    while i <= end:
        if collection[i] < v:
            exchange(collection, i, start)
            i += 1
            start += 1
        elif collection[i] > v:
            exchange(collection, i, end)
            end -= 1
        else:
            i += 1
    return end


def exchange(col, i, j):
    temp = col[i]
    col[i] = col[j]
    col[j] = temp


if __name__ == '__main__':
    coll = [3, 7, 9, 3, 7, 8, 3, 7, 6]
    print(sort(coll))
