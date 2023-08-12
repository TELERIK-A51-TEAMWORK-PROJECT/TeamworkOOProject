import unittest
from core.application_data import ApplicationData
from commands.create_truck import CreateTruckCommand

class TestCreateTruckCommand(unittest.TestCase):

    def setUp(self):
        self.app_data = ApplicationData()  

    def test_execute_creates_truck(self):
        params = ['1003', '5000', '8000']
        command = CreateTruckCommand(params, self.app_data)
        
        result = command.execute()

        expected_result = (
            '------------------------------------------------------------------------------\n'
            'Truck Scania with id: [1003] was created!\n'
            '------------------------------------------------------------------------------'
        )
        self.assertEqual(result, expected_result)
        self.assertTrue(self.app_data.vehicle_exists(1003))

        truck = self.app_data.find_truck_by_id(1003)
        self.assertEqual(truck.capacity_kg, 5000)
        self.assertEqual(truck.max_range, 8000)

    def test_execute_existing_truck(self):
        existing_truck_id = 1012
        self.app_data.create_truck(existing_truck_id, 6000, 10000)

        params = [str(existing_truck_id), '6000', '10000']
        command = CreateTruckCommand(params, self.app_data)

        with self.assertRaises(ValueError) as context:
            command.execute()
        expected_error_msg = (f'Truck {ApplicationData.find_nameoftruck_by_id(existing_truck_id)} with id: [{existing_truck_id}] already exists!')
        self.assertEqual(str(context.exception), expected_error_msg)
