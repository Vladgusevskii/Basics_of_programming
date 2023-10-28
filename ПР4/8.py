# -- coding: utf-8 --
def main():
    n = int(input('Введите число n: '))
    for i in range(1, n + 1):
        for x in range(1, i + 1):
            print (x, sep='', end='')
        print ()
main()
