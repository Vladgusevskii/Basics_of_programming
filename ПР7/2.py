# -- coding: utf-8 --

# Вариант 6

def inp():
    list = []
    while len(list) != 10:
        i = int(input(f'Введите число массива #{len(list)+1}: '))
        list.append(i)
    return list

def summs():
    list = inp()
    result = []
    for i in range(1, len(list)):
        if list[i] + list[i-1] > 5:
            msg = str(f'{list[i]} + {list[i-1]} = {list[i] + list[i-1]}')
            result.append(msg)
    return result

def main():
    list = summs()
    result = 0
    print(f'\nСуммы чисел массива > 5:\n')
    for i in list:
        print(i)
        result += 1
    print(f'\nКол-во: {result}')

main()
