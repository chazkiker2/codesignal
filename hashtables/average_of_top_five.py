"""
Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average student `1` is `87`.
The average of student `2` is `88.6`, but with integer division is `88`.

[1,91],
[1,92],
[1,60],
[1,65],
[1,87],
[1,100],
(91 + 92 + 60 + 65 + 87 + 100) // 6 = 82

(91 + 92) // 2 -> 91
    (91 + 60) // 2 -> 75
        (75 + 65) // 2 -> 70
            (70 + 87) // 2 -> 78
                (78 + 100) // 2 -> 89

1: 91, 92, 60, 65, 87, 100

[2,93],
[2,97],
[2,77],
[2,100],
[2,76]]

2: 93, 97, 77, 100, 76
(93 + 97 + 77 + 100 + 76) // 5 = 88

Notes:

The score of the students is between 1 and 100.
[execution time limit] 4 seconds (py3)

[input] array.array.integer scores

[output] array.array.integer


"""


def avg_top_five(scores):
    score_dic = {}
    for student_id, score in scores:
        if student_id not in score_dic:
            score_dic[student_id] = []

        score_dic[student_id].append(score)

    for student_id in score_dic:
        score_dic[student_id].sort()  # sort scores in place from least to greatest
        score_dic[student_id] = score_dic[student_id][-5:]  # slice last five (greatest five)

    # [student_id, average_score] for each student in score_dic
    top_five_averages = [[stud_id, (sum(score_dic[stud_id]) // len(score_dic[stud_id]))] for stud_id in score_dic]
    return top_five_averages


def tester(fn, test_case):
    actual = fn(test_case["input"])
    print("\n-----------\n")
    print(f"actual: {actual}, expected: {test_case['expected']}")
    print(f"Passed: {actual == test_case['expected']}")
    print("\n")


if __name__ == '__main__':
    test_case_01 = {
        "input": [[1, 91],
                  [1, 92],
                  [2, 93],
                  [2, 97],
                  [1, 60],
                  [2, 77],
                  [1, 65],
                  [1, 87],
                  [1, 100],
                  [2, 100],
                  [2, 76]],
        "expected": [[1, 87],
                     [2, 88]]
    }
    test_case_02 = {
        "input": [[1, 2]],
        "expected": [[1, 2]]
    }

    tester(avg_top_five, test_case_01)
    tester(avg_top_five, test_case_02)
