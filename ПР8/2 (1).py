# --coding: utf-8 --
def sor(str):
    return ''.join(sorted(str))

str = input('Введите строку')
print(sor(str))