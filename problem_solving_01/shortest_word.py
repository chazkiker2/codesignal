"""
Given a string of words, return the length of the shortest word(s).

Notes:

The input string will never be empty and you do not need to validate for different data types.

"""


def shortest_word_01(input_str):
    split_str = input_str.split()
    min_length = split_str[0]
    for word_str in split_str:
        if len(word_str) < min_length:
            min_length = len(word_str)


def shortest_word_02(input_str):
    return min(len(word_str) for word_str in input_str.split())


if __name__ == '__main__':
    print(shortest_word_01("Chaz is not the shortest word"))
    print(shortest_word_02("Chaz is not the shortest word"))
