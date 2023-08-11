import unittest
from blueprints_models.company_trucks import CompanyTrucks
class TestCompanyTrucks(unittest.TestCase):

    def setUp(self):
        self.valid_truck = CompanyTrucks(1010, 20000, 8000)

    def test_valid_vehicle_id(self):
        valid_ids = [1001, 1020, 1040]
        for vehicle_id in valid_ids:
            truck = CompanyTrucks(vehicle_id, 20000, 8000)
            self.assertEqual(truck.vehicle_id, vehicle_id)

    def test_invalid_vehicle_id(self):
        invalid_ids = [1000, 1041, 1050]
        for vehicle_id in invalid_ids:
            with self.assertRaises(ValueError):
                CompanyTrucks(vehicle_id, 20000, 8000)

    def test_valid_capacity(self):
        valid_capacities = [1000, 15000, 42000]
        for capacity in valid_capacities:
            truck = CompanyTrucks(1010, capacity, 8000)
            self.assertEqual(truck.capacity_kg, capacity)

    def test_invalid_capacity(self):
        invalid_capacities = [-100, 45000, 50000]
        for capacity in invalid_capacities:
            with self.assertRaises(ValueError):
                CompanyTrucks(1010, capacity, 8000)

    def test_valid_max_range(self):
        valid_ranges = [1000, 6500, 13000]
        for max_range in valid_ranges:
            truck = CompanyTrucks(1010, 20000, max_range)
            self.assertEqual(truck.max_range, max_range)

    def test_invalid_max_range(self):
        invalid_ranges = [-100, 14000, 20000]
        for max_range in invalid_ranges:
            with self.assertRaises(ValueError):
                CompanyTrucks(1010, 20000, max_range)