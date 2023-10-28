# -- coding: utf-8 --
def main():
    s = 0
    n = int(input('Введите число n: '))
    for i in range(1, n + 1):
        s += i**3
    print (s)
main()
