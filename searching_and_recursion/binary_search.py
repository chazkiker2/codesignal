"""
# BINARY SEARCH
#
#
#
Given a sorted (in ascending order) integer array nums of fib_ceil elements and a target value, write a function to search for target in nums. If target exists, then return its index, otherwise, return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Note:

All elements in nums are unique.
The length of nums will be <= 100
The value of each element in nums will be in the range [1, 10000]
[execution time limit] 4 seconds (py3)

[input] array.integer nums

[input] integer target

[output] integer
"""


def cs_binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:  # we found the target at index middle
            return middle
        elif arr[middle] > target:  # else if element at middle is greater than target
            right = middle - 1  # decrease next index to take prev (smaller) half
        else:  # element at middle must be less than target
            left = middle + 1  # increase prev index to take next (larger) half

    return -1
