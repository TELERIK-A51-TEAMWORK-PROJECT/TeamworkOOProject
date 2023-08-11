import unittest
from blueprints_models.actros import Actros
class TestCompanyTrucks(unittest.TestCase):

    def setUp(self):
        self.valid_truck = Actros(1029, 25000, 13000)

    def test_valid_vehicle_id(self):
        valid_ids = [1029, 1035, 1040]
        for vehicle_id in valid_ids:
            truck = Actros(vehicle_id, 25000, 13000)
            self.assertEqual(truck.vehicle_id, vehicle_id)

    def test_invalid_vehicle_id(self):
        invalid_ids = [1005, 1024, 1041]
        for vehicle_id in invalid_ids:
            with self.assertRaises(ValueError):
                Actros(vehicle_id, 25000, 13000)

    def test_valid_capacity(self):
        valid_capacities = [1000, 15000, 26000]
        for capacity in valid_capacities:
            truck = Actros(1027, capacity, 13000)
            self.assertEqual(truck.capacity_kg, capacity)

    def test_invalid_capacity(self):
        invalid_capacities = [-100, 37001, 40000]
        for capacity in invalid_capacities:
            with self.assertRaises(ValueError):
                Actros(1027, capacity, 13000)

    def test_valid_max_range(self):
        valid_ranges = [13000]
        for max_range in valid_ranges:
            truck = Actros(1027, 20000, max_range)
            self.assertEqual(truck.max_range, max_range)

    def test_invalid_max_range(self):
        invalid_ranges = [-5,9999, 14000, 12000]
        for max_range in invalid_ranges:
            with self.assertRaises(ValueError):
                Actros(1027, 20000, max_range)