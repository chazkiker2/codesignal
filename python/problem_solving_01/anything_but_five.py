"""
Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

Examples:

csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
Notes:

The output can contain the digit 5.
The start number will always be less than the end number (both numbers can also be negative).
"""


def anything_but_five_01(start, end):
    count = 0
    for number in range(start, end + 1):
        if '5' not in str(number):
            count += 1

    return count


def anything_but_five_02(start, end):
    not_fives = [number for number in range(start, end + 1) if "5" not in str(number)]
    return len(not_fives)


if __name__ == '__main__':
    t1m1 = anything_but_five_01(1, 5)
    t1m2 = anything_but_five_02(1, 5)
    print(t1m1)
    print(t1m2)
