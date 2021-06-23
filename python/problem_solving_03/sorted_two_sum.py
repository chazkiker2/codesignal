"""
Given a sorted array (in ascending order) of integers and a target,
write a function that finds the two integers that add up to the target.

Examples:

csSortedTwoSum([3,8,12,16], 11) -> [0,1]
csSortedTwoSum([3,4,5], 8) -> [0,2]
csSortedTwoSum([0,1], 1) -> [0,1]
Notes:

Each input will have exactly one solution.
You may not use the same element twice.

"""


def sorted_two_sum_01(numbers, target):
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]


def sorted_two_sum_02(numbers, target):
    numbers.sort()
    for i in range(len(numbers)):
        j = i + 1
        if numbers[i] + numbers[j] == target:
            return [i, j]


def sorted_two_sum_seb(numbers, target):
    num_map = {
        number: index
        for index, number in enumerate(numbers)
    }

    for number, index in num_map.items():  # O(n) loop
        diff = target - number
        if diff in num_map:   # O(1) operation
            return [index, num_map[diff]]


def sorted_two_sum_seb_02(numbers, target):
    dict = {}
    for i, v in enumerate(numbers):
        dict[v] = i

    for k, v in dict.items():
        subber = target - k  # this will give us a value in the array...
        if subber in dict:
            r = [v, dict[subber]]
            return r

    return result


if __name__ == '__main__':
    test1_m1 = sorted_two_sum_01([3, 8, 12, 16], 11)  # -> [0, 1]
    test1_m2 = sorted_two_sum_seb([3, 8, 12, 16], 11)  # -> [0, 1]
    print(test1_m1)
    print(test1_m2)

    test2_m1 = sorted_two_sum_seb([3, 4, 5], 8)  # -> [0, 2]
    # test2_m2 = sorted_two_sum_02([3, 4, 5], 8)  # -> [0, 1]
    print(test2_m1)
    # print(test2_m2)
