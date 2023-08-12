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
        expected_output += "Trucks: No information\n"
        expected_output += "Routes: No information\n"
        expected_output += "Packages: No information\n"
        expected_output += "------------------------------------------------------------------------------\n"
        self.assertEqual(employee_login.execute(), expected_output)

    def test_execute_incorrect_password(self):
        params = [self.invalid_password]
        with self.assertRaises(ValueError):
            employee_login = EmployeeLogin(params, self.app_data)
            employee_login.execute()

    def test_format_data_empty_list(self):
        employee_login = EmployeeLogin(["mbi10811"], self.app_data)
        data_list = []
        data_type = "TestType"
        id_func = lambda item: item["id"]
        info_func = lambda item: [item["info"]]
        expected_output = f"{data_type}: No information\n"
        self.assertEqual(employee_login.format_data(data_list, data_type, id_func, info_func), expected_output)

    def test_format_data_nonempty_list(self):
        employee_login = EmployeeLogin(["mbi10811"], self.app_data)
        data_list = [{"id": 1, "info": "Info1"}, {"id": 2, "info": "Info2"}] 
        data_type = "TestType"
        id_func = lambda item: item["id"]
        info_func = lambda item: [item["info"]]
        expected_output = f"{data_type}: 1 - Info1 / 2 - Info2\n"
        self.assertEqual(employee_login.format_data(data_list, data_type, id_func, info_func), expected_output)