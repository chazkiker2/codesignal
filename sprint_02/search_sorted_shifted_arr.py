"""
You are given a sorted array in ascending order that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]) and a target value.

Write a function that returns the target value's index. If the target value is not present in the array, return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

[execution time limit] 4 seconds (py3)

[input] array.integer nums

[input] integer target

[output] integer
"""
from typing import List


def find_pivot(arr, low, high):
    if high < low:  # base
        return -1
    if high == low:
        return low
    mid = (low + high) // 2
    # if mid_idx < high_idx and el at mid is larger than the following element
    if mid < high and arr[mid] > arr[mid + 1]:
        # then mid is the pivot point
        return mid
    # if mid_idx > low_idx and el at mid is less than the el before
    if mid > low and arr[mid] < arr[mid - 1]:
        # then the index next before mid is pivot
        return mid - 1
    # if el at low is larger than or the same as mid
    if arr[low] >= arr[mid]:
        # recurse with the next half
        return find_pivot(arr, low, mid - 1)
    # else, el at mid must be less than the smallest el, recurse with the prev half
    return find_pivot(arr, mid + 1, high)


def bin_search_iter(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            # target found
            return mid
        elif arr[mid] < target:
            # target is greater than mid
            # take larger half
            start = mid + 1
        else:
            # target is less than mid
            # take lower half
            end = mid - 1

    return -1  # target not found


def search_sorted_shifted_arr(nums: List[int], target: int) -> int:
    n = len(nums)
    pivot = find_pivot(nums, 0, n - 1)

    # if no pivot found, array is not rotated at all
    if pivot == -1:
        return bin_search_iter(nums, target, 0, n - 1)

    if nums[pivot] == target:
        # target found
        return pivot

    if nums[0] <= target:
        # end at index before pivot
        return bin_search_iter(nums, target, 0, pivot - 1)

    # start at index after pivot
    return bin_search_iter(nums, target, pivot + 1, n - 1)
