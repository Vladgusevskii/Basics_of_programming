# -- coding: utf-8 --
s = 0
n = int(input('Введите кол-во чисел: '))
for i in range(n):
    a = int(input(f'Введите число №{i+1}: '))
    s += a
print (s)


