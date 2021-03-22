filename = 'guest_book.txt'
a = True
while a:
    b = input('Введите своё имя:')
    if b == "stop":
        a = False
    else:
        with open(filename, 'a') as file_object:
            message = ('Приветствую тебя, ' + b + '.\n')
            print(message)
            file_object.write(message)



