# -- coding: utf-8 --
def nums():
    i = int(input('Введите число от 1 до 8: '))
    if i >= 1 and i <= 8:
        return i
    else:
        print ('Неверное число')
        return nums()
def main():
    a = nums() 
    b = nums() 
    c = nums() 
    d = nums() 
    if (a+b+c+d) % 2 == 0:
        return 'Да'
    else:
        return 'Нет'

print (main())
