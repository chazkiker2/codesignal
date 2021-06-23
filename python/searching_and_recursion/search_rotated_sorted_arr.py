"""
# SEARCH ROTATED SORTED ARRAY
#
#
#
Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You should search for target in nums and if found return its index, otherwise return -1.

Example 1:
Input: nums = [6,7,0,1,2,3,4,5], target = 0
Output: 2

Example 2:
Input: nums = [6,7,0,1,2,3,4,5], target = 3
Output: 5

Example 3:
Input: nums = [1], target = 0
Output: -1

Note:

1 <= nums.length < 100
1 <= nums[i] <= 100
All values of nums are unique.
[execution time limit] 4 seconds (py3)

[input] array.integer nums

[input] integer target

[output] integer
"""


def bin_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1


def cs_search_rotated_sorted_array(nums, target):
    # piv = find_pivot(nums)
    length_nums = len(nums)
    index_max = max(range(length_nums), key=nums.__getitem__)

    if index_max == length_nums - 1:  # arr is not pivoted
        return bin_search(nums, target)
    else:
        nums_sorted = nums[index_max::] + nums[:index_max]
        sorted_res = bin_search(nums_sorted, target)

        return (sorted_res + index_max) % length_nums
