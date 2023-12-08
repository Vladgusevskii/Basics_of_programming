#-- coding: utf-8 --
def import_matrix():
    with open('Гусевский Владислав Николаевич_У-232_vvod.txt', 'r') as file:
        txt = file.readlines()
        matrix = []
        for a in txt:
            lst = []
            for b in a.split():
                lst.append(int(b))
            matrix.append(lst)
    return matrix

def export_output(out):
    with open('Гусевский Владислав Николаевич_У-232_vivod.txt', 'w') as file:
        file.write(str(out))

def kratnchislo(matrix, k):
    a = 0
    for i in matrix:
        for j in i:
            if j % k == 0:
                a += 1
    return a


def maxkrat(matrix, k):
    max_num = 0
    for i in matrix:
        for j in i:
            if j % k == 0 and j > max_num:
                max_num = j
    return max_num

def main():
    matrix = import_matrix()
    k = 3  
    kratnchislo_count = kratnchislo(matrix, k)
    maxkrat_num = maxkrat(matrix, k)
    export_output(kratnchislo_count)
    print("Количество элементов, кратных", k, ":", kratnchislo_count)
    print("Наибольший элемент, кратный", k, ":", maxkrat_num)

main()