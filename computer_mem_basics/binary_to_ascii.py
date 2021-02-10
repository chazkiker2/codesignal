"""
Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.

Every eight bits in the binary string represents one character on the ASCII table.

Examples:

csBinaryToASCII("011011000110000101101101011000100110010001100001") -> "lambda"
01101100 -> 108 -> "l"
01100001 -> 97 -> "a"
01101101 -> 109 -> "m"
01100010 -> 98 -> "b"
01100100 -> 100 -> "d"
01100001 -> 97 -> "a"
csBinaryToASCII("") -> ""
Notes:

The input string will always be a valid binary string.
Characters can be in the range from "00000000" to "11111111" (inclusive).
In the case of an empty input string, your function should return an empty string.
"""


def binary_to_ascii(binary):
    result_str = ""
    eight_bits = [binary[i:i + 8] for i in range(0, len(binary), 8)]
    for bit in eight_bits:
        num = int(bit, 2)
        result_str += chr(num)

    return result_str


def binary_to_ascii_02(binary):
    eight_bits = [binary[i:i + 8] for i in range(0, len(binary), 8)]
    return "".join(chr(int(bit, 2)) for bit in eight_bits)
