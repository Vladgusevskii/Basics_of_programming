#-- coding: utf-8 --
def import_matrix():
    with open('Гусевский Владислав Николаевич_У-232_vvod2.txt', 'r') as file:
        txt = file.readlines()
        matrix = []
        for a in txt:
            lst = []
            for b in a.split():
                lst.append(int(b))
            matrix.append(lst)
    return matrix

def export_output(out):
    with open('Гусевский Владислав Николаевич_У-232_vivod2.txt', 'w') as file:
        file.write(str(out))

def find_max(A):
    maxval = 0
    row = 0
    stroke = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if abs(A[i][j]) > maxval:
                maxval = abs(A[i][j])
                row = i
                stroke = j
    return row, stroke

def reduce(matrix, row, stroke):
    submatrix = [row[:stroke] + row[stroke+1:] for row in (matrix[:row] + matrix[row+1:])]
    return submatrix

def new(A):
    row, stroke = find_max(A)
    matrix = reduce(A, row, stroke)
    for i in matrix:
        output = ' '.join(map(str, i))
        print(output)

def main():
    A = import_matrix()
    print('До:')
    for i in A:
        output = ' '.join(map(str, i))
        print(output)
    print('\n', 'После:')
    new(A)

main()