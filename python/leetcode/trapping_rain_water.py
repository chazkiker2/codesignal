"""
Given `n` non-negative integers representing an elevation map where the
width of each bar is `1`, compute how much water it can trap after raining.

## Example 1:

- Input: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`
- Output: `6`
- Explanation: The above elevation map (black section) is represented by
array `[0,1,0,2,1,0,1,3,2,1,2,1]`.
In this case, `6` units of rain water (blue section) are being trapped.


[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6


              XX
      XX......XXXX..XX
  XX..XXXX..XXXXXXXXXXXX
0 1 0 2 1 0 1 3 2 1 2 1   Elevation
0 0 1 0 1 2 1 0 0 1 0 0   Water
0 1 1 2 2 2 2 3 3 3 3 3   Capacity


## Example 2:

- Input: `height = [4,2,0,3,2,5]`
- Output: `9`


          XX
XX........XX
XX....XX..XX
XXXX..XXXXXX
XXXX..XXXXXX
4 2 0 3 2 5     Elevation
0 2 4 1 2 0     Water
4 4 4 4 4 5



## Constraints:

- `n == height.length`
- `0 <= n <= 3 * 104`
- `0 <= height[i] <= 105`
"""

from parameterized import parameterized
import unittest
from typing import List
from heapq import heapify
from collections import deque


class Solution(object):
    def trap_pointers(self, height):
        """
        - time: O(n). Single iteration of O(n)
        - space: O(1) extra space. Only constant space required for `left`, `right`, `left_max`, and `right_max`
        """
        answer = 0

        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    answer += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    answer += right_max - height[right]

                right -= 1

        return answer

    def trap_stack(self, height):
        """
        - Time complexity: O(n).
            - Single iteration of O(n) in which each bar can be touched at most twice(due to insertion and deletion from stack) and insertion and deletion from stack takes O(1) time.
        - Space complexity: O(n). Stack can take up to O(n) space in case of stairs-like or flat structure.
        """
        answer = 0
        current = 0
        stack = deque()
        while current < len(height):
            # while stack is not empty and the current bar is higher than the current bar at the top of the stack
            while stack and height[current] > height[stack[-1]]:
                # pop the current bar from the top of our stack
                top = stack.pop()

                # if stack is now empty, break
                if not stack:
                    break

                # find the distance b/w current el and the element at the top of the stack, which is to be filled
                distance = current - stack[-1] - 1
                # find the bounded height
                bounded_height = min(
                    height[current], height[stack[-1]]
                ) - height[top]

                # add resulting trapped water to the answer
                answer += distance * bounded_height

            # push current index to top of the stack
            stack.append(current)
            # move current to the next position
            current += 1

        # return the number of filled water units
        return answer

    def trap_dynamic(self, height: List[int]) -> int:
        """
        Complexity Analysis:
        -  time: O(n)
            - we store max hieghts up to a point using 2 iterations of O(n) each
            - we finally update answer using the stored values in O(n)
        - space: O(n) extra space
            - additional O(n) space for left_max and right_max arrays than in a brute force approach that would
            manually find left and right parts over and over just to find the highest bar size up to that index in O(n^2) time and O(1) space
        """
        answer = 0

        if not height:
            return answer

        len_height = len(height)
        left_max = [0 for _ in range(len_height)]
        right_max = [0 for _ in range(len_height)]

        for i in range(len_height):
            left_max[i] = max(height[i], left_max[i-1])

        right_max[len_height - 1] = height[len_height-1]
        for i in range(len_height-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])

        answer += sum(
            [
                min(left_max[i], right_max[i]) - height[i]
                for i in range(len_height)
            ]
        )

        return answer


class Test(unittest.TestCase):

    @parameterized.expand([
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9)
    ])
    def test_solution_dyn(self, height, expected):
        solution = Solution()
        self.assertEqual(expected, solution.trap_dynamic(height))

    @parameterized.expand([
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9)
    ])
    def test_solution_stack(self, height, expected):
        solution = Solution()
        self.assertEqual(expected, solution.trap_stack(height))

    @parameterized.expand([
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9)
    ])
    def test_solution_pointers(self, height, expected):
        solution = Solution()
        self.assertEqual(expected, solution.trap_pointers(height))


if __name__ == "__main__":
    unittest.main()
