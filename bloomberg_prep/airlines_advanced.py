"""

# Airlines Prompt

Plane reservation processing.

## DESCRIPTION

A family with given number of members (`num_family_members`) wants to reserve their seats on their flight.

The plane they are boarding has `num_rows` rows—each row containing `num_seats_per_aisle` seats between each aisle break.

Each row is labeled "A" through `end_letter`, where `end_letter` is a valid uppercase letter between A and Z.

The family would all like to sit directly next to each other, not even across aisles if possible (but they're flexible if need be!)

Given an input-string with each currently reserved seat separated by a space (`reserved_seats`), find (1) all possible seats
for the family to sit next to each other without crossing an aisle, and (2) all "not-preferable" options where the family would
be sitting across the aisle. Sitting in different rows is not an option.

Return a tuple of length 2 (`list_one`, `list_two`) where `list_one` is every possible configuration for the family to
all sit next to each other without crossing aisles. And `list_two` is every other configuration, where the family WOULD all
sit next to each other without crossing aisles.

## INPUT

- `num_rows` rows of seats — number of rows in the airplane
- `num_aisle_breaks` number of aisles in each row
- `end_letter` — each row has seats labeled A to `end_letter` (i.e., `K`... each row would have seats labeled A through K)
- `num_family_members`: an int representing the number of people in the family (i.e., `3`)
- `reserved_seats`: a space-separated string where each value is a reserved seat (i.e., `"1A 2B 4G"`)

## OUTPUT

Return a tuple of length 2 (`list_one`, `list_two`) where `list_one` is every possible configuration for the family to
all sit next to each other without crossing aisles. And `list_two` is every other configuration, where the family WOULD all
sit next to each other without crossing aisles.

## Examples

1. EASY
    input:
        - num_rows=4,
        - num_aisle_breaks=0,
        - end_letter="K",
        - num_family_members=3,
        - reserved_seats="1A 2B 4G"
    example call:  airline_seat_booking(4, 0, "K", 3, "1A 2B 4G")
    expected output:
        (
            # not across aisle
            [
                ['1B', '1C', '1D'], ['1C', '1D', '1E'], ['1D', '1E', '1F'], ['1E', '1F', '1G'], ['1F', '1G', '1H'], ['1G', '1H', '1I'], ['1H', '1I', '1J'], ['1I', '1J', '1K'],
                ['2C', '2D', '2E'], ['2D', '2E', '2F'], ['2E', '2F', '2G'], ['2F', '2G', '2H'], ['2G', '2H', '2I'], ['2H', '2I', '2J'], ['2I', '2J', '2K'],
                ['3B', '3C', '3D'], ['3C', '3D', '3E'], ['3D', '3E', '3F'], ['3E', '3F', '3G'], ['3F', '3G', '3H'], ['3G', '3H', '3I'], ['3H', '3I', '3J'], ['3I', '3J', '3K'],
                ['4B', '4C', '4D'], ['4C', '4D', '4E'], ['4D', '4E', '4F'], ['4H', '4I', '4J'], ['4I', '4J', '4K']
            ],

            # across aisle
            []
        )
3. HARDER
    input:
        - num_rows=4
        - num_aisle_breaks=3
        - end_letter="R"
        - num_family_members=6,
        - reserved_seats=""

    example_call=book_seats(4, 3, "R", 6, "")

    expected output:



"""

import unittest

ASCII_LOWER = "abcdefghijklmnopqrstuvwxyz"
ascii_reverse_map = {c: i for i, c in enumerate(ASCII_LOWER)}

lower_range = ord("a")


# upper_range = ord(ASCII_LOWER[len(ASCII_LOWER) - 1])

# 1 2 3      4 5 6       7 8 9       10 11 12        13 14 15       16 17 18
# 1 2 3 4 5 6        7 8 9 10 11 12      13 14 15 16 17 18
class AlphabetUtils:
    def __init__(self, ending_letter):
        self.lower_range = ord("a")
        self.upper_range = ord(ending_letter.lower())
        self.num_col = ascii_reverse_map[ending_letter.lower()] + 1
        self.ascii_lower = "".join(ASCII_LOWER[i] for i in range(self.num_col))
        self.ascii_reverse = {c: i for i, c in enumerate(self.ascii_lower)}


