import unittest
from core.application_data import ApplicationData
from commands.manager_login import ManagerLogin

class TestManagerLogin(unittest.TestCase):
    def setUp(self):
        self.app_data = ApplicationData()
        self.valid_password = "manager1000"
        self.invalid_password = "incorrect"

    def test_execute_correct_password(self):
        params = [self.valid_password]
        employee_login = ManagerLogin(params, self.app_data)
        expected_output = "MANAGER VIEW INFO:\n"
        expected_output += "Customers: No information\n"
        expected_output += "------------------------------------------------------------------------------\n"
        self.assertEqual(employee_login.execute(), expected_output)

    def test_execute_incorrect_password(self):
        params = [self.invalid_password]
        with self.assertRaises(ValueError):
            employee_login = ManagerLogin(params, self.app_data)
            employee_login.execute()