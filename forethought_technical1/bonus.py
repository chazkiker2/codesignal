"""
- decide whether two strings are isomorphic

iso: if you take first string & change each individual letter into another letter, can you end up with second string?

both input strings will be same length

assume all lowercase letters

- egg add
- paper title
- foo bar
"""


def map_word(word):
    map = {}
    for i, c in enumerate(word):
        if ord(c) not in map:
            map[ord(c)] = []
        map[ord(c)].append(i)

    return sorted(map.values())


def is_iso(word1, word2):
    res = map_word(word1) == map_word(word2)
    print(f"{word1} {word2}\t--\t{res}")
    return res


if __name__ == '__main__':
    is_iso("egg", "add")
    is_iso("paper", "title")
    is_iso("foo", "bar")
