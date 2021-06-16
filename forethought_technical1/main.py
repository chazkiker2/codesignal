# list of positive ints
# and a target int
# goal is to find all pairs in list that add up to the target
# potentially multiple pairs
# no duplicates
# could be unsorted

def find_all_pairs(numbers, target):
    visited = set()
    valid_pairs = set()

    for num in numbers:
        possible_match = target - num

        if possible_match in visited:
            valid_pairs.add((possible_match, num))

        visited.add(num)

    return valid_pairs


if __name__ == '__main__':
    expected = find_all_pairs([1, 2, 3, 4, 5], 6)
    print(expected)
