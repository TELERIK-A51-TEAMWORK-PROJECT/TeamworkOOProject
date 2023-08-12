import unittest
from blueprints_models.man import Man
class TestCompanyTrucks(unittest.TestCase):

    def setUp(self):
        self.valid_truck = Man(1013, 36000, 10000)

    def test_valid_capacity(self):
        valid_capacities = [1000, 15000, 36000]
        for capacity in valid_capacities:
            truck = Man(1012, capacity, 10000)
            self.assertEqual(truck.capacity_kg, capacity)

    def test_invalid_capacity(self):
        invalid_capacities = [-100, 37001, 40000]
        for capacity in invalid_capacities:
            with self.assertRaises(ValueError):
                Man(1012, capacity, 10000)

    def test_valid_max_range(self):
        valid_ranges = [10000]
        for max_range in valid_ranges:
            truck = Man(1012, 20000, max_range)
            self.assertEqual(truck.max_range, max_range)

    def test_invalid_max_range(self):
        invalid_ranges = [-5,9999, 14000, 20000]
        for max_range in invalid_ranges:
            with self.assertRaises(ValueError):
                Man(1012, 20000, max_range)