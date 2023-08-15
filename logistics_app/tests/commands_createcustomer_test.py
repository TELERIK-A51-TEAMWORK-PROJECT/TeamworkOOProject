import unittest
from core.application_data import ApplicationData
from logistics_info.location import Locations
from commands.create_customer import CreateCustomerCommand  

class TestCreateCustomerCommand(unittest.TestCase):

    def setUp(self):
        self.app_data = ApplicationData()  

    def test_execute(self):
        params = ["Melbourne", "Ivailo", "Bonev", "1234567899", "john@abv.bg"]
        cmd = CreateCustomerCommand(params, self.app_data)
        result = cmd.execute()

        expected_result = (
            "Customer was created in (Melbourne):\n"
            "Info: [Ivailo Bonev] | Number: [1234567899] | Email: (john@abv.bg)\n"
            "------------------------------------------------------------------------------"
        )

        self.assertEqual(result, expected_result)

    def test_invalid_params_count(self):
        params = ["LocationA", "Ivailo", "Bonev", "1234567890"]
        with self.assertRaises(ValueError):
            CreateCustomerCommand(params, self.app_data)

