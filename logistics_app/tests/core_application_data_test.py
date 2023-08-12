import unittest
from core.application_data import ApplicationData
from blueprints_models.actros import Actros
from blueprints_models.scania import Scania
from blueprints_models.man import Man
from logistics_info.route import RouteOfTrucks
from logistics_info.customer_info import Customer
from logistics_info.package import Package


class TestApplicationData(unittest.TestCase):

    def setUp(self):
        self.app_data = ApplicationData()
        
    def test_create_route(self):
        route = self.app_data.create_route(1, 1003, "Melbourne->AliceSprings", "2023/7/8")
        self.assertEqual(len(self.app_data.routes), 1)
        
    def test_create_customer(self):
        customer = self.app_data.create_customer("Melbourne", "John", "Doe", "1234567890", "john@example.com")
        self.assertEqual(len(self.app_data.customers), 1)
        
    def test_create_package(self):
        package = self.app_data.create_package(1, "Package1", 10, "john@example.com", "Melbourne")
        self.assertEqual(len(self.app_data.packages), 1)
        
    def test_find_truck_by_id(self):
        self.app_data.create_truck(1003, 5000, 8000)
        truck = self.app_data.find_truck_by_id(1003)
        self.assertTrue(isinstance(truck, Scania))
        
    def test_find_route_by_id(self):
        self.app_data.create_route(1, 1003, "Melbourne->AliceSprings", "2023/7/8")
        route = self.app_data.find_route_byid(1)
        self.assertTrue(isinstance(route, RouteOfTrucks))
        
    def test_find_customer_by_email(self):
        self.app_data.create_customer("Melbourne->AliceSprings", "John", "Doe", "1234567890", "john@example.com")
        customer = self.app_data.find_customer_byemail("john@example.com")
        self.assertTrue(isinstance(customer, Customer))
        
    def test_find_package_by_id(self):
        self.app_data.create_package(1, "Package1", 10, "john@example.com", "Melbourne")
        package = self.app_data.find_package_byid(1)
        self.assertTrue(isinstance(package, Package))
        
    def test_vehicle_exists(self):
        self.app_data.create_truck(1003, 5000, 8000)
        self.assertTrue(self.app_data.vehicle_exists(1003))
        
    def test_route_exists(self):
        self.app_data.create_route(1, 1003, "Melbourne->AliceSprings", "2023/7/8")
        self.assertTrue(self.app_data.route_exits(1))
        
    def test_package_exists(self):
        self.app_data.create_package(1, "Package1", 10, "john@example.com", "Melbourne")
        self.assertTrue(self.app_data.package_exits(1))
        
