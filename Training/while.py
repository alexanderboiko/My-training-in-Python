number = 23
running = True

while running:
	guess = int(input('Введите целое число : '))

	if guess == number:
		print('Поздравляю, вы угадали.')
		running = False# это останавливает цикл
	elif guess < number:
		print('нет, загаданное число немного больше этого. ')
	else:
		print('нет, загаданное число немного меньше этого')
else:
	print('цикл while закончен.')
	#здесь можно выполнить все что еще нужно

print('Завершение.')