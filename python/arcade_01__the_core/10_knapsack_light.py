"""
# Knapsack Light

## Description

You found two items in a treasure chest! The first item weighs `weight1` and is worth `value1`, and the
second item weighs `weight2` and is worth `value2`. What is the total maximum value of the items you can take with
you, assuming that your max weight capacity is `maxW` and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two
first items or two second items.

## Example

-  Example 1
  - input: `value1 = 10`, `weight1 = 5`, `value2 = 6`, `weight2 = 4`, and `maxW = 8`, the
  - output should be `knapsackLight(10, 5, 6, 4, 8) = 10.`
  - explanation: You can only carry the first item.
- Example 2
  - input: For `value1 = 10`, `weight1 = 5`, `value2 = 6`, `weight2 = 4`, and `maxW = 9`,
  - output: `knapsackLight(10, 5, 6, 4, 9) = 16.`
  - description: You're strong enough to take both of the items with you.
- Example 3
  - input: `value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6`
  - output: `knapsackLight(5, 3, 7, 4, 6) = 7`
  - explanation: You can't take both items, but you can take any of them.

## Input/Output

- [execution time limit] 4 seconds (py3)
- [input] integer `value1`
  - Guaranteed constraints: `2 ≤ value1 ≤ 20`.
- [input] integer `weight1`
  - Guaranteed constraints: `2 ≤ weight1 ≤ 10`.
- [input] integer `value2`
  - Guaranteed constraints: `2 ≤ value2 ≤ 20`.
- [input] integer `weight2`
  - Guaranteed constraints: `2 ≤ weight2 ≤ 10`.
- [input] integer `maxW`
  - Guaranteed constraints: `1 ≤ maxW ≤ 20`.
- [output] integer
"""


def knapsack_light(value1, weight1, value2, weight2, max_w):
    is_w1_in_range = weight1 <= max_w
    is_w2_in_range = weight2 <= max_w
    is_both_in_range = max_w >= weight1 + weight2

    is_v1_ge = value1 >= value2

    if not is_w1_in_range and not is_w2_in_range:
        return 0
    if is_both_in_range:
        return value1 + value2
    else:
        return value1 \
            if is_v1_ge and is_w1_in_range \
            else value2


def knapsack_light_better(v1, w1, v2, w2, max_w):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        return max(value1 if weight1 <= maxW else 0, value2 if weight2 <= maxW else 0)


if __name__ == '__main__':
    assert knapsack_light(10, 5, 6, 4, 8) == 10
    assert knapsack_light(10, 5, 6, 4, 9) == 16
    assert knapsack_light(5, 3, 7, 4, 6) == 7
