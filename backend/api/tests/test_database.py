import unittest
from api.database import get_beer


class TestDatabase(unittest.TestCase):

    def test_get_beer_existing_beer(self):
        beer_name = "Corona"
        expected_beer = {
            'name': 'Corona',
            'price': 115,
            'quantity': 2
        }
        expected_last_updated = '2024-09-10 12:00:00'

        beer, last_updated = get_beer(beer_name)

        self.assertEqual(beer, expected_beer)
        self.assertEqual(last_updated, expected_last_updated)

    def test_get_beer_nonexistent_beer(self):
        beer_name = "Pilsen"

        with self.assertRaises(ValueError) as error:
            get_beer(beer_name)

        self.assertEqual(str(error.exception), "Cerveza 'Pilsen' no encontrada en el inventario")
