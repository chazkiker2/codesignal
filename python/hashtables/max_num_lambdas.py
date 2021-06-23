"""
Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of instances of "lambda" that can be formed.

Example 1:

Input: text = "mbxcdatlas"
Output: 1
Example 2:

Input: text = "lalaaxcmbdtsumbdav"
Output: 2
Example 3:

Input: text = "sctlamb"
Output: 0
Notes:

text consists of lowercase English characters only
[execution time limit] 4 seconds (py3)

[input] string text

[output] integer


"""
from collections import Counter


def max_num_lambdas(text):
    text_count = Counter(text)
    lambda_letters_dic = {
        "l": 1,
        "a": 2,
        "m": 1,
        "b": 1,
        "d": 1,
    }
    lambda_letters_counter = {lambda_letter: text_count[lambda_letter] for lambda_letter in lambda_letters_dic.keys()}
    emptied = False
    lambda_count = 0
    while not emptied:
        for letter in lambda_letters_dic.keys():
            lambda_letters_counter[letter] -= lambda_letters_dic[letter]
            if lambda_letters_counter[letter] < 0:
                emptied = True

        if not emptied:
            lambda_count += 1

    return lambda_count


if __name__ == '__main__':
    actual1 = max_num_lambdas("mbxcdatlas")
    print(f"test_case_01: Passed? {1 == actual1} -- Actual: {actual1}, Expected: {1}")

    actual2 = max_num_lambdas("lalaaxcmbdtsumbdav")
    print(f"test_case_02: Passed? {2 == actual2} —— Actual: {actual2}, Expected: {2}")
