"""
Given a string, return a new string with all the vowels removed.

Examples:

csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"

Notes:
- For this challenge, "y" is not considered a vowel.

"""


def remove_the_vowels_01(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    new_str = input_str
    for char in vowels:
        new_str = new_str.replace(char, '')

    return new_str


def remove_the_vowels_02(input_str):
    return "".join(char for char in input_str if (char.lower() not in "aeiou"))


if __name__ == '__main__':
    r1 = remove_the_vowels_01("chaz")
    r2 = remove_the_vowels_02("chaz")
    print(r1)
    print(r2)
