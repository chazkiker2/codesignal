"""
# [Leetcode 88: Merge Sorted Array]

[Leetcode 88: Merge Sorted Array]: https://leetcode.com/problems/merge-sorted-array/

- Difficulty: Easy


## Description

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

## Examples


### Example 1

- Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
- Output: [1,2,2,3,5,6]
- Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
  The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

### Example 2

- Input: nums1 = [1], m = 1, nums2 = [], n = 0
- Output: [1]
- Explanation: The arrays we are merging are [1] and [].
  The result of the merge is [1].

### Example 3

- Input: nums1 = [0], m = 0, nums2 = [1], n = 1
- Output: [1]
- Explanation: The arrays we are merging are [] and [1].
  The result of the merge is [1].
  Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

## Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-109 <= nums1[i], nums2[j] <= 109`


**Follow up:** Can you come up with an algorithm that runs in O(m + n) time?
"""


class Solution(object):
    def merge_py(self, nums1, m, nums2, n):
        nums1[m:m+n] = nums2
        nums1.sort()

    def merge(self, nums1, m, nums2, n):
        """
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

        Merge nums1 and nums2 into a single array sorted in non-decreasing order.

        The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
        To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should
        be merged, and the last `n` elements are set to 0 and should be ignored. nums2 has a length of n.
        """
        # self.merge_easy(nums1, m, nums2, n)
        # self.merge_pointers(nums1, m, nums2, n)
        self.merge_pointers_o1_space(nums1, m, nums2, n)

    def merge_pointers_o1_space(self, nums1, m, nums2, n):
        """

        ## Complexity Analysis

            - Time Complexity
                - O(n + m) same as `merge_pointers`
            - Space Complexity:
                - O(1). Unlike `merge_pointers` we don't use an extra array

        ## Proof

            1. We know that upon initialization, `p` is `n` steps ahead of `p1`. (In other words, `p1 + n = p`)
            2. We also know that during each of the `p` iterations this algorithm performs, `p` is always decremented by `1`
               and either `p1` or `p2` is decremented by `1`
            3. We can deduce that when `p1` decremented, the gap between `p` and `p1` stays the same, so there cannot be an "overtake" in that case
            4. We can also deduce that when `p2` is decremented though, the gap between `p` and `p1` shrinks by `1` as `p` moves, but not `p1`.
            5. From that, we can deduce that the maximum number of times that `p2` can be decremented is `n`. In other words, the gap between `p` and `p1`
               can shrink by `1` at most `n` times.
            6. In conclusion, it's impossible for an overtake to occur, as `p` and `p1` started `n` apart. When `p = p1` the gap has to have shrunk `n` times.
               This means that all of `nums2` has been merged, so there is nothing more to do.

        ## Demonstration

            ### STAGE 001

                nums1 = [1, 2, 3, 0, 0, 0]
                            ^        ^
                            p1       p

                nums2 = [2, 5, 6]
                            ^
                            p2

                nums1[p1=2] = 3
                nums2[p2=2] = 6
                3 < 6
                nums1[p=6] = nums2[p2=2] = 6
                p2 -= 1

                nums1 == [1, 2, 3, 0, 0, 6]

            ### STAGE 002

                nums1 = [1, 2, 3, 0, 0, 6]
                            ^     ^
                            p1    p

                nums2 = [2, 5, 6]
                            ^
                            p2

                nums1[p1=2] = 3
                nums2[p2=1] = 5
                3 < 6
                nums1[p=5] = nums2[p2=1] = 5
                p2 -= 1

                nums1 == [1, 2, 3, 0, 5, 6]


            ### STAGE 003

                nums1 = [1, 2, 3, 0, 5, 6]
                            ^  ^
                            p1 p

                nums2 = [2, 5, 6]
                        ^
                        p2

                nums1[p1=2] = 3
                nums2[p2=0] = 2
                3 > 2
                nums1[p=4] = nums1[p1=2] = 3
                p1 -= 1
                nums1 == [1, 2, 3, 3, 5, 6]


            ### STAGE 004

                nums1 == [1, 2, 3, 3, 5, 6]
                            ^  ^
                            p1 p

                nums2 = [2, 5, 6]
                        ^
                        p2

                nums1[p1=1] = 2
                nums2[p2=0] = 2
                2 == 2
                nums1[p=2] = nums1[p1=1] = 2
                p1 -= 1 -> p1 = 0

            ### STAGE 005

                nums1 == [1, 2, 2, 3, 5, 6]
                        ^  ^
                        p1 p

                nums2 = [2, 5, 6]
                        ^
                        p2

                nums1[p1=0] = 1
                nums2[p2=0] = 2
                1 < 2
                nums1[p=1] = nums2[p2=0] = 2
                p2 -= 1 -> p2 = -1
                nums1 = [1, 2, 2, 3, 5, 6]

            ### STAGE 006

                break loop b/c p2 < 0
        """
        p1 = m - 1
        p2 = n - 1
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

    def merge_pointers(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        p1 = 0
        p2 = 0

        # compare elements from nums1_copy and nums2
        # write the smallest to nums1
        for p in range(n + m):
            # ensure that p1 and p2 aren't over boundaries
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

    def merge_easy(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[i+m] = nums2[i]

        nums1.sort()

        return nums1


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    sol.merge(
        nums1,
        3,
        [2, 5, 6],
        3,
    )
    expected = [1, 2, 2, 3, 5, 6]
    print(f"{nums1=}")
