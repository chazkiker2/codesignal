

# find freq of specific letter in dict
# find freq of specific letter in word
# "Hello, World" -- max count per ? 3 -- max count per word ?
#
# character -- list of words
# character
# unit / unit ratio
#
# return the ratio of occurrences
# - how often that character happens per word

from collections import Counter

def k_most_words(words, k):
    """
    :param words: non-empty list of words
    :param k: the number of elements to return
    :return: the k most frequent words in list
    """
    # Iterate
    # add to a dictionary
    # count + 1 for each value for every occurence

    counted = Counter(words)
    print(counted)

    for k, v in counted.most_common(k):
        print(f"{k}, {v}")


if __name__ == '__main__':
    test_cases = [
        (
            ["i", "love", "leetcode", "i", "love", "coding"],
            2,
            ["i", "love"]
        ),
    ]

    for words, k, expected in test_cases:
        actual = k_most_words(words, k)
        print(f"{actual=} {expected=} {actual == expected}")