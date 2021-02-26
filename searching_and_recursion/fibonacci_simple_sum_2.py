"""
# FIBONACCI SIMPLE SUM 2
#
#
#
For a given positive integer fib_ceil determine if it can be represented
as a sum of two Fibonacci numbers (possibly equal).

Example

For fib_ceil = 1, the output should be
fibonacciSimpleSum2(fib_ceil) = true.

Explanation: 1 = 0 + 1 = F0 + F1.

For fib_ceil = 11, the output should be
fibonacciSimpleSum2(fib_ceil) = true.

Explanation: 11 = 3 + 8 = F4 + F6.

For fib_ceil = 60, the output should be
fibonacciSimpleSum2(fib_ceil) = true.

Explanation: 60 = 5 + 55 = F5 + F10.

For fib_ceil = 66, the output should be
fibonacciSimpleSum2(fib_ceil) = false.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer fib_ceil

Guaranteed constraints:
1 ≤ fib_ceil ≤ 2 · 109.

[output] boolean

true if fib_ceil can be represented as Fi + Fj, false otherwise.
"""
from itertools import combinations


def fibonacci_seq_in_range(fib_ceil):
    fib_nums = [0, 1]

    for i in range(2, fib_ceil + 1):
        new_fib = fib_nums[i - 1] + fib_nums[i - 2]

        fib_nums.append(new_fib)

        if new_fib > fib_ceil:
            return fib_nums

    return fib_nums


def fibonacci_simple_sum_2(num):
    if num <= 0:
        return False
    if num == 1:
        return True

    fibs_in_range = fibonacci_seq_in_range(num)

    for fib_a, fib_b in combinations(fibs_in_range, 2):
        if fib_a + fib_b == num:
            return True

    return False
