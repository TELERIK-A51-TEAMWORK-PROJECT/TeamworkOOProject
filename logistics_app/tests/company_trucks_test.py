import unittest

from blueprints_models.truck_models import Truck_Models
from blueprints_models.company_trucks import CompanyTrucks

VALID_NAME = Truck_Models.ACTROS
VALID_CAPACITY = 10000
VALID_MAX_RANGE = 6000


class Company_trucks_Should(unittest.TestCase):

    def test_constructor_raisesError_when_capacityOutOfBounds(self):
        with self.assertRaises(ValueError):
            _ = CompanyTrucks(VALID_NAME, -50, VALID_MAX_RANGE)

    def test_constructor_raiseError_when_priceIsNegative(self):
        with self.assertRaises(ValueError):
            _ = CompanyTrucks(VALID_NAME, VALID_CAPACITY, -100)

    def test_constructor_setsProperties_whenArgumentsAreValid(self):
        company_trucks = CompanyTrucks(VALID_NAME, VALID_CAPACITY, VALID_MAX_RANGE)
        self.assertEqual(VALID_NAME, company_trucks.model_name)
        self.assertEqual(VALID_CAPACITY, company_trucks.capacity_kg)
        self.assertEqual(VALID_MAX_RANGE, company_trucks.max_range)