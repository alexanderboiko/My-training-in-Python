# Знакомство с виджетами. Виджет Button


def say_hello():
    print('hello')


def add_label():
    label = tk.Label(win, text='new')
    label.pack()


def counter():
    global count
    count += 1
    btn_4['text'] = f'Счетчик: {count}'


count = 0

import tkinter as tk

win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title('My first GUI')

btn_1 = tk.Button(win, text='Hello',
                  command=say_hello
                  )
btn_2 = tk.Button(win, text='Add new label',
                  command=add_label
                  )

btn_3 = tk.Button(win, text='Add new label lambda',
                  command=lambda: tk.Label(win, text='New lambda').pack()
                  )

btn_4 = tk.Button(win, text=f'Счетчик: {count}',
                  command=counter,
                  bg='blue'
                  )

btn_1.pack()
btn_2.pack()
btn_3.pack()
btn_4.pack()

win.mainloop()
