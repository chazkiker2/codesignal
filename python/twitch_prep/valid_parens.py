"""
Given a string `s` containing just the characters
"""
from collections import deque

# def valid_pairs(parens):
    #
    # opposites = {
    #     "(": ")",
    #     "{": "}",
    #     "[": "]",
    # }
    #
    # enders = {
    #     ")": "(",
    #     "}": "{",
    #     "]": "["
    # }
    #
    # expected = deque()
    #
    # s = 0
    # for p in parens:
    #     if p in enders:
    #         if p == expected.pop():
    #             return False
    #     else:
    #         expected.append(opposites[p])
    #
    #     s ^= ord(opposites[p])
    #
    # return s == 0


# if __name__ == '__main__':
#     test_cases = [
#         ["()", True],
#         ["()[]{}", True],
#         ["(]", False]
#     ]
#
#     for test_number, (params, expected) in enumerate(test_cases):
#         received = valid_pairs(params)
#         print(f"{test_number}, valid_pairs({params}): {received=} {expected=} --- pass? {received == expected}")
