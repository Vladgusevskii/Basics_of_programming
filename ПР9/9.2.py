#-- coding: utf-8 --
matrix = [
        [1,2,3],
        [4,-5,6],
        [7,8,-9]
        ]

def find_max(A):
    maxval = 0
    row = 0
    stroke = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if abs(A[i][j]) > maxval:
                maxval = abs(A[i][j])
                row = i
                stroke = j
    return row,stroke

def reduce(matrix, row, stroke):
    submatrix = [row[:stroke] + row[stroke+1:] for row in (matrix[:row] + matrix[row+1:])]
    return submatrix

def new(A):
    row, stroke = find_max(A)
    matrix = reduce(A,row,stroke)
    for i in matrix:
        output = ' '.join(map(str,i))
        print(output)

def main(A):
    print('До:')
    for i in A:
        output = ' '.join(map(str,i))
        print(output)
    print('\n','После:')
    new(A)

main(matrix)