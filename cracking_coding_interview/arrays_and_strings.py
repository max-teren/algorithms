import random
from typing import List
import itertools


# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
# --> Use bit array with length equal number of possible letters and mark 1 in array letter position for inputs
def is_unique(input_str: str):
    checker = {}
    for i in range(0, len(input_str) - 1):
        if input_str[i] not in checker:
            checker[input_str[i]] = True
        else:
            return False
    return True


assert is_unique("algorithm")
assert not is_unique("determine")


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


# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement
# of letters. The palindrome does not need to be limited to just dictionary words.
def is_palindrome_permutation(line: str):
    counter = {}
    for char in line.lower():
        if char == " ":
            continue
        elif char in counter:
            counter[char] = counter[char] + 1
        else:
            counter[char] = 1
    center = False
    for val in counter.values():
        if val % 2 == 0:
            continue
        elif not center:
            center = True
        else:
            return False
    return True


assert is_palindrome_permutation("Tact Coa")


# 1.5 One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
def one_way(first: str, second: str):
    first_iterator_i = iter(first)
    first_iterator_j = iter(first)
    next(first_iterator_j)

    second_iterator_i = iter(second)
    second_iterator_j = iter(second)
    next(second_iterator_j)

    first_length = len(first)
    second_length = len(second)
    if abs(first_length - second_length) > 1:
        return False
    changes_counter = 0
    for i in range(0, max(first_length, second_length)):
        if changes_counter > 1:
            return False
        else:
            first_value_one = next(first_iterator_i, None)
            first_value_two = next(first_iterator_j, None)

            second_value_one = next(second_iterator_i, None)
            second_value_two = next(second_iterator_j, None)

            if first_value_one == second_value_one:
                continue
            elif first_value_two == second_value_one:
                changes_counter += 1
                next(first_iterator_i)
                next(first_iterator_j)
                continue
            elif second_value_two == first_value_one:
                changes_counter += 1
                next(second_iterator_i)
                next(second_iterator_j)
                continue
            else:
                changes_counter += 1
                continue
    return True


assert not one_way("pale", "bake")
assert one_way("pale", "ple")


# 1.6 String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3.
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).
def string_compression(line: str):
    compressed = []
    counter = 0
    for i in range(0, len(line)):
        counter += 1
        if i + 1 > (len(line) - 1) or line[i] != line[i + 1]:
            compressed.append(f"{line[i]}{counter}")
            counter = 0

    commpresed_line = "".join(compressed)
    return commpresed_line if len(commpresed_line) < len(line) else line


assert string_compression("aabcccccaaa") == "a2b1c5a3"


# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in
# the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place?
def rotate_matrix(n: int):
    def init_matrix():
        matrix = []
        for i in range(0, n):
            matrix.append(random.sample(range(1, 100), n))
        return matrix

    matrix = init_matrix()
    for row in matrix:
        print(row)

    rotated_matrix = []
    for i in range(0, n):
        column = list(map(lambda x: x[i], matrix))
        column.reverse()
        rotated_matrix.append(column)

    print("\n")
    for row in rotated_matrix:
        print(row)

    return rotated_matrix


# rotate_matrix(5)


# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.
def zero_matrix(n: int, m: int):
    def init_matrix():
        matrix = []
        for i in range(0, n):
            matrix.append(random.sample(range(0, 10), m))
        return matrix

    matrix = init_matrix()
    for row in matrix:
        print(row)

    zero_rows = set()
    zero_columns = set()
    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)

    emtry_row = [0 for i in range(0, m)]
    for i in range(0, n):
        if i in zero_rows:
            matrix[i] = emtry_row
        else:
            for j in zero_columns:
                matrix[i][j] = 0

    print()
    for row in matrix:
        print(row)


# zero_matrix(5, 6)


# 1.9 String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a
# substring of another. Given two strings, sl and s2, write code to check if s2 is a rotation
# of sl using only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").
def string_rotation(s1: str, s2: str):
    s3 = s2 + s2
    return s3.find(s1) != -1


print(string_rotation("waterbottle", "erbottlewat"))
