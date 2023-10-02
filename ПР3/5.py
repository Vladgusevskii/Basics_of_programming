# -- coding: utf-8 --
def main(a,b,c):
    numbers = [a,b,c]
    return min(numbers)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print ('Минимальное число: ', main(a,b,c))
