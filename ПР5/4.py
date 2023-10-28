# -- coding: utf-8 --
x = int(input('Введите x: '))
y = int(input('Введите y: '))

def f1(x):
    i = (x / 100)*10
    x += i
    return x

def f2(x, y):
    result = 0
    while x <= y:
        x = f1(x)
        result += 1
    return result

print (f2(x,y))
