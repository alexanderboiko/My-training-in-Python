filename = 'guest_book.txt'
with open(filename, 'a') as file_object:
    a = True
while a:
    b = input('Введите своё имя:')
    if b == "stop":
        a = False
    else:
        message = ("Приветствую тебя, " + b + '.\n')
        file_object.write(message)
        print(message)

