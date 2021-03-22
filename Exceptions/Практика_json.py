import json
# Программа загружае любимое число
# В противном случае запрашивает и сохраняет его

# filename = 'favourite.json'
# try:
#     with open(filename) as f_obj:
#         favourite_number = json.load(f_obj)
# except FileNotFoundError:
#     favourite_number = input('Введите свое любимое число:')
#     with open(filename, 'w') as f_obj:
#         json.dump(favourite_number, f_obj)
#         print('Я знаю ваше любимое число '+ favourite_number)
# else:
#     print(favourite_number +' это число уже есть!')


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""


filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    return None
else:
    return username

def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username



def greet_user():
    """Приветствует пользователя по имени."""


username = get_stored_username()
if username:
    print("Welcome back, " + username + "!")
else:
    username = get_new_username()
print("We'll remember you when you come back, " + username + "!")

greet_user()
