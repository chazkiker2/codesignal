"""
You are given a non-empty array of integers.

One element appears exactly once, with every other element appearing at least twice, perhaps more.

Write a function that can find and return the element that appears exactly once.

Example 1:

Input: [1,1,2,1]
Output: 2
Example 2:

Input: [1,2,1,2,1,2,80]
Output: 80
Note: You should be able to develop a solution that has O(n) time complexity.

[execution time limit] 4 seconds (py3)

[input] array.integer nums

[output] integer
"""
from functools import reduce

from collections import Counter

def find_single_number(nums):
    return Counter(nums).most_common()[:-2:-1][0][0]


def find_single_number_positive_ints(nums):
    ans = 0

    for x in nums:
        ans ^= x  # bitwise xor equals

    return ans


if __name__ == '__main__':
    test_case_01 = [2, 2, -3, 2]
    expected_01 = -3
    actual_01 = find_single_number(test_case_01)
    print(f"test_case_01: Passed? {expected_01 == actual_01}")

    test_case_02 = [0, 1, 0, 1, 0, 1, 99]
    expected_02 = 99
    actual_02 = find_single_number(test_case_02)
    print(f"test_case_02: Passed? {actual_02 == expected_02}")
