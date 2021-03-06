"""
# [Leetcode 13: Roman to Integer]

[Leetcode 13: Roman to Integer]: https://leetcode.com/problems/roman-to-integer/
"""
# from code.test_util import AbstractSuite
import unittest
import code


groups = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}

exc = {
    "I": ["V", "X"],
    "X": ["L", "C"],
    "C": ["D", "M"]
}


def roman_to_int(s: str) -> int:
    total_sum = 0
    i = 0

    while i < len(s):
        c = s[i]
        if c in exc and i < len(s) - 1 and s[i+1] in exc[c]:
            i += 2
            total_sum += groups[s[i+1]] - groups[c]
        else:
            i += 1
            total_sum += groups[c]

    return total_sum

    # for i, c in enumerate(s):
    #     if i in escaped:
    #         continue
    #     if c in exc and i < len(s) - 1 and s[i+1] in exc[c]:
    #         escaped.add(i+1)
    #         total_sum += groups[s[i+1]] - groups[c]
    #     else:
    #         total_sum += groups[c]

    # return total_sum


class Test(unittest.TestCase):
    def test_001(self):
        self.assertEqual(3, self.fn("III"))

    def test_002(self):
        self.assertEqual(4, self.fn("IV"))

    def test_003(self):
        self.assertEqual(9, self.fn("IX"))

    def test_004(self):
        self.assertEqual(58, self.fn("LVIII"))

    def test_005(self):
        self.assertEqual(1994, self.fn("MCMXCIV"))


if __name__ == "__main__":
    print(dir(code))
    print(code.__all__)
    print(code.__package__)
    print(code.__name__)
    # print(code.__spec__)
    # AbstractSuite(Test, [roman_to_int]).run()
