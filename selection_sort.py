def sort(collection):
    for i in range(0, len(collection)):
        smallest_index = i
        for j in range(i + 1, len(collection)):
            if collection[j] < collection[smallest_index]:
                smallest_index = j
        temp = collection[i]
        collection[i] = collection[smallest_index]
        collection[smallest_index] = temp
    return collection


if __name__ == '__main__':
    print(sort([7, 10, 5, 3, 8, 4, 2, 9, 6]))
