"""
There are N students in a baking class together.
Some of them are friends, while some are not friends.
The students' friendship can be considered transitive.
This means that if Ami is a direct friend of Bill, and Bill is a
direct friend of Casey, Ami is an indirect friend of Casey.

A friend circle is a group of students who are either direct or indirect friends.

Given a N*N matrix M representing the friend relationships between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.

You need to write a function that can output the total number of friend circles among all the students.

-------------
Example 1:

Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]

Output: 2

Explanation: The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.

    a   b   c
a   1   1   0
b   1   1   0
c   0   0   1
a: [b]
b: [a]
c: []

-------------
Example 2:

Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation: The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
    a   b   c
a   1   1   0
b   1   1   1
c   0   1   1

a: [b]
b: [a, c]
c: [b]


[execution time limit] 4 seconds (py3)

[input] array.array.integer friendships

[output] integer


"""


def friend_circles(matrix):
    # length of matrix eq num of people
    friendships = {i: set() for i in range(len(matrix))}
    pring(friendships)
    for f in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[f][c] == 1:
                friendships
    return matrix


if __name__ == '__main__':
    res_1 = friend_circles([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    res_2 = friend_circles([[1,1,0], [1,1,1], [0, 1,1]])
    print(res_2)
    assert res_1 == 2
