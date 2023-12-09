# -- coding: utf-8 --

## Задание 3

def main():
    x = int(input('Введите число: '))
    if x == 0:
        exit(0)
    if x % 2 != 0:
            print(x)
    main()

main()
