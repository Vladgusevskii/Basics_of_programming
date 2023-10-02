# -- coding: utf-8 --
def main(a,b,l,N):
    length = (2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)
    return length
a = int(input('Введите растояние между рядами: '))
b = int(input('Введите расстояние между дырками в ряду: '))
l = int(input('Введите длину свободного конца шнурка: '))
N = int(input('Введите кол-во дырок в ряду: '))
print ('Искомая длина шнурка: ', main(a,b,l,N))
