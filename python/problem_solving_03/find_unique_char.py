"""
Given a string, write a function that returns the index of the first unique (non-repeating) character. If there isn't a unique (non-repeating) character, return -1.

Examples:

csFirstUniqueChar(input_str = "lambdaschool") -> 2
csFirstUniqueChar(input_str = "ilovelambdaschool") -> 0
csFirstUniqueChar(input_str = "vvv") -> -1
Notes:

input_str will only contain lowercase alpha characters.
"""


def first_unique_char_01(input_str):
    unique = {}
    for i, letter in enumerate(input_str):
        if unique.get(letter) is not None:
            unique[letter] = -1
        else:
            unique[letter] = i

    first = -1
    for x in unique:
        i = unique[x]
        if (first >= 0 and 0 <= i < first) or first < 0:
            first = i

    return first if first is not None else -1
