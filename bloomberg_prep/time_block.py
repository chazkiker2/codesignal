"""
## Description

Given a list of "Events," return a list of occupied time-blocks

- events are represented as tuples: (start, end, event_name)
    - start is simply a number, you don't need to be concerned about AM/PM
    - end is simply a number, you don't need to be concerned about AM/PM
    - assume all events hold valid times where 0 <= start <= end and both start and time are valid integers (no decimals)
    - event_name is simply a string with the name of the event
- return a list of "time-blocks" such that each contiguous block of scheduled time is represented
    - each time block should have a start time and an end time
    - output is not necessarily the same length as input list
    - event_names should not be featured in output
    - output does not need to be sorted

## Example

input_001 = [
    (100, 300, "event"),
    (115, 245, "event"),
    (200, 400, "event"),
    (600, 700, "event"),
    (500, 600, "event"),
]
expected_001 = [
    [100, 400],
    [500, 700],
]

if expected_001 = time_blocks(input_001):
    print("TEST_PASSED")
else:
    print("TEST_FAILED")

"""






# 100       300
#   115  245
def time_block(events):
    ranges = []

    for start, end, _ in events:
        added = False
        for i, (block_start, block_end) in enumerate(ranges):
            # if start overlaps
            if block_start <= start <= block_end:
                ranges[i][1] = max(ranges[i][1], end)
                added = True
                break

            # if end overlaps
            if block_start <= end <= block_end:
                ranges[i][0] = min(ranges[i][0], start)
                added = True
                break

        if not added:
            ranges.append([start, end])

    return ranges


class Event:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Block:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.prev = None
        self.next = None

    def __repr__(self):
        return_str = ""
        current = self
        while current.prev:
            current = current.prev

        while current:
            return_str += f"Block({current.start}, {current.end}) => "
            current = current.next
        return return_str[:-4]

    def add(self, start, end):
        if self.start <= start <= self.end:
            self.end = max(end, self.end)
            return
        if self.start <= end <= self.end:
            self.start = min(start, self.start)
            return

        if start > self.end:
            if self.next:
                self.next.add(start, end)
            else:
                self.next = Block(start, end)
                self.next.prev = self
                return

        else:
            if self.prev:
                self.prev.add(start, end)
            else:
                self.prev = Block(start, end)
                self.prev.next = self

    def take_all(self):
        lst = []

        current = self
        while current.prev:
            current = self.prev

        while current:
            lst.append([current.start, current.end])
            current = current.next

        return lst


def time_block_best(events):
    init_start, init_end, _ = events[0]
    root_block = Block(init_start, init_end)
    for s, e, _ in events:
        root_block.add(s, e)

    return root_block.take_all()


if __name__ == '__main__':
    test_cases = [
        # ========= TEST CASE 1 ==========
        (
            # INPUT
            [
                (100, 300, "event"),
                (115, 245, "event"),
                (200, 400, "event"),
                (600, 700, "event"),
                (500, 600, "event"),
            ],
            # EXPECTED
            [
                [100, 400],
                [500, 700],
            ]
        )
    ]

    for i, test_case in enumerate(test_cases):
        input, expected = test_case
        actual = time_block_best(input)
        print(
            f"TEST {i}\n"
            f"\t{input=}\n"
            f"\t{expected=}\n"
            f"\t{actual=}\n"
            f"PASSED ? {expected == actual}"
        )
