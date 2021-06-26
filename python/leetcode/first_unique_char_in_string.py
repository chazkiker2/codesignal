from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counted = Counter(s)

        for i, c in enumerate(s):
            if counted[c] == 1:
                return i

        return -1
