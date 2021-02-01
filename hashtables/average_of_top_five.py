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
    for stud_id, score in scores:
        if stud_id not in score_dic:
            score_dic[stud_id] = []

        score_dic[stud_id].append(score)

    print(score_dic)

    # avg_scores_iter = [[stud_id, avg_score] for stud_id, avg_score in score_dic.items()]
    # print(avg_scores_iter)
    top_five = []
    for stud_id in score_dic:
        score_dic[stud_id].sort()
        score_dic[stud_id] = score_dic[stud_id][-5:]
        avg_score = sum(score_dic[stud_id]) // len(score_dic[stud_id])
        top_five.append([stud_id, avg_score])

    print(score_dic)
    return top_five

    # avg_scores = []

    # for stud_id in score_dic:
    #     avg_score = reduce(lambda a, b: a + b, score_dic[stud_id]) // len(score_dic[stud_id])
    #     int_sum = sum(score_dic[stud_id])
    #     int_avg = int_sum // len(score_dic[stud_id])
    #     print(int_avg)
    #     avg_scores.append([stud_id, avg_score])

    # return avg_scores

# def avg_top_five(scores):
#     pass
