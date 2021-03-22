class User:
    """Модель пользователя"""

    def __init__(self, first_name, last_name, age, salary):
        """Инициализирует пользователя"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
        self.login_attempts = 0

    def describe_user(self):
        """Описывает пользователя"""
        print('My name is ' + self.first_name.title() + ' ' + self.last_name.title() +
              '. I am ' + str(self.age) + ' years old. And I want ' + str(self.salary) +
              ' dollars in a month!!!')

    def greet_user(self):
        """Приветствует пользователя"""
        print('Hello ' + self.first_name.title() + " " + self.last_name.title())

    def increment_login_attempts(self):
        """Добавляет попытку ввода логина"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Сбрасывает количество попыток"""
        self.login_attempts = 0

    def read_login_attempts(self):
        """Выводит количество попыток"""
        print(self.login_attempts)

class Privileges:
    def __init__(self):
        self.privileges = ['удалить пользователя', 'забанить пользователя']

    def show_privileges(self):
        print(self.privileges)

class Admin(User, Privileges):
    """Модель администратора"""
    def __init__(self, first_name, last_name, age, salary):
        super().__init__(first_name, last_name, age, salary)
        self.privileges = Privileges()


user = User('alexander', 'boiko', 30, 2000)
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
user.read_login_attempts()
user1 = Admin('yana', 'boiko', 26, 1500)
user1.describe_user()
user1.privileges.show_privileges()
user1.increment_login_attempts()
user1.read_login_attempts()