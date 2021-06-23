def judge_trust(n, trust):
    trust_in = {i: 0 for i in range(1, n + 1)}
    trust_out = {i: 0 for i in range(1, n + 1)}
    for [truster, trustee] in trust:
        trust_out[truster] += 1
        trust_in[trustee] += 1
    judge = 0
    for key in trust_out:
        if trust_out[key] == 0:
            judge = key
    if judge > 0 and trust_in[judge] == (n - 1):
        return judge
    else:
        return -1


def uncover_spy(n, trust):
    trust_in = {i: 0 for i in range(1, n + 1)}
    trust_out = {i: 0 for i in range(1, n + 1)}

    for truster, trustee in trust:
        trust_out[truster] += 1
        trust_in[trustee] += 1

    spy = -1
    for truster in trust_out:
        if trust_out[truster] == 0 and trust_in[truster] == n - 1:
            spy = truster

    return spy


def tester(n, trust, expected):
    actual = uncover_spy(n, trust)
    print("\n\n-----TEST\n")
    print(f"input: n={n}, trust={trust}")
    print(f"actual: {actual}")
    print(f"expected: {expected}")
    print(f"\npass? {actual == expected}")
    print("------\n")


if __name__ == '__main__':
    tester(2, [[1, 2]], 2)
    tester(3, [[1, 3], [2, 3]], 3)
    tester(3, [[1, 3], [2, 3], [3, 1]], 1)
    tester(3, [[1, 2], [2, 3]], -1)
    tester(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]], 3)
