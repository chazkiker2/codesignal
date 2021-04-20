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
    2: {}
}

DEFAULT_SEED = test_cases[1][SEED]


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.gen = Generation(DEFAULT_SEED)

    def test_get_neighbors(self):
        expected = {
            'up_left': (-1, -1),
            'up': (-1, 0),
            'up_right': (-1, 1),
            'right': (0, 1),
            'down_right': (1, 1),
            'down': (1, 0),
            'down_left': (1, 1),
            'left': (0, -1)
        }
        actual = self.gen.get_neighbor_coords(0, 0)

        self.assertEqual(actual, expected)

    def test_count_neighbors_00(self):

        dictx = {
            (0, 0): 3,
            (0, 1): 4,
            (0, 2): 3,
            (1, 0): 4,
            (1, 1): 3,
            (1, 2): 3,
        }
        for ti in range(len(self.gen)):
            for tj in range(len(self.gen[ti])):
                actual = self.gen.count_live_neighbors(ti, tj)
                expected = test_cases[1][NBRS][ti][tj]
                msg = f"coords=({ti}, {tj}) {expected=}, {actual=}\n" \
                      f"{self.gen=}"
                self.assertEqual(expected, actual, msg)
        # for coords, expected in dictx.items():
        #     actual = self.gen.count_live_neighbors(*coords)
        #     msg = f"{coords=} {expected=}, {actual=}\n" \
        #           f"{self.gen=}"
        #     self.assertEqual(expected, actual, msg)

        # expected = 3
        # actual = self.gen.count_live_neighbors(0, 0)
        # self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
