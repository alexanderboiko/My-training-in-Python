# Введение в tkinter. Главное меню

import tkinter as tk

win = tk.Tk()
picture = tk.PhotoImage(file='people.png')
win.iconphoto(False, picture)
win.config(bg='#FFCE73')
win.title('Моё первое графическое приложение')
win.geometry('500x600+100+200')
win.minsize(300, 400)
win.maxsize(700, 800)
win.resizable(True, True)

win.mainloop()
