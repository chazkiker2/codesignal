"""
Find all the pairs of two integers in an unsorted array that sum up to a given S.

For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should
return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.

two_int_sum(array, sum_number):

two_int_sum([3, 5, 2, -4, 8, 11], 7) -> [[11, -4], [2, 5]]

sort -> .sort() sorted(array). - comes at cost of time complexity

return_arr [] -> list with every given pair that adds up to 7

"""


def find_all_pairs_best(input_arr, sum_value):
    valid_pairs = []
    visited = set()
    input_arr.sort()

    for el in input_arr:
        diff = sum_value - el
        if diff in input_arr:
            valid_pairs.append([el, diff])

        # if diff == sum_value:


    return valid_pairs


def find_all_pairs(input_arr, sum_target):
    return_list = set()

    for index1 in range(len(input_arr)):
        for index2 in range(index1 + 1, len(input_arr)):
            # if index1 == index2:
            # we will not compare the current number to itself

            if index1 != index2:  # else, we have two different numbers
                num1 = input_arr[index1]
                num2 = input_arr[index2]
                if num1 + num2 == sum_target:
                    return_list.add((num1, num2))

    return list(return_list)


def find_all_pairs_better(input_arr, target_sum, n=None):
    if not n:
        n = len(input_arr)

    valid_pairs = []

    counts_dict = {}

    for i in range(n):
        temp = target_sum - input_arr[i]
        if temp in counts_dict:
            count = counts_dict[temp]
            for j in range(count):
                valid_pairs.append([temp, input_arr[i]])

        if input_arr[i] not in counts_dict:
            counts_dict[input_arr[i]] = 0

        counts_dict[input_arr[i]] += 1

    return valid_pairs


if __name__ == '__main__':
    # test_case_01 = find_all_pairs([3, 5, 2, -4, 8, 11], 7)
    # print(test_case_01)
    # test_case_02 = find_all_pairs_better([3, 5, 2, -4, 8, 11], 7)
    # print(test_case_02)

    test_case_01 = find_all_pairs_best([3, 5, 2, -4, 8, 11], 7)
    print(test_case_01)