def book_seats(num_rows, num_aisle_breaks, end_letter, num_family_members, reserved_seats):
    alpha = AlphabetUtils(end_letter)

    seats = [
        [0 for _ in range(alpha.num_col + 1)]
        for _ in range(num_rows)
    ]

    options = []
    alt_options = []
    k = num_family_members

    for reserved_seat in reserved_seats.split():
        reserved_seat = reserved_seat.lower()
        idx_switch = -1

        for i, c in enumerate(reserved_seat):
            # if the current character is a letter
            if lower_range <= ord(c) <= alpha.upper_range:
                idx_switch = i
                break

        if idx_switch < 0:
            raise ValueError(f"Invalid input could not parse {reserved_seat}")

        # mark the seat as reserved
        row = int(reserved_seat[0:idx_switch])
        seat = reserved_seat[idx_switch:]
        seats[row - 1][alpha.ascii_reverse[seat]] = 1

    for row_number, seat_section in enumerate(seats):
        n = len(seat_section)
        if n < k:
            raise ValueError("family size may not be larger than len(seat_section)")
        window_sum = sum(seat_section[:k])
        for i in range(n - k):
            if window_sum == 0:
                start_seat = i
                end_seat = i + k
                this_entry = []
                is_cross_aisle = False
                for s in range(start_seat, end_seat):
                    entry = f"{row_number + 1}{alpha.ascii_lower[s].upper()}"
                    this_entry.append(entry)
                    if num_aisle_breaks != 0 and \
                            s != 0 and \
                            (s % (alpha.num_col / (num_aisle_breaks + 1))) == 0 and \
                            s != start_seat and \
                            s != end_seat and \
                            s != n:
                        print(f"{s=} {entry} {row_number}{start_seat}-{end_seat}")
                        is_cross_aisle = True
                if is_cross_aisle:
                    alt_options.append(this_entry)
                else:
                    options.append(this_entry)

            window_sum = window_sum - seat_section[i] + seat_section[i + k]

    return options, alt_options


class Test001(unittest.TestCase):
    def setUp(self) -> None:
        self.input = (4, 0, "K", 3, "1A 2B 4G")
        self.expected = (
            [
                ['1B', '1C', '1D'], ['1C', '1D', '1E'], ['1D', '1E', '1F'], ['1E', '1F', '1G'], ['1F', '1G', '1H'],
                ['1G', '1H', '1I'], ['1H', '1I', '1J'], ['1I', '1J', '1K'], ['2C', '2D', '2E'], ['2D', '2E', '2F'],
                ['2E', '2F', '2G'], ['2F', '2G', '2H'], ['2G', '2H', '2I'], ['2H', '2I', '2J'], ['2I', '2J', '2K'],
                ['3A', '3B', '3C'], ['3B', '3C', '3D'], ['3C', '3D', '3E'], ['3D', '3E', '3F'], ['3E', '3F', '3G'],
                ['3F', '3G', '3H'], ['3G', '3H', '3I'], ['3H', '3I', '3J'], ['3I', '3J', '3K'], ['4A', '4B', '4C'],
                ['4B', '4C', '4D'], ['4C', '4D', '4E'], ['4D', '4E', '4F'], ['4H', '4I', '4J'], ['4I', '4J', '4K']
            ],
            []
        )

    def test(self):
        self.assertEqual(self.expected, book_seats(*self.input))


class Test002(unittest.TestCase):
    """
    - INPUT:
        - num_rows=4,
        - num_breaks=1,
        - last_letter="H",
        - family_size=3,
        - reserved_seats=1A, 2B, 4G
    - example_call=book_seats(4, 1, "H", 3, "1A 2B 4G")

                A  B  C  D     E  F  G  H
        1       X  .  .  .     .  .  .  .
        2       .  X  .  .     .  .  .  .
        3       .  .  .  .     .  .  .  .
        4       .  .  .  .     .  .  X  .
    """

    def setUp(self) -> None:
        self.input = (4, 1, "H", 3, "1A 2B 4G")
        self.expected = (
            [
                ["1B", "1C", "1D"], ["1E", "1F", "1G"], ["1F", "1G", "1H"],
                ["2E", "2F", "2G"], ["2F", "2G", "2H"],
                ["3A", "3B", "3C"], ["3B", "3C", "3D"], ["3E", "3F", "3G"], ["3F", "3G", "3H"],
                ["4A", "4B", "4C"], ["4B", "4C", "4D"],
            ],
            [
                ["1C", "1D", "1E"], ["1D", "1E", "1F"],
                ["2C", "2D", "2E"], ["2D", "2E", "2F"],
                ["3C", "3D", "3E"], ["3D", "3E", "3F"],
                ["4C", "4D", "4E"], ["4D", "4E", "4F"],
            ],
        )

    def test(self):
        self.assertEqual(self.expected, book_seats(*self.input))


