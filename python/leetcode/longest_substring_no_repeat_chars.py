
"""
Given a string `s`, find the length of the *longest substring* without repeating characters.

# Example 1:

- Input: s = "abcabcbb"
- Output: 3
- Explanation: The answer is "abc", with the length of 3.


# Example 2:

- Input: s = "bbbbb"
- Output: 1
- Explanation: The answer is "b", with the length of 1.

# Example 3:

- Input: s = "pwwkew"
- Output: 3
- Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:

- Input: s = ""
- Output: 0


# Constraints:

- `0 <= s.length <= 5 * 104`
- `s` consists of English letters, digits, symbols and spaces
"""
import unittest


class Solution(object):
    def length_of_longest_sub(self, s):
        # a dict with key value pairs such that
        # key: character -- value: the most recently visited index where we visited the character
        dic = {}
        # the length of the longest substring
        max_len = start = 0

        for current_index, char in enumerate(s):
            if char in dic:
                start = max(start, dic[char] + 1)

            max_len = max(max_len, current_index - start + 1)
            dic[char] = current_index

        return max_len

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0

        for i in range(len(s)):
            count = 0
            visited = set()

            for c in s[i:]:
                if c in visited:
                    break

                count += 1
                visited.add(c)

            max_count = max(count, max_count)

        return max_count


class Test(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        solution = Solution()
        self.fn = solution.length_of_longest_sub

    def test_001(self):
        self.assertEqual(3, self.fn("abcabcbb"))

    def test_002(self):
        self.assertEqual(1, self.fn("bbbbb"))

    def test_003(self):
        self.assertEqual(0, self.fn(""))

    def test_004(self):
        self.assertEqual(3, self.fn("dvdf"))

    def test_005(self):
        self.assertEqual(6, self.fn("asjrgapa"))

    def test_006(self):
        self.assertEqual(3, self.fn("pwwkew"))


if __name__ == "__main__":
    unittest.main()
