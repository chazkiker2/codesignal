def square_all_digits_01(n):
    digit_str = ""
    for number in str(n):
        digit_str += str(int(number)**2)

    return int(digit_str)


def square_all_digits_02(n):
    return "".join(str(int(number)**2) for number in str(n))

if __name__ == '__main__':
    print(square_all_digits_02(213))