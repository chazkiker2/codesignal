"""

"""
import heapq


class Heap(object):
    def __init__(self, initial=None, key=lambda x: x):
        self.key = key
        self.index = 0
        if initial:
            self._data = [(key(item), i, item)
                          for i, item in enumerate(initial)]
            self.index = len(self._data)
            heapq.heapify(self._data)
        else:
            self._data = []

    def __str__(self) -> str:
        items = [d[2] for d in self._data]
        return f"<Heap: {items.__str__()}>"

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self._data)[2]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        rooms = Heap()

        intervals.sort(key=lambda interval: interval[0])

        for start, end in intervals:

            if rooms.is_empty():
                rooms.push(end)

            else:
                popped = rooms.pop()

                if start >= popped:
                    rooms.push(end)
                else:
                    rooms.push(popped)
                    rooms.push(end)

        return len(rooms)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[6, 15], [13, 20], [6, 17]], 3),
        ([[5, 8], [6, 8]], 2),
        ([[1, 5], [8, 9], [8, 9]], 2)
    ]

    for i, (params, expected) in enumerate(test_cases):
        print(f"\nTEST {i} with input {params}:")
        actual = solution.minMeetingRooms(params)
        print(actual, expected)
