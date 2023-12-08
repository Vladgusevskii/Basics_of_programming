#-- coding: utf-8 --
matrix = [
[2,4,7],
[3,8,2],
[9,8,1]
]
k = 3
def kratnchislo(matrix):
    a = 0
    for i in matrix:
        for j in i:
            if j % k == 0:
                a += 1
    return a


def maxkrat(matrix):
    max_num = 0
    for i in matrix:
        for j in i:
            if j % k == 0 and j > max_num:
                max_num = j
    print(max_num)

maxkrat(matrix)
print(kratnchislo(matrix))
