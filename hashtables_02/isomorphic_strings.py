"""
Given two strings a and b, determine if they are isomorphic.

Two strings are isomorphic if the characters in a can be replaced to get b.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input:
a = "odd"
b = "egg"

Output:
true
Example 2:

Input:
a = "foo"
b = "bar"

Output:
false
Example 3:

Input:
a = "abca"
b = "zbxz"

Output:
true
Example 4:

Input:
a = "abc"
b = ""

Output:
false
[execution time limit] 4 seconds (py3)

[input] string a

[input] string b

[output] boolean


"""


def isomorphic_strings(a, b):
    if len(a) != len(b):
        return False

    letter_map = {}
    for a_letter, b_letter in zip(a, b):
        if a_letter not in letter_map:
            letter_map[a_letter] = b_letter
        elif letter_map[a_letter] != b_letter:
            return False

    return True


if __name__ == '__main__':
    a1, b1 = ("egg", "add")
    expected_1 = True
    actual_1 = isomorphic_strings(a1, b1)
    print(f"TEST1: {expected_1}, {actual_1} — Passed? {expected_1 == actual_1}")
    a2, b2 = ("", "")
    expected_2 = True
    actual_2 = isomorphic_strings(a2, b2)
    print(f"TEST1: {expected_2}, {actual_2} — Passed? {expected_2 == actual_2}")

    a3, b3 = ("abc", "")
    expected_3 = False
    actual_3 = isomorphic_strings(a3, b3)
    print(f"TEST1: {expected_3}, {actual_3} — Passed? {expected_3 == actual_3}")
