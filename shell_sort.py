def sort(collection):
    steps = [7, 3, 1]
    for step in steps:
        for i in range(0, len(collection), step):
            for j in range(i - 1, -1, -step):
                if collection[i] < collection[j]:
                    temp = collection[i]
                    collection[i] = collection[j]
                    collection[j] = temp
                    i = j
    return collection


if __name__ == '__main__':
    print(sort([7, 10, 5, 3, 8, 4, 2, 9, 6]))
