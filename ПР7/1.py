
# -- coding: utf-8 --

# Вариант 6

list = [33, 53, 90, 96, 44, 76, 54, 42, 27, 14]

def avg(list):
    average = sum(list) / len(list)
    result = 0
    for i in list:
        if int(i) > int(average):
            result += 1
    return result

def maxv(list):
    maxval = max(list)
    result = 0
    for i in list:
        if i < maxval:
            result += 1
    return result

print(f'Больше среднего: {avg(list)}\nМеньше максимального: {maxv(list)}')
