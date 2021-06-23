"""
Given a pattern and a string a, find if a follows the same pattern.

Here, to "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in s.

Example 1:

Input:
pattern = "abba"
a = "lambda school school lambda"

Output: true
Example 2:

Input:
pattern = "abba"
a = "lambda school school coding"

Output:
false
Example 3:

Input:
pattern = "aaaa"
a = "lambda school school lambda"

Output: false
Example 4:

Input:
pattern = "abba"
a = "lambda lambda lambda lambda"

Output: false
Notes:

pattern contains only lower-case English letters.
a contains only lower-case English letters and spaces ' '.
a does not contain any leading or trailing spaces.
All the words in a are separated by a single space.
[execution time limit] 4 seconds (py3)

[input] string pattern

[input] string a

[output] boolean
"""


def word_pattern(pattern, a):
    split_words = a.split()  # split a into separate words

    if len(pattern) != len(split_words):
        # pattern length and num of words is different
        # not a match
        return False

    pattern_dict = {}

    # rep stands for "repetition", as in the instance in pattern
    for rep, word in zip(pattern, split_words):
        if rep not in pattern_dict:
            pattern_dict[rep] = word
        if word not in pattern_dict:
            pattern_dict[word] = rep
        if pattern_dict[rep] != word or pattern_dict[word] != rep:
            return False

    return True


def tester(pattern, string, expected):
    actual = word_pattern(pattern, string)
    print(f"\n--------")
    print(f"pattern: {pattern}, string: {string}")
    print(f"actual: {actual}, expected: {expected}, passed: {actual == expected}")


if __name__ == '__main__':
    tester("abba", "lambda school school lambda", True)
    tester("abba", "lambda school school coding", False)
    tester("aaaa", "lambda school school lambda", False)
    tester("abba", "lambda lambda lambda lambda", False)
    tester("abc", "abc", False)
    tester("t", "l", True)
