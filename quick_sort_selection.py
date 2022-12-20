import random


def select_top_k(collection, k):
    random.shuffle(collection)
    q_select(collection, k, 0, len(collection) - 1)
    return collection[:k]


def q_select(collection, k, start, end):
    pointer = partition(collection, start, end)
    if pointer + 1 < k:
        q_select(collection, k, pointer + 1, end)
    elif pointer + 1 > k:
        q_select(collection, k, 0, pointer)


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
    coll = random.sample(range(1, 100), 30)
    print(coll)
    print(select_top_k(coll, 3))
