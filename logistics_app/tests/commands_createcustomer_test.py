import unittest
from core.application_data import ApplicationData
from logistics_info.location import Locations
from commands.create_customer import CreateCustomerCommand  # Replace 'your_module' with the actual module name

class TestCreateCustomerCommand(unittest.TestCase):

    def setUp(self):
        self.app_data = ApplicationData()  # You might need to initialize this with appropriate data

    def test_execute(self):
        params = ["Melbourne", "John", "Doee", "1234567899", "john@abv.bg"]
        cmd = CreateCustomerCommand(params, self.app_data)
        result = cmd.execute()

        expected_result = (
            "Customer was created in (Melbourne):\n"
            "Info: [John Doee] | Number: [1234567899] | Email: (john@abv.bg)\n"
            "------------------------------------------------------------------------------"
        )

        self.assertEqual(result, expected_result)

    def test_invalid_params_count(self):
        params = ["LocationA", "John", "Doe", "1234567890"]
        with self.assertRaises(ValueError):
            CreateCustomerCommand(params, self.app_data)

