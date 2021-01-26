"""
Two words are blanagrams if they are anagrams but exactly one letter has been substituted for another.

Given two words, check if they are blanagrams of each other.

Example

For word1 = "tangram" and word2 = "anagram", the output should be
checkBlanagrams(word1, word2) = true;

After changing the first letter 't' to 'a' in the word1, the words become anagrams.

For word1 = "tangram" and word2 = "pangram", the output should be
checkBlanagrams(word1, word2) = true.

Since a word is an anagram of itself (a so-called trivial anagram), we are not obliged to rearrange letters. Only the substitution of a single letter is required for a word to be a blanagram, and here 't' is changed to 'p'.

For word1 = "aba" and word2 = "bab", the output should be
checkBlanagrams(word1, word2) = true.

You can take the first letter 'a' of word1 and change it to 'b', obtaining the word "bba", which is an anagram of word2 = "bab". It is also possible to change the first letter 'b' of word2 to 'a' and obtain "aab", which is an anagram of word1 = "aba".

For word1 = "silent" and word2 = "listen", the output should be
checkBlanagrams(word1, word2) = false.

These two words are anagrams of each other, but no letter substitution was made (the trivial substitution of a letter with itself shouldn't be considered), so they are not blanagrams.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string word1
    A string consisting of lowercase letters.
Guaranteed constraints:
    - 1 ≤ word1.length ≤ 100.

[input] string word2
    A string consisting of lowercase letters.
Guaranteed constraints:
 word2.length = word1.length.

[output] boolean

Return true if word1 and word2 are blanagrams of each other, otherwise return false.
"""
from collections import Counter


def check_blanagrams(word1, word2):
    dif_dict = Counter(word1) - Counter(word2)
    return sum(dif_dict.values()) == 1
    # return sum((Counter(word1) - Counter(word2)).values()) == 1
    # dict1, dict2 = Counter(word1), Counter(word2)
    # return sum((dict1-dict2).values()) == 1

    # print(f"d1-d2={sum((dict1-dict2).values())} and d2-d1={sum((dict2-dict1).values())}")

    # print(f"d1={dict1}\nd2={dict2}\nd1-d2={dict1-dict2}\nd2-d1={dict2-dict1}")
    # print((dict1-dict2).values())
    # print((dict1-dict2).values())
    # for zipped in zip(dict1, dict2):
    #     print(zipped)
    # non_match = []

    # for letter in dict1:
    #     # if dict2.get(letter) is
    #     # k, v = vek
    #     if dict1[letter] != dict2.get(letter):
    #
    #     print(f"d1=({letter}: {dict1[letter]}), d2=({letter}: {dict2.get(letter)})")
    #     # print(f"d1=({k}, {v}), d2: ({k}, {dict2.get(k)})")


# print(check_blanagrams("tangram", "anagram"))


def check_blanagrams_wrong(word1, word2):
    filtered_dict = dict(filter(lambda el: el[1] % 2 != 0, Counter(word1 + word2).items()))
    return len(filtered_dict) == 2


def check_blanagrams_old(word1, word2):
    sorted_dict = Counter(sorted(word1 + word2))
    filtered_dict = dict(filter(lambda el: el[1] % 2 != 0, sorted_dict.items()))
    # filtered_dict = {k: v for (k, v) in sorted_dict.items() if v % 2 != 0}

    print(filtered_dict.items())

    if len(filtered_dict.items()) > 2 or len(filtered_dict.items()) == 0:
        # more than 2 non-matches
        return False

    else:
        # only two entries in dict
        return True

        # arr = filtered_dict.items()
        # print(arr[0][1])
        # if (arr[0][1]  % 2) == (arr[1][1] % 2):
        #     return True
        # arr = filtered_dict.items()
        # if arr[0][1] == arr[1][1]:
        #     return True
        # for k, v in filtered_dict.items():
        #     filtered_dict[k] = (v % 2)
        #     print(f"{k}, {v}")

    # print(sorted_dict)
    # print(filtered_dict)

    # print(f"w1={w1_dict}, w2={w2_dict}")
