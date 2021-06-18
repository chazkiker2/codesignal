# x, y representation
#
# -1, 1     0, 1      1, 1
# -1, 0,    0, 0      1, 0
# -1, -1    0, -1     1, -1
#
# arr[x][y]
#
# [0][0]    [0][1]    [0][2]
# [1][0]    [1][1]    [1][2]
# [2][0]    [2][1]    [2][2]
#
# arr[i][j]
#
# [i-1][j-1]    [i-1][j  ]    [i-1][j+1]
# [i  ][j-1]    [i=1][j=1]    [i  ][j+1]
# [i+1][j-1]    [i+1][j  ]    [i+1][j+1]

# for any given cell at (i, j), neighbors can be represented like so:
def get_neighbor_coords(i, j):
    return {
        "up_left": (i - 1, j - 1),
        "up": (i - 1, j),
        "up_right": (i - 1, j + 1),
        "next": (i, j + 1),
        "down_right": (i + 1, j + 1),
        "down": (i + 1, j),
        "down_left": (i + 1, j + 1),
        "prev": (i, j - 1),
    }


def generate_successor(current_gen):
    # current generation given as argument

    # the successor generation
    # two-dimensional with the same dimensions as `current_gen` array
    # but fill every slot with `None`
    successor_gen = [
        [None for _ in range(len(current_gen[i]))]
        for i in range(len(current_gen))
    ]

    #  # non-comprehension version of the line above:
    #  successor_gen = [ [None] * len(current_gen[0]) ] * len(current_gen)

    for i in len(current_gen):
        for j in len(current_gen[i]):

            cell_coords = (i, j)

            is_alive = current_gen[i][j]

            num_live_neighbors = 0

            for direction, neighbor_coords in get_neighbor_coords(i, j).items():
                ni, nj = neighbor_coords
                if current_gen[ni][nj] != 0:
                    num_live_neighbors += 1

            has_two = num_live_neighbors == 2
            has_three = num_live_neighbors == 3

            # 1. Any live cell with two or three live neighbors survives.
            if is_alive and (has_two or has_three):
                successor_gen[i][j] = 1
            # 2. Any dead cell with three live neighbors becomes a live cell.
            elif (not is_alive) and has_three:
                successor_gen[i][j] = 1
            # 3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
            else:
                successor_gen[i][j] = 0


if __name__ == "__main__":
    seed = [...]  # some initial pattern to kick off the Game

    current_generation = seed

    while True:
        new_generation = generate_successor(current_generation)
        current_generation = new_generation