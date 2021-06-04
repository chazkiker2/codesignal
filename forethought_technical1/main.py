# list of positive ints
# and a target int
# goal is to find all pairs in list that add up to the target
# potentially multiple pairs
# no duplicates
# could be unsorted

def find_all_pairs(numbers, target):
    """
    :param numbers: list of positive integers — no duplicates
    :param target: integer, target sum
    :return: all pairs that sum to target
    """

    # may want to sort numbers
    # some set to keep all of our pairs in
    #
    # iterate through all of our numbers and essentially
    # O(n^2) -- nested for loop comparing our current_number to every other number
    # current_number, to every following index
    # if you hit a pair, add it to the set

    # sorted_nums = sorted(numbers)
    visited = set()
    valid_pairs = set()

    for num in numbers:
        possible_match = target - num
        if possible_match in visited:  # faster than O(n)
            valid_pairs.add((possible_match, num))

        visited.add(num)

        # for o_i in range(i+1, len(numbers)):
        #     if num + sorted_nums[o_i] == target:
        #         valid_pairs.add((num, sorted_nums[o_i]))
    return valid_pairs


if __name__ == '__main__':
    expected = find_all_pairs([1, 2, 3, 4, 5], 6)
    print(expected)
