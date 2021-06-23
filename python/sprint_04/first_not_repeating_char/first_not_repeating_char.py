"""
Given a string s consisting of small English letters,
find and return the first instance of a non-repeating
character in it.

If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
first_not_repeating_character(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
first_not_repeating_character(s) = '_'.

There are no characters in this string that do not repeat.

[execution time limit] 4 seconds (py3)

[input] string s

A string that contains only lowercase English letters.

[output] char

The first non-repeating character in s of '_' if there are no characters that do not repeat.

"""
from collections import Counter


def first_not_repeating_char(s):
    counter = Counter(s)
    print(counter)

    for char, count in counter.items():
        if count == 1:
            return char

    return "_"


def tester(fn_input, expected_output):
    actual_output = first_not_repeating_char(fn_input)
    print("\n\n-----TEST")
    print(f"input: {fn_input}")
    print(f"actual: {actual_output}")
    print(f"expected: {expected_output}")
    print(f"\n\npassed: {actual_output == expected_output}")


if __name__ == '__main__':
    tester("abacabad", "c")
    tester("abacabaabacaba", "_")
