def opposite_reverse_01(txt):
    str_to_return = ""
    for character in reversed(txt):
        str_to_return += character.swapcase()
    return str_to_return


def opposite_reverse_02(txt):
    return "".join(char.swapcase() for char in reversed(txt))


if __name__ == '__main__':
    print(opposite_reverse_02("Chaz"))
