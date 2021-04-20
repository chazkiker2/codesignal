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
        "right": (i, j + 1),
        "down_right": (i + 1, j + 1),
        "down": (i + 1, j),
        "down_left": (i + 1, j + 1),
        "left": (i, j - 1),
    }


def generate_successor(current_gen):
    # current generation given as argument
    M = len(current_gen)
    N = len(current_gen[0])
    # the successor generation
    # two-dimensional with the same dimensions as `current_gen` array
    # but fill every slot with `None`
    successor_gen = [
        [-1 for _ in range(len(current_gen[i]))]
        for i in range(len(current_gen))
    ]

    #  # non-comprehension version of the line above:
    #  successor_gen = [ [None] * len(current_gen[0]) ] * len(current_gen)

    for i in range(len(current_gen)):
        for j in range(len(current_gen[i])):
            # (i, j) represent our current cell coordinates
            is_alive = current_gen[i][j] != 0
            num_live_neighbors = 0
            for direction, neighbor_coords in get_neighbor_coords(i, j).items():
                ni, nj = neighbor_coords
                ni %= M
                nj %= N
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

    return successor_gen


def make_zilch_array(m, n):
    return [[0 for _ in range(m)] for _ in range(n)]


class Generation(list):
    def __init__(self, *args, **kwargs):
        super(Generation, self).__init__(*args, **kwargs)
        self.current_gen = self.copy()

    def __str__(self):
        return "\n" + "\n".join("\t".join(str(el) for el in sub_array) for sub_array in self)

    def has_life(self):
        for sub_array in self:
            if 1 in sub_array:
                return True
        return False

    # @staticmethod
    def get_neighbor_coords(self, i, j):
        M = len(self.current_gen)
        N = len(self.current_gen[0])

        original = {
            "up_left": (i - 1, j - 1),
            "up": (i - 1, j),
            "up_right": (i - 1, j + 1),
            "right": (i, j + 1),
            "down_right": (i + 1, j + 1),
            "down": (i + 1, j),
            "down_left": (i + 1, j + 1),
            "left": (i, j - 1),
        }

        return {k: (coords[0] % M, coords[1] % N) for k, coords in original.items()}

    def count_live_neighbors(self, i, j):
        # print(f"{self.current_gen}, {self}")
        M = len(self.current_gen)
        N = len(self.current_gen[0])
        num_live_neighbors = 0
        visited = set()
        neighbors = self.get_neighbor_coords(i, j)
        # neighbors = [(ni, nj) for ni, nj in .values()]
        # for direction, neighbor_coords in self.get_neighbor_coords(i, j).items():
        for ni, nj in neighbors.values():
            # ni, nj = neighbor_coords
            ni %= M
            nj %= N
            stup = (ni, nj)
            # and stup not in visited:
            if self[ni][nj] != 0:
                visited.add(stup)
                # print(f"{ni=}, {nj=}")
                num_live_neighbors += 1

        return num_live_neighbors

    def generate_successor(self):
        self.current_gen = self.copy()
        current_gen = self.current_gen
        # current generation given as argument
        M = len(current_gen)
        N = len(current_gen[0])

        for i in range(len(current_gen)):
            for j in range(len(current_gen[i])):
                # (i, j) represent our current cell coordinates
                is_alive = current_gen[i][j] != 0
                num_live_neighbors = 0
                for direction, neighbor_coords in self.get_neighbor_coords(i, j).items():
                    ni, nj = neighbor_coords
                    ni %= M
                    nj %= N
                    if current_gen[ni][nj] != 0:
                        num_live_neighbors += 1

                has_two = num_live_neighbors == 2
                has_three = num_live_neighbors == 3

                # 1. Any live cell with two or three live neighbors survives.
                if is_alive and (has_two or has_three):
                    self[i][j] = 1
                # 2. Any dead cell with three live neighbors becomes a live cell.
                elif (not is_alive) and has_three:
                    self[i][j] = 1
                # 3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
                else:
                    self[i][j] = 0

    def live(self):
        print(f"SEED GENERATION {self}")

        last_self = self.copy()
        count_reps = 1
        frame_count = 1
        stuck = False

        while self.has_life():
            # print(f"LAST GENERATION {self}")
            self.generate_successor()
            print(f"GENERATION {frame_count} {self}")

            if last_self == self:
                count_reps += 1
            else:
                count_reps = 0

            last_self = self.copy()
            frame_count += 1

            if count_reps == 4:
                stuck = True
                break

        if stuck:
            print(f"\nSTUCK AT THIS FRAME{current_generation}")
        else:
            print(f"\nNO LIFE TO CONTINUE\n{current_generation}")


if __name__ == "__main__":
    # some initial pattern to kick off the Game
    seed = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 1],
    ]
    # 0, 0, 1,
    # 0, 1, 1,
    # 0, 0, 1,
    #
    # 0,
    #

    current_generation = Generation(seed)
    current_generation.live()

    # while current_generation.has_life():
    #     new_generation = Generation(generate_successor(current_generation))
    #     print(current_generation)
    #     print(new_generation)
    #     current_generation = new_generation
    # else:
    #     print(f"\nNO LIFE TO CONTINUE\n{current_generation}")
