# Знакомство с виджетами. Entry

import tkinter as tk


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')


def delete_entry():
    name.delete(0, tk.END)

def submit():
    print(name.get())
    print(password.get())

win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title('Мое первое графическое приложение')
tk.Label(win, text='Имя').grid(row=0, column=0, stick='w')
tk.Label(win, text='Пароль').grid(row=1, column=0, stick='w')

name = tk.Entry(win)
password = tk.Entry(win,show='@')
name.grid(row=0, column=1)
password.grid(row=1, column=1)
tk.Button(win, text="get", command=get_entry).grid(row=2, column=0)
tk.Button(win, text="delete", command=delete_entry).grid(row=2, column=1, stick='we')
tk.Button(win, text="submit", command=submit).grid(row=3, column=0, stick='we')
tk.Button(win, text="in", command=lambda: name.insert(0, 'hello')) \
    .grid(row=2, column=2, stick='we')

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
