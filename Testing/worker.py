class Employee():

    def __init__(self, first_name, second_name, salary):
        """Инициализация работника"""
        self.first_name = first_name.title()
        self.second_name = second_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Дает работнику надбавку"""
        self.salary += amount