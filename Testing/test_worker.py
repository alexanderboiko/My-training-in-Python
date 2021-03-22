import unittest
from worker import Employee

class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee"""

    def setUp(self):
        """Создание работника для использования в тестах"""
        self.alex = Employee('alex', 'lutai', 1000)

    def test_give_default_raise(self):
        """Тест который проверяет надбавку по умолчанию"""
        self.alex.give_raise()
        self.assertEqual(self.alex.salary, 6000)

    def test_give_custom_raise(self):
        """Тест который проверяет любую надбавку"""
        self.alex.give_raise(7000)
        self.assertEqual(self.alex.salary, 8000)

unittest.main()
