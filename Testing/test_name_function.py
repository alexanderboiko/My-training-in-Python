import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'."""

    def test_first_last_name(self):
        """Имена вида 'Janis Joplin' работают правильно?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Работают ли такие имена как 'Wolfgang Amadeys Mozart'?"""
        formatted_name = get_formatted_name('wolfgang', 'amadeys', 'mozart')
        self.assertEqual(formatted_name, 'Wolfgang Amadeys Mozart')


unittest.main()
