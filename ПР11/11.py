# -- coding: utf-8 --

# Вариант 1

import tkinter as tk
import requests, json

def parse(repo,label):
    file = f'{repo}_output.json'
    try:
        filtered = {}
        output = requests.get(f'https://api.github.com/users/{repo}').json()
        needed = ['company','created_at','email','id','name','url']
        for i in needed:
            if i in output.keys() == False:
                raise Exception('Репозиторий не существует')
            filtered[i] = output[i]
        with open(file,'w') as write:
            json.dump(filtered,write)
        txt = f'Информация сохранена в {file}'
    except Exception as err:
        txt = f'Ошибка: {err}'
    label.config(text=txt)

def main_ui():
    window = tk.Tk()
    window.title('GitHub json parser')

    repo = tk.Entry(window)
    parse_btn = tk.Button(window, text='Parse', command=lambda: parse(repo.get(),output))
    txt = tk.Label(window, text='Введите имя репозитория')
    output = tk.Label(window)

    modules = [txt,repo,parse_btn,output]

    for i in modules:
        i.pack(pady=10)

    window.mainloop()

main_ui()