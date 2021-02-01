"""
given a matrix that is 4 rows by 4*n columns, each 4x4 grid has numbers 1–16 with one index = "?"

for the given matrix, return the parent matrix with each 4x4 completed

test-case 1:
matrix1 = [
    ['1', '2', '3', '4']
    ['5', '6', '7', '8']
    ['9', '10', '11', '12']
    ['13', '14', '15', '?']
]
resolve_matrix(matrix1) # -> [
    ['1', '2', '3', '4']
    ['5', '6', '7', '8']
    ['9', '10', '11', '12']
    ['13', '14', '15', '16']
]


test-case 2:
matrix2 = [
    ['1', '2', '3', '4', '5', '6', '7', '8']
    ['5', '6', '7', '8', '9', '10', '11', '12']
    ['9', '10', '11', '12', '13', '14', '15', '16']
    ['13', '14', '15', '?', '1', '2', '3', '?']
]
"""


def resolve_matrix(matrix):
    num_tables = len(matrix[0]) // 4
    tables = {i: [['0'] * 4] * 4 for i in range(num_tables)}
    print(f"num_tables={num_tables}, tables={tables}")
    count = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (col % 4) == 0:
                count = (count + 1) % num_tables

            print(f"row={row}, col={col}, count={count}, el={matrix[row][col]}")
            # print(f"tables[{count}][{row}][{col % 4}]={tables[count][row][col % 4]}")
            tables[count][row][(col - 1) % 4] = matrix[row][col]

            # try:
            #     num_int = int(matrix[row][col])
            #     tables[count][row][col % 4] = num_int
            # except ValueError:

    print(tables)
    return tables

if __name__ == '__main__':
    # driver code:
    matrix1 = [
        ['1', '2', '3', '4'],
        ['5', '6', '7', '8'],
        ['9', '10', '11', '12'],
        ['13', '14', '15', '?']
    ]
    print(resolve_matrix(matrix1))
    # -> [
    #     ['1', '2', '3', '4']
    #     ['5', '6', '7', '8']
    #     ['9', '10', '11', '12']
    #     ['13', '14', '15', '16']
    # ]
    # matrix2 = [
    #     ['1', '2', '3', '4', '5', '6', '7', '8'],
    #     ['5', '6', '7', '8', '9', '10', '11', '12'],
    #     ['9', '10', '11', '12', '13', '14', '15', '16'],
    #     ['13', '14', '15', '?', '1', '2', '3', '?']
    # ]
    # print(resolve_matrix(matrix2))
    # # -> [
    # #     ['1', '2', '3', '4', '5', '6', '7', '8'],
    # #     ['5', '6', '7', '8', '9', '10', '11', '12'],
    # #     ['9', '10', '11', '12', '13', '14', '15', '16'],
    # #     ['13', '14', '15', '?', '1', '2', '3', '?']
    # # ]
