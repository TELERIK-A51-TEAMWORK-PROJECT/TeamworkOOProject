import unittest
from core.application_data import ApplicationData
from commands.employee_login import EmployeeLogin

class TestEmployeeLogin(unittest.TestCase):
    def setUp(self):
        self.app_data = ApplicationData()
        self.valid_password = "mbi10811"
        self.invalid_password = "incorrect"

    def test_execute_correct_password(self):
        params = [self.valid_password]
        employee_login = EmployeeLogin(params, self.app_data)
        expected_output = "EMPLOYEE VIEW INFO:\n"
        expected_output += "Trucks (0):\n"
        expected_output += "No information\n"
        expected_output += "Routes (0):\n"
        expected_output += "No information\n"
        expected_output += "Packages (0):\n"
        expected_output += "No information\n"
        expected_output += "------------------------------------------------------------------------------\n"
        self.assertEqual(employee_login.execute(), expected_output)

    def test_execute_incorrect_password(self):
        params = [self.invalid_password]
        with self.assertRaises(ValueError):
            employee_login = EmployeeLogin(params, self.app_data)
            employee_login.execute()
