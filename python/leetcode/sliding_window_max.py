"""
You are given an array of integers `nums`, there is a sliding window of size `k`
which is moving from the very left of the array to the very right.

You can only see the `k` numbers in the window. Each time the sliding window moves
right by one position.

Return the max sliding window.


## Example 1:

- Input: `nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`
- Output: `[3, 3, 5, 5, 6, 7]`
- Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


## Example 2:

- Input: `nums = [1]`, `k = 1`
- Output: `[1]`


## Example 3:

- Input: `nums = [1, -1]`, `k = 1`
- Output: `[1, -1]`


## Example 4:

- Input: `nums = [9, 11]`, `k = 2`
- Output: `[11]`


## Example 5:

- Input: `nums = [4, -2]`, `k = 2`
- Output: `[4]`


## Constraints:

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `1 <= k <= nums.length`
"""


import unittest
from collections import deque
import util


class Solution(object):

    def max_sliding_window_dynamic(self, nums, k):
        """
        - time  : `O(N)`, since all we do is `3` passes along the array of length `N`.
        - space : `O(N)` to keep left and right arrays of length `N`, and output array of length `N - k + 1`
        """
        n = len(nums)

        if n * k == 0:
            return []

        if k == 1:
            return nums

        left, right = ([0 for _ in range(n)] for _ in range(2))
        left[0] = nums[0]
        right[n - 1] = nums[n - 1]

        for i in range(1, n):
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        return [
            max(left[i + k - 1], right[i]) for i in range(n - k + 1)
        ]

    def max_sliding_window_deque(self, nums, k):
        """
        - time  : `O(N)`, since each element is processed exactly twice - it's index added and then removed from the deque.
        - space : `O(N)`, since `O(N−k+1)` is used for an output array and `O(k)` for a deque.
        """
        # base cases
        n = len(nums)

        if n * k == 0:
            return []

        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

    def max_sliding_window_bad(self, nums, k):
        """
        - time : O(N ^ 2)
        - space: O(N)
        """
        if len(nums) < k:
            raise ValueError("k cannot be larger than len(nums)")
        return [
            max(nums[i:i+k]) for i in range(len(nums) - k + 1)
        ]


# class Test(unittest.TestCase):
#     def setUp(self) -> None:
#         super().setUp()
#         self.fn = Solution().max_sliding_window_dynamic
    # def test_001(self):
    #     self.assertEqual(
    #         [3, 3, 5, 5, 6, 7],
    #         self.fn([1, 3, -1, -3, 5, 3, 6, 7], 3)
    #     )


if __name__ == "__main__":

    test_deq = util.Tester(Solution().max_sliding_window_deque)

    test_many = util.TestMany(
        [
            Solution().max_sliding_window_bad,
            Solution().max_sliding_window_deque,
            Solution().max_sliding_window_dynamic
        ]
    )

    test_many.test(
        [3, 3, 5, 5, 6, 7],
        ([1, 3, -1, -3, 5, 3, 6, 7], 3)
    )

    # test_dyn = util.Tester(Solution().max_sliding_window_dynamic)
    # print(test_dyn)

    # test_dyn.test(
    #     [3, 3, 5, 5, 6, 7],
    #     ([1, 3, -1, -3, 5, 3, 6, 7], 3)
    # )
    # test_dyn.run()

    test_many.run()
