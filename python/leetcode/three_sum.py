"""
Leetcode 15: 3Sum

https://leetcode.com/problems/3sum/

This problem is a follow up to the following problems:

- 2Sum    - LeetCode 1   - https://leetcode.com/problems/two-sum/
- 2Sum II - LeetCode 167 - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


Related:

- [3Sum Closest]
- [4Sum]
- [3Sum Smaller]

[3Sum Closest]: https://leetcode.com/problems/3sum-closest/
[4Sum]: https://leetcode.com/problems/4sum/
[3Sum Smaller]: https://leetcode.com/problems/3sum-smaller/
"""

import unittest


class Solution(object):

    def three_sum_hash_set(self, nums):
        """
        # Description

            <!-- Links -->
            [Two Sum]: https://leetcode.com/articles/two-sum/
            [3Sum Smaller]: https://leetcode.com/problems/3sum-smaller/
            [3Sum Closest]: https://leetcode.com/problems/3sum-closest/
            [Two Sum: One-pass Hash Table]: https://leetcode.com/articles/two-sum/#approach-3-one-pass-hash-table
            <!-- End Links -->

            Since triplets must sum up to the target value, we can try the hash table approach from the [Two Sum] solution. This
            approach won't work, however, if the sum is not necessarily equal to the target, like in [3Sum Smaller] and [3Sum Closest]

            We move our pivot element `nums[i]` and analyze elements to its right. We find all pairs whose sum is equal `-nums[i]` using the
            [Two Sum: One-pass Hash Table] Approach, so that the sum of the pivot element (`nums[i]`) and the pair (`-nums[i]`) is equal to zero.

            To do that, we process each element `nums[j]` to the right of the pivot, and check whether a complement `-nums[i] - nums[j]` is already
            in the hashset. If it is, we found a triplet. Then, we add `nums[j]` to the hashset, so it can be used as a complement from that point on.

            Like in the `three_sum_with_sort` approach, we will also sort the array so we can skip repeated values.


        # Complexity Analysis

            - Time Complexity:
                - O(n^2). `two_sum_ii` is `O(n)` and we call it `n` times
                - Sorting the array takes `O(n log_n)` so overall complexity is `O(n log_n + n^2)`.
                  This is asymptotically equivalent to `O(n^2)`

            - Space Complexity:
                - O(n) for the hashset
        """
        res = []

        # sort the input array `nums`
        nums.sort()
        # iterate through the array
        for i in range(len(nums)):
            current = nums[i]
            prev = nums[i - 1] if i != 0 else None

            # if current value is greater than zero :: break from the loop. remaining values cannot sum to zero
            if current > 0:
                break

            # else :: call `two_sum` for the current position
            if i == 0 or nums[i] != nums[i - 1]:
                self.util_two_sum(nums, i, res)

            # if the current value is the same as the previous :: skip it

        return res

    def util_two_sum(self, nums, i, res):
        visited = set()
        j = i + 1
        # for each index j > i in array
        while j < len(nums):
            # compute `complement`
            complement = -nums[i] - nums[j]
            # if the complement exists in visited, we found a triplet
            if complement in visited:
                # add valid triplet to result
                res.append([nums[i], nums[j], complement])
                # increment j until we're on the last occurrence of possible duplicates
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1

            # add j to the set of visited
            visited.add(nums[j])
            # increment j to move to next
            j += 1

        # no return necessary, we're modifying `res` directly

    def three_sum_no_sort(self, nums):
        """
        # Description

            What if you cannot modify the input array, and you want to avoid copying it due to memory constraints?

            We can modify the `three_sum_hash_set` approach to work with an unsorted array. We can put a combination of three values into a hashset to avoid duplicates
            Values in a combination should be ordered (e.g., ascending). Otherwise we can have results with the same values in the different positions.

        # Complexity Analysis

            - Time Complexity:
                - O(n^2). We have outer and inner loops, each going through `n` elements.
                - While the asymptotic complexity is the same, this algorithm is noticeably slower than the previous approach. Lookups in a hashset, though requiring constant
                  time, are expensive compared to the direct memory access.
            - Space Complexity:
                - O(n) for the hashset/hashmap
                - For the purpose of complexity analysis, we ignore the memory required for the output. However, in this approach we also store output in the hashset for de-duplication.
                  In the worst case, there could be O(n^2) triplets in the output.
                  For example:`[-k, -k + 1, ..., -1, 0, 1, ... k - 1, k]`
                  Adding a new number to this sequence will produce `n / 3` new triplets
        """

        res = set()
        dups = set()

        visited = {}
        for i, v1 in enumerate(nums):
            if v1 not in dups:
                dups.add(v1)
                for v2 in nums[i+1:]:
                    complement = -v1 - v2
                    if complement in visited and visited[complement] == i:
                        # order valid triplet in ascending order
                        sorted_entry = tuple(sorted((v1, v2, complement)))
                        # and add it to the result
                        res.add(sorted_entry)

                    visited[v2] = i
        return res

    def three_sum_with_sort(self, nums):
        """
        # Complexity Analysis

            - Time Complexity:
                - O(n^2). `two_sum_ii` is `O(n)` and we call it `n` times
                - Sorting the array takes `O(n log_n)` so overall complexity is `O(n log_n + n^2)`.
                  This is asymptotically equivalent to `O(n^2)`

            - Space Complexity:
                - from `O(log_n)` to `O(n)`, depending on the implementation of the sorting algorithm. For the purpose of complexity analysis,
                  we ignore the memory required for the output
        """
        # sort array first
        nums.sort()

        res = []

        # iterate through the array
        for i in range(len(nums)):
            # if current value is greater than zero, break from loop.
            # remaining values cannot sum to zero
            if nums[i] > 0:
                break

            # if current value is first in line or different than its previous element
            # call `two_sum_ii` for the current position `i`
            if i == 0 or nums[i - 1] != nums[i]:
                self.util_two_sum_ii(nums, i, res)

            # if the current value is the same as before, skip it

        return res

    def util_two_sum_ii(self, nums, i, res):
        """
        a `two_sum` function used as a utility in `three_sum_with_sort`
        """
        lo = i + 1
        hi = len(nums) - 1

        while lo < hi:
            a, b, c = nums[i], nums[lo], nums[hi]
            sum_ = a + b + c

            # if sum < 0, increment low
            if sum_ < 0:
                lo += 1

            # if sum is greater than zero, decrement hi
            elif sum_ > 0:
                hi -= 1

            # otherwise, sum == 0 and we've found a valid triplet
            else:
                # add it to the result
                res.append([a, b, c])
                # decrement lo
                lo += 1
                # increment hi
                hi -= 1
                # increment lo until we've passed all triplets
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1

        # no return necessary, we're modifying `res` directly

    def three_sum_brute_force(self, nums):
        len_nums = len(nums)

        valid_triplets = set()

        for i in range(len_nums):
            for j in range(i+1, len_nums):
                for k in range(j+1, len_nums):
                    if i != j and i != k and j != k and (nums[i] + nums[j] + nums[k]) == 0:
                        tup = tuple(sorted([nums[i], nums[j], nums[k]]))
                        valid_triplets.add(tup)

        s = [list(tup) for tup in valid_triplets]
        s.sort(key=lambda tup: (tup[0], tup[1], tup[2]))

        return s


class Test(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        solution = Solution()
        self.fn = solution.three_sum_hash_set

    def assert_list_eq_unsorted(self, a, b):
        for inner in a:
            inner.sort()
        for inner in b:
            inner.sort()
        a.sort()
        b.sort()

        self.assertListEqual(a, b)

    def test_001(self):
        self.assert_list_eq_unsorted(
            [[-1, -1, 2], [-1, 0, 1]],
            self.fn([-1, 0, 1, 2, -1, -4])
        )


if __name__ == "__main__":
    unittest.main()
