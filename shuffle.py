import random


def shuffle(collection):
    for i in range(0, len(collection)):
        r = random.randint(0, i)
        exchange(collection, i, r)
    return collection


def exchange(col, i, j):
    temp = col[i]
    col[i] = col[j]
    col[j] = temp


if __name__ == '__main__':
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9]))
