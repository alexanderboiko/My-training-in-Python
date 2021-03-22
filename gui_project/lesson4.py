# Как размещать виджеты при помощи метода grid

import tkinter as tk

win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title('Мое первое графическое приложение')

# btn_1 = tk.Button(win, text='Hello1')
# btn_2 = tk.Button(win, text='Hello2')
# btn_3 = tk.Button(win, text='Hello3')
# btn_4 = tk.Button(win, text='Hello4')
# btn_5 = tk.Button(win, text='Hello5')
# btn_6 = tk.Button(win, text='Hello6')
# btn_7 = tk.Button(win, text='Hello7')
# btn_8 = tk.Button(win, text='Hello8')
#
# btn_1.grid(row=0, column=0)
# btn_2.grid(row=0, column=1)
# btn_3.grid(row=1, column=0, stick='we')
# btn_4.grid(row=1, column=1)
# btn_5.grid(row=2, column=0)
# btn_6.grid(row=2, column=1)
# btn_7.grid(row=3, column=0, columnspan=2, stick='we')
# btn_8.grid(row=0, column=2, rowspan=4, stick='sn')

for i in range(5):
    for j in range(2):
        tk.Button(win, text=f"Hello {i} {j}").grid(row=i, column=j, stick='we')

win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
