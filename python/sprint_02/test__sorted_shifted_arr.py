import unittest
from search_sorted_shifted_arr import search_sorted_shifted_arr


class MyTestCase(unittest.TestCase):

    def test_search_with_unshifted_arr(self):
        search_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(10):
            res = search_sorted_shifted_arr(search_arr, i)
            self.assertEqual(res, i)

    def test_search_with_unshifted_arr_2(self):
        search_arr = [5, 8, 10, 31, 54, 81]
        for i, el in enumerate(search_arr):
            res = search_sorted_shifted_arr(search_arr, el)
            self.assertEqual(res, i)

    def test_search_with_shifted_arr(self):
        shifted_arr = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]

        for i, el in enumerate(shifted_arr):
            res = search_sorted_shifted_arr(shifted_arr, el)
            self.assertEqual(res, i)

    def test_search_with_shifted_arr_2(self):
        shifted_arr = [31, 54, 81, 5, 8, 10]

        for i, el in enumerate(shifted_arr):
            res = search_sorted_shifted_arr(shifted_arr, el)
            self.assertEqual(res, i)

    def test_search_with_unshifted_large(self):
        fifty_n = [i for i in range(51)]
        hundred_n = [i for i in range(101)]
        five_hundo_n = [i for i in range(501)]
        thundo = [i for i in range(1001)]
        four_thundo = [i for i in range(4000)]
        twenty_thundo = [i for i in range(20000)]

        self.assertEqual(search_sorted_shifted_arr(fifty_n, 32), 32)
        self.assertEqual(search_sorted_shifted_arr(fifty_n, 25), 25)
        self.assertEqual(search_sorted_shifted_arr(fifty_n, 2), 2)
        self.assertEqual(search_sorted_shifted_arr(fifty_n, 51), -1)
        self.assertEqual(search_sorted_shifted_arr(hundred_n, 32), 32)
        self.assertEqual(search_sorted_shifted_arr(hundred_n, 90), 90)
        self.assertEqual(search_sorted_shifted_arr(hundred_n, 101), -1)
        self.assertEqual(search_sorted_shifted_arr(five_hundo_n, 500), 500)
        self.assertEqual(search_sorted_shifted_arr(five_hundo_n, 501), -1)
        self.assertEqual(search_sorted_shifted_arr(thundo, 943), 943)
        self.assertEqual(search_sorted_shifted_arr(four_thundo, 3241), 3241)
        self.assertEqual(search_sorted_shifted_arr(twenty_thundo, 19562), 19562)

    @unittest.skip
    def test_search_with_unshifted_huge(self):
        lotta_digits = [i for i in range(
            1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527)]
        self.assertEqual(search_sorted_shifted_arr(lotta_digits, 500), 500)


if __name__ == '__main__':
    unittest.main()
