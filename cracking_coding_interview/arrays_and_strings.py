# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
# --> Use bit array with length equal number of possible letters and mark 1 in array letter position for inputs
import itertools


def is_unique(input_str: str):
    checker = {}
    for i in range(0, len(input_str) - 1):
        if input_str[i] not in checker:
            checker[input_str[i]] = True
        else:
            return False
    return True


assert is_unique("algorithm")
assert (not is_unique("determine"))


# 1.2 Check Permutation: Given two strings,write a method to decide if one is a permutation of the other.
def permutation(first, second):
    first_counter = {}
    second_counter = {}
    for i, j in itertools.zip_longest(first, second):
        if not i:
            return False
        elif i in first_counter:
            first_counter[i] += 1
        else:
            first_counter[i] = 1

        if not j:
            return False
        elif j in second_counter:
            second_counter[j] += 1
        else:
            second_counter[j] = 1
    return first_counter == second_counter


assert permutation("abcd", "dcba")
assert not (permutation("abcd", "dcbaa"))
