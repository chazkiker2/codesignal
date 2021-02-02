"""
Given an array of strings strings, write a function that can group the anagrams.
The groups should be ordered such that the larger groups come
first, with subsequent groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original letters exactly once.

Example 1:
    Input:
        strs = ["apt","pat","ear","tap","are","arm"]

    Output:
        [["apt","pat","tap"],["ear","are"],["arm"]]


Example 2:
    Input:
        strs = [""]

    Output:
        [[""]]


Example 3:
    Input:
        strs = ["a"]

    Output:
        [["a"]]

Notes:

strs[i] consists of lower-case English letters.
[execution time limit] 4 seconds (py3)

[input] array.string strs

[output] array.array.string

Note: the final array is not sorted as described in the problem.
It's sorted by default key order in the dictionary.
Shouldn't be an issue for most, but if you're doing a weird solution like I did,
 you might fail one of the hidden tests if you try to manually sort with the described order.
"""


def group_anagrams(strings):
    group_map = {''.join(sorted(string)): [] for string in strings}
    for word in strings:
        key = ''.join(sorted(word))
        group_map[key].append(word)

    return [value for value in group_map.values()]

    # set_list = [set(string) for string in strings]
    # set_map = {i: set(string) for i, string in enumerate(strings)}
    # print(set_map)
    #
    # group_map = {letter_set: [] for letter_set in set_map.values()}
    # print(group_map)
    # anagram_map = {}
    # group_map = {}
    # group_count = 0
    # for word in strings:
    #     group_count += 1
    #     # group_map[group_count] = []
    #     # letters = [letter for letter in word]
    #     for letter in word:
    #         if letter not in group_map:
    #             group_map[letter] = group_count
    #
    # print(group_map)
    # nested_list = [value for value in group_map.values()]
    # return nested_list


def tester(input_array, expected):
    actual = group_anagrams(input_array)
    print(f"\n--------")
    print(f"input: {input_array}")
    print(f"actual: {actual}, expected: {expected}")
    print(f"passed: {actual == expected}")
    print(f"--------\n\n")


if __name__ == '__main__':
    tester(["apt",
            "pat",
            "ear",
            "tap",
            "are",
            "arm"],
           [["apt", "pat", "tap"],
            ["ear", "are"],
            ["arm"]]
           )
    tester([""], [[""]])
    tester(["a"], [["a"]])
