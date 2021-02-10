"""
Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

Examples:

csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"
"""


def longest_possible_01(str_1, str_2):
    to_sort = str_1 + str_2 if str_1 != str_2 else str_1
    unique = ""

    for char in to_sort:
        if char not in unique:
            unique += char

    return "".join(sorted(unique))
