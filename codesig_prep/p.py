level_intervals = {
    300: "Poor",
    400: "Good",
    650: "Excellent",
    800: "Elite",
}

score_level_cache = level_intervals.copy()


def get_level_from_score(score):
    global level_intervals
    global score_level_cache

    # if this is a new `score`, we need to manually find its value
    if score not in score_level_cache:
        # start at lowest level, work our way up
        last_level = "Poor"

        for max_score_in_level, level in level_intervals.items():
            # if our score is greater than the highest score in this level tier
            if score > max_score_in_level:
                # increase level
                last_level = level
            # otherwise, we are in our current level!
            else:
                # we can stop iterating
                break
        # save the association between this score and this level in our cache
        score_level_cache[score] = last_level

    # return out of the cache by default (only dictionary access makes for the tiniest optimization)
    return score_level_cache[score]


class CountDict(dict):
    def __init__(self, items):
        super(CountDict, self).__init__()
        for el in items:
            if el not in self:
                self[el] = 0
            self[el] += 1


def gca_scores(scores):
    count_map = CountDict(get_level_from_score(score) for score in scores)
    total_count = len(scores)

    percentages = {
        # calculate the percentage of (SCORES_IN_LEVEL / TOTAL_SCORES), round to the 2nd decimal place
        level: round(((count / total_count) * 100), 2)
        for level, count in count_map.items()
    }

    return [
        # format each association in the requested format: "{LEVEL_TIER}: {XX.XX}%"
        f"{level}: {percent}%" for level, percent in
        # sort first by percentage (value) sort type: DESC
        # then by level (key) -- sort type: alphabet DESC
        sorted(
            percentages.items(),
            # Sort by Value then by Key
            key=lambda entry: (entry[1], entry[0]),
            # specify to sort in DESCENDING order
            reverse=True
        )
    ]


if __name__ == '__main__':

    EXPECT = "expect"
    PARAMS = "params"

    test_cases = [
        {
            EXPECT: ['Poor: 25.0%', 'Good: 25.0%', 'Excellent: 25.0%', 'Elite: 25.0%'],
            PARAMS: [300, 401, 651, 801],
        },
        {
            EXPECT: ['Poor: 50.0%', 'Excellent: 25.0%', 'Elite: 25.0%'],
            PARAMS: [300, 300, 651, 801]
        }
    ]

    for i, test_case in enumerate(test_cases):
        expected = test_case[EXPECT]
        params = test_case[PARAMS]
        actual = gca_scores(params)
        print(
            f"TEST #{i}"
            f"\n\tparams\t\t{params}"
            f"\n\texpected\t{expected}"
            f"\n\tactual\t\t{actual}"
            f"\n\t{'PASSED' if actual == expected else 'FAILED'}"
        )
