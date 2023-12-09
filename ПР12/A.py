# -- coding: utf-8 --

## Задание 4

def main(x):
    if x < 10:
        return x
    else:
        a = x % 10 + main(x // 10)
        return a

print(main(int(input('Введите число: '))))

