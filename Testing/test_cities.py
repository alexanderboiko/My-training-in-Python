import unittest
from city_functions import get_city_country


class CitiesNamesTest(unittest.TestCase):
    """Тесты для city_functions.py"""

    def test_city_country(self):
        """Работают ли имена двойного формата"""
        formatted_name = get_city_country('santiago', 'chile')
        self.assertEqual(formatted_name, "Santiago, Chile")

    def test_city_country_population(self):
        """Работают ли имена тройного формата"""
        formatted_name = get_city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, "Santiago, Chile - 5000000")


unittest.main()
