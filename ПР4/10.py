# -- coding: utf-8 --
n = int(input('Введите число n: '))
k = int(input('Введите число k: '))
fib = [0, 1]
for i in range(2, n + 1):
    fib.append(fib[i - 1] + fib[i - 2])
print (sum(fib[k-1:]))
