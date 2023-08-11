import unittest
from logistics_info.location import Locations
from logistics_info.customer_info import Customer 

class TestCustomerClass(unittest.TestCase):

    def test_validcustomer_creation(self):
        location = Locations.MEL
        first_name = "Ivailo"# няма право на цифри в името
        last_name = "Bonev" # няма право на цифри в името
        telephone = "0999999999" # телефона тества до 10 цифри
        email = "bobi@abv.bg" # без специални символи

        customer = Customer(location, first_name, last_name, telephone, email)
        
        self.assertEqual(customer.location, location)
        self.assertEqual(customer.first_name, first_name)
        self.assertEqual(customer.last_name, last_name)
        self.assertEqual(customer.telephone, telephone)
        self.assertEqual(customer.email, email)