class Test003(unittest.TestCase):
    """
    - num_rows = 4
    - num_aisle_breaks = 3
    - ending_letter = "R"
    - family_size = 6
    - reserved_seats = ""
    """

    def setUp(self) -> None:
        self.input = (4, 3, "R", 6, "")
        self.expected = (
            [
                ['1A', '1B', '1C', '1D', '1E', '1F'], ['1B', '1C', '1D', '1E', '1F', '1G'],
                ['1C', '1D', '1E', '1F', '1G', '1H'], ['1D', '1E', '1F', '1G', '1H', '1I'],
                ['1J', '1K', '1L', '1M', '1N', '1O'], ['1K', '1L', '1M', '1N', '1O', '1P'],
                ['1L', '1M', '1N', '1O', '1P', '1Q'], ['1M', '1N', '1O', '1P', '1Q', '1R'],
                ['2A', '2B', '2C', '2D', '2E', '2F'], ['2B', '2C', '2D', '2E', '2F', '2G'],
                ['2C', '2D', '2E', '2F', '2G', '2H'], ['2D', '2E', '2F', '2G', '2H', '2I'],
                ['2J', '2K', '2L', '2M', '2N', '2O'], ['2K', '2L', '2M', '2N', '2O', '2P'],
                ['2L', '2M', '2N', '2O', '2P', '2Q'], ['2M', '2N', '2O', '2P', '2Q', '2R'],
                ['3A', '3B', '3C', '3D', '3E', '3F'], ['3B', '3C', '3D', '3E', '3F', '3G'],
                ['3C', '3D', '3E', '3F', '3G', '3H'], ['3D', '3E', '3F', '3G', '3H', '3I'],
                ['3J', '3K', '3L', '3M', '3N', '3O'], ['3K', '3L', '3M', '3N', '3O', '3P'],
                ['3L', '3M', '3N', '3O', '3P', '3Q'], ['3M', '3N', '3O', '3P', '3Q', '3R'],
                ['4A', '4B', '4C', '4D', '4E', '4F'], ['4B', '4C', '4D', '4E', '4F', '4G'],
                ['4C', '4D', '4E', '4F', '4G', '4H'], ['4D', '4E', '4F', '4G', '4H', '4I'],
                ['4J', '4K', '4L', '4M', '4N', '4O'], ['4K', '4L', '4M', '4N', '4O', '4P'],
                ['4L', '4M', '4N', '4O', '4P', '4Q'], ['4M', '4N', '4O', '4P', '4Q', '4R']
            ],
            [
                ['1E', '1F', '1G', '1H', '1I', '1J'], ['1F', '1G', '1H', '1I', '1J', '1K'],
                ['1G', '1H', '1I', '1J', '1K', '1L'], ['1H', '1I', '1J', '1K', '1L', '1M'],
                ['1I', '1J', '1K', '1L', '1M', '1N'], ['2E', '2F', '2G', '2H', '2I', '2J'],
                ['2F', '2G', '2H', '2I', '2J', '2K'], ['2G', '2H', '2I', '2J', '2K', '2L'],
                ['2H', '2I', '2J', '2K', '2L', '2M'], ['2I', '2J', '2K', '2L', '2M', '2N'],
                ['3E', '3F', '3G', '3H', '3I', '3J'], ['3F', '3G', '3H', '3I', '3J', '3K'],
                ['3G', '3H', '3I', '3J', '3K', '3L'], ['3H', '3I', '3J', '3K', '3L', '3M'],
                ['3I', '3J', '3K', '3L', '3M', '3N'], ['4E', '4F', '4G', '4H', '4I', '4J'],
                ['4F', '4G', '4H', '4I', '4J', '4K'], ['4G', '4H', '4I', '4J', '4K', '4L'],
                ['4H', '4I', '4J', '4K', '4L', '4M'], ['4I', '4J', '4K', '4L', '4M', '4N']
            ]
        )

    def test(self):
        self.assertEqual(self.expected, book_seats(*self.input))


if __name__ == '__main__':
    unittest.main()
