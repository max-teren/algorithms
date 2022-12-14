from copy import copy


def sort(collection):
    m_sort(collection, 0, len(collection) - 1)
    return collection


def m_sort(col, start, end):
    if end - start == 0:
        return
    elif end - start == 1:
        col if col[start] < col[end] else exchange(col, start, end)
    else:
        mid = int((end - start) / 2)
        m_sort(col, start, start + mid)
        m_sort(col, start + mid + 1, end)
        merge(col, start, end)


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
    print(sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
