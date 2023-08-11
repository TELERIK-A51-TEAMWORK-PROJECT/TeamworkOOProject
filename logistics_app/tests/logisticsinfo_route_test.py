import unittest
from datetime import datetime, timedelta
from logistics_info.location import Locations  # Make sure to import the required modules/classes
from logistics_info.calculation_helpers import calculate_destionation_km, calculate_maxrange_km
from logistics_info.route import RouteOfTrucks 

class TestRouteOfTrucks(unittest.TestCase):
    def setUp(self):
        self.route_data = {
            'route_id': 1,
            'truck_id': 123,
            'destinations': 'A->B->C',
            'start_time': '2023/08/11'
        }
        self.route = RouteOfTrucks(**self.route_data)
    
    def test_route_id_positive(self):
        with self.assertRaises(ValueError):
            self.route.route_id = -1

    def test_destinations_with_dates(self):
        expected_destinations_with_dates = ['A', '08/11/2023, 10:00:00', 'B', '08/11/2023, 11:00:00', 'C']
        self.assertEqual(self.route.destinations_with_dates, expected_destinations_with_dates)