import unittest


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        INPUT:
        matrix = [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ]
        Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

        # across
        matrix[0][0],
        matrix[0][1],
        matrix[0][2],

        # down
        matrix[1][2],
        matrix[2][2],

        # left
        matrix[2][1]
        matrix[2][0]

        # up
        matrix[1][0]

        # across
        matrix[1][1]

        # --- finished


        """
        # starting row index
        start_row_index = 0
        # starting column index
        start_col_index = 0
        # ending row index
        end_row_index = len(matrix)
        # ending column index
        end_col_index = len(matrix[0])

        # flattened, spiral-ordered matrix
        spiral_matrix = []

        while start_row_index < end_row_index and start_col_index < end_col_index:
            # across (right)
            for i in range(start_col_index, end_col_index):
                spiral_matrix.append(matrix[start_row_index][i])
            start_row_index += 1

            # down
            for i in range(start_row_index, end_row_index):
                spiral_matrix.append(matrix[i][end_col_index - 1])
            end_col_index -= 1

            # left
            if (start_row_index < end_row_index):
                for i in range(end_col_index-1, (start_col_index-1), -1):
                    spiral_matrix.append(matrix[end_row_index-1][i])
                end_row_index -= 1

            # up
            if (start_col_index < end_col_index):
                for i in range(end_row_index-1, start_row_index-1, -1):
                    spiral_matrix.append(matrix[i][start_col_index])
                start_col_index += 1

        return spiral_matrix


class Test(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.fn = Solution().spiralOrder

    def test_001(self):
        self.assertEqual(
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
            self.fn([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        )


if __name__ == "__main__":
    unittest.main()
