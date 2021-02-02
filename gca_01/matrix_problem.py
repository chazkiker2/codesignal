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
            print(f"row={row}, col={col}, el={matrix[row][col]}")
            print(f"(col//4)={col // 4}")
            print(f"(col%4)={col % 4}")
            print(f"(col-1)%4={(col - 1) % 4}")
            tables[col//4][row][col%4] = matrix[row][col]
            # print(f"tables[{count}][{row}][{col % 4}]={tables[count][row][col % 4]}")
            # tables[col % 4][row][(col - 1) % 4] = matrix[row][col]

            # try:
            #     num_int = int(matrix[row][col])
            #     tables[count][row][col % 4] = num_int
            # except ValueError:

    # print(tables)
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
    expected1 = [
        ['1', '2', '3', '4'],
        ['5', '6', '7', '8'],
        ['9', '10', '11', '12'],
        ['13', '14', '15', '16'],
    ]
    actual1 = resolve_matrix(matrix1)
    print(f"TEST 2: \nactual: {actual1}, \nexpected: {expected1}")
    print(f"\npassed: {actual1 == expected1}")
    matrix2 = [
        ['1', '2', '3', '4', '5', '6', '7', '8'],
        ['5', '6', '7', '8', '9', '10', '11', '12'],
        ['9', '10', '11', '12', '13', '14', '15', '16'],
        ['13', '14', '15', '?', '1', '2', '3', '?'],
    ]
    expected2 = [
        ['1', '2', '3', '4', '5', '6', '7', '8'],
        ['5', '6', '7', '8', '9', '10', '11', '12'],
        ['9', '10', '11', '12', '13', '14', '15', '16'],
        ['13', '14', '15', '16', '1', '2', '3', '16'],
    ]
    actual2 = resolve_matrix(matrix2)
    print(f"\n\n-----TEST 2: \n")
    print(f"actual: {actual2}, \nexpected: {expected2}")
    print(f"\npassed: {actual2 == expected2}")
