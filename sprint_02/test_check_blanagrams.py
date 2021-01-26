import unittest
from check_blanagrams import check_blanagrams


class MyTestCase(unittest.TestCase):
    def test_blanagram_true(self):
        self.assertEqual(check_blanagrams("tangram", "anagram"), True)
        self.assertEqual(check_blanagrams("aabbc", "aabbd"), True)
        self.assertEqual(check_blanagrams("racecar", "racxcar"), True)
        self.assertEqual(check_blanagrams("xxxz", "xxxy"), True)
        self.assertEqual(check_blanagrams("aabb", "aaab"), True)

    def test_blanagram_false(self):
        self.assertEqual(check_blanagrams("aaabc", "abbbc"), False)
        self.assertEqual(check_blanagrams("racecar", "racecar"), False)
        self.assertEqual(check_blanagrams("racecar", "racxccr"), False)
        # Counter("aabb", "aaab") -> { a: 5, b: 3} -> len(filtered_dict) == 2 -> True


if __name__ == '__main__':
    unittest.main()

# like aaabc and abbbd would work in his equation but it should fail
