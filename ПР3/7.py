# -- coding: utf-8 --
def main():
    n = int(input('Введите год: '))
    if (n % 4 == 0 and n % 100 != 0) or n % 300 == 0:
        return 'Да'
    else:
        return 'Нет'

print (main())
