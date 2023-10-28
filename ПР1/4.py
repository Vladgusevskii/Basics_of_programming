# -*- coding: utf-8 -*-
seconds = int(input('Введите число секунд: '))
days = seconds // 86400
minutes = (seconds // 60) % 60
hours = seconds // 3600
print (f'Дни: {days}\nМинуты: {minutes}\nЧасы: {hours}\nСекунды: {seconds % 60}')
