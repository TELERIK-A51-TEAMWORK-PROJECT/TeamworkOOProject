import unittest
from blueprints_models.man import Man
class TestCompanyTrucks(unittest.TestCase):

    def setUp(self):
        self.valid_truck = Man(1013, 36000, 10000)

    def test_valid_vehicle_id(self):
        valid_ids = [1012, 1016, 1023]
        for vehicle_id in valid_ids:
            truck = Man(vehicle_id, 37000, 10000)
            self.assertEqual(truck.vehicle_id, vehicle_id)

    def test_invalid_vehicle_id(self):
        invalid_ids = [1005, 1027, 1039]
        for vehicle_id in invalid_ids:
            with self.assertRaises(ValueError):
                Man(vehicle_id, 37000, 10000)

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