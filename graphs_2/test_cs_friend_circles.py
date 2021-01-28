import unittest

from cs_friend_circles import friend_circles


class MyTestCase(unittest.TestCase):
    def test_case_01(self):
        result = friend_circles([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
