# Виджет Combobox

import tkinter as tk
from tkinter import ttk


def show_day():
    print(combo.get())


weekDays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

win = tk.Tk()
win.geometry(f"300x400+800+150")
win.title('Мое первое графическое приложение')

combo = ttk.Combobox(win, values=weekDays)
ttk.Button(win, text='show_day', command=show_day).pack()
combo.current(0)
combo.pack()

win.mainloop()
