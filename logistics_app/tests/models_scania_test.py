import unittest
from blueprints_models.scania import Scania
class TestCompanyTrucks(unittest.TestCase):

    def setUp(self):
        self.valid_truck = Scania(1010, 41000, 8000)

    def test_valid_capacity(self):
        valid_capacities = [1000, 15000, 36000]
        for capacity in valid_capacities:
            truck = Scania(1010, capacity, 8000)
            self.assertEqual(truck.capacity_kg, capacity)

    def test_invalid_capacity(self):
        invalid_capacities = [-100, 43000, 50000]
        for capacity in invalid_capacities:
            with self.assertRaises(ValueError):
                Scania(1010, capacity, 8000)

    def test_valid_max_range(self):
        valid_ranges = [8000]
        for max_range in valid_ranges:
            truck = Scania(1010, 20000, max_range)
            self.assertEqual(truck.max_range, max_range)

    def test_invalid_max_range(self):
        invalid_ranges = [-5,9999, 14000, 12000]
        for max_range in invalid_ranges:
            with self.assertRaises(ValueError):
                Scania(1010, 20000, max_range)