"""
Given two words, decide whether they are isomorphic

iso: if you take first string & change each individual letter into another letter, can you end up with second string?

both input strings will be same length

assume all lowercase letters

- egg add True
- paper title True
- foo bar False
"""


def map_word(word):
    map = {}
    for i, c in enumerate(word):
        if ord(c) not in map:
            map[ord(c)] = []
        map[ord(c)].append(i)

    return sorted(map.values())


def is_iso(word1, word2):
    return map_word(word1) == map_word(word2)


if __name__ == '__main__':
    assert (is_iso("egg", "add") == True)
    assert (is_iso("egg", "dad") == False)
    assert (is_iso("paper", "title") == True)
    assert (is_iso("foo", "bar") == False)
