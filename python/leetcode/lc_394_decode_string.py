"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"


Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

"""
import unittest
from collections import deque
import test_util
import re


class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = deque()
        string_stack = deque()

        current_string = ""

        k = 0

        valid_letters = (ord("a"), ord("z"))
        valid_digits = (ord("0"), ord("9"))

        def is_digit(ch):
            return valid_digits[0] <= ord(ch) <= valid_letters[1]

        def is_letter(letter):
            return valid_letters[0] <= ord(ch) <= valid_letters[1]

        for ch in s:
            if ch == "[":
                count_stack.append(int(k))
                string_stack.append(current_string)
                current_string = ""
                k = 0

            elif ch == "]":
                decoded_str = string_stack.pop()

                for _ in range(count_stack.pop()):
                    decoded_str += current_string

                current_string = decoded_str

            elif is_digit(ch):
                k = k*10 + int(ch)

            else:
                current_string += ch

        return current_string

        # START, END = '[', ']'

        # new_seq = [False, ""]
        # num_rep = 1
        # # print('[' == "[")
        # for c in s:
        #     if c == START:
        #         new_seq[0] = True
        #     elif c == END:
        #         stack.append((num_rep, new_seq[1]))
        #         # for _ in range(num_rep):
        #         #     stack.append(new_seq[1])
        #         num_rep = 1
        #         new_seq = [False, ""]

        #     elif is_letter(c):
        #         if new_seq[0]:
        #             new_seq[1] += c
        #         else:
        #             stack.append((num_rep, c))
        #             # for _ in range(num_rep):
        #             #     stack.append(c)
        #     else:
        #         num_rep = int(c)
        #         # stack.append(num_rep)
        #         # num_rep = int(c)

        # print(stack)

        # while stack:
        #     num_rep, seq = stack.popleft()
        #     for _ in range(num_rep):
        #         ret += seq

        # return ret


class Test(unittest.TestCase):
    def test_001(self):
        self.assertEqual("aaabcbc", self.fn("3[a]2[bc]"))

    def test_002(self):
        self.assertEqual("accaccacc", self.fn("3[a2[c]]"))

    def test_003(self):
        self.assertEqual("abcabccdcdcdef", self.fn("2[abc]3[cd]ef"))

    def test_004(self):
        self.assertEqual("abccdcdcdxyz", self.fn("abc3[cd]xyz"))


if __name__ == "__main__":
    test_util.run_suite(Test, [Solution().decodeString])
