"""
Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.

Examples:
`csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
`csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"
"""


def remove_duplicate_words(input_str):
    unique_words = []  # unique words will go here

    # split input_str into individual words
    split_input = input_str.split()

    for word in split_input:  # for every word in input
        if word not in unique_words:  # If word is new
            unique_words.append(word)  # Add word to unique list

    # return unique words separated by a space
    return " ".join(unique_words)
