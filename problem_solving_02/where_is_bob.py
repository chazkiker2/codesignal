def where_is_bob_01(names):
    for i, name in enumerate(names):
        if name == "Bob":
            return i

    return -1


def where_is_bob_02(names):
    return names.find("Bob")
