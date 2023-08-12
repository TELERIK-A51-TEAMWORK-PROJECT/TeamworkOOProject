import unittest
from commands.create_truck import CreateTruckCommand
from commands.create_route import CreateRouteCommand
from commands.create_customer import CreateCustomerCommand
from commands.create_package import CreatePackageCommand
from commands.assign_package_to_truck import AssignPackageToTruck
from commands.employee_login import EmployeeLogin
from commands.manager_login import ManagerLogin
from core.application_data import ApplicationData
from core.command_factory import CommandFactory

class TestCommandFactory(unittest.TestCase):
    def setUp(self):
        self.app_data = {}
        self.factory = CommandFactory(self.app_data)

    def test_create_truck_command(self):
        cmd = self.factory.create("CreateTruck parametur1 parametur2 parametur3")
        self.assertIsInstance(cmd, CreateTruckCommand)

    def test_create_route_command(self):
        cmd = self.factory.create("CreateRoute parametur1 parametur2 parametur3 parametur4")
        self.assertIsInstance(cmd, CreateRouteCommand)

    def test_create_customer_command(self):
        cmd = self.factory.create("CreateCustomer parametur1 parametur2 parametur3 parametur4 parametur5")
        self.assertIsInstance(cmd, CreateCustomerCommand)

    def test_create_package_command(self):
        cmd = self.factory.create("CreatePackage parametur1 parametur2 parametur3 parametur4 parametur5")
        self.assertIsInstance(cmd, CreatePackageCommand)

    def test_assign_package_to_truck_command(self):
        cmd = self.factory.create("AssignPackage parametur1 parametur2 parametur3")
        self.assertIsInstance(cmd, AssignPackageToTruck)

    def test_employee_login_command(self):
        cmd = self.factory.create("EmployeeLogin parametur1")
        self.assertIsInstance(cmd, EmployeeLogin)

    def test_manager_login_command(self):
        cmd = self.factory.create("ManagerLogin parametur1")
        self.assertIsInstance(cmd, ManagerLogin)

    def test_unknown_command(self):
        with self.assertRaises(ValueError):
            self.factory.create("InvalidCommand")

