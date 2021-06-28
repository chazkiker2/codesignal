"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.



Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:

Input: s = "azxxzy"
Output: "ay"


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""
import unittest
import test_util


class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr = [c for c in s]

        popping = True
        while popping:
            popped = False
            for i in range(len(arr)-1):

                if i+1 < len(arr) and arr[i] == arr[i+1]:
                    arr.pop(i)
                    arr.pop(i)
                    popped = True

            popping = popped

        return ''.join(arr)


class Test(unittest.TestCase):
    def test_001(self):
        self.assertEqual("ca", self.fn("abbaca"))

    def test_002(self):
        self.assertEqual("ay", self.fn("azxxzy"))


if __name__ == "__main__":
    test_util.AbstractSuite(Test, [Solution().removeDuplicates]).run()
