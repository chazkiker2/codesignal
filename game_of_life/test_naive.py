import unittest
from naive import Generation

SEED = "seed"
FRAMES = "FRAMES"
NBRS = "neighbors"
# (0, 0): D, 4, D
# (1, 0): D, 4, D
# 0     0       1
# 0     1       1
# 0     0       1
#
# [4, 4, 3],
# [4, 3, 3],
# [4, 4, 3],
#
# 0,4,0   0,4     1,3
# 0,4   1,3     1,3
# 0,4   0,4     1,3


test_cases = {
    1: {
        SEED: [
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 1],
        ],
        NBRS: [
            [4, 4, 3],
            [4, 3, 3],
            [4, 4, 3],
        ],
        FRAMES: {
            0: [
                [0, 0, 1],
                [0, 1, 1],
                [0, 0, 1],
            ],
        }
    },
    2: {
        SEED: [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        NBRS: [
            [0, 1, 1, 1, 0],
            [0, 2, 1, 2, 0],
            [0, 3, 2, 3, 0],
            [0, 2, 1, 2, 0],
            [0, 1, 1, 1, 0],
        ],
        FRAMES: {
            0: [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            1: [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        }
    }
}

TEST_CASE = test_cases[2]


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test_case = TEST_CASE
        self.gen = Generation(self.test_case[SEED])

    def test_get_neighbors(self):
        M = len(self.gen) - 1
        N = len(self.gen[0]) - 1

        expected = {
            'up_left': (M, N),
            'up': (M, 0),
            'up_right': (M, 1),
            'right': (0, 1),
            'down_right': (1, 1),
            'down': (1, 0),
            'down_left': (1, N),
            'left': (0, N)
        }
        actual = self.gen.get_neighbor_coords(0, 0)

        self.assertEqual(expected, actual)

    def make_tester_count_neighbors(self, i, j):
        actual = self.gen.count_live_neighbors(i, j)
        expected = self.test_case[NBRS][i][j]
        msg = f"coords=({i}, {j}) {expected=}, {actual=}\n" \
              f"{self.gen}\n"
        self.assertEqual(expected, actual, msg)

    def test_count_all_neighbors(self):
        for ti in range(len(self.gen)):
            for tj in range(len(self.gen[ti])):
                self.make_tester_count_neighbors(ti, tj)

    def test_count_neighbors(self):
        self.make_tester_count_neighbors(2, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
