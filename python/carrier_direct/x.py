
from typing import Mapping


def is_prime(num):
    """
    given num -- return boolean indicating whether num is a prime number
    """
    # list of prime numbers –––
    # num / num
    # num / 1
    # num / any_other_number

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def count_primes(numbers):
    """
    array list [ 2,4, 5, 16, 200
    """
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1

    return count


if __name__ == "__main__":
    print(f"{is_prime(10)=}")
    print(f"{is_prime(11)=}")

    print(count_primes([2, 4, 5, 16, 200]))
