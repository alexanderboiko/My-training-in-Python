x = 50

def func():
	global x

	print('x равно', x)
	x = 2
	print('заменяем гобальное значение х на', x)

func()
print('значение х составляет', x)