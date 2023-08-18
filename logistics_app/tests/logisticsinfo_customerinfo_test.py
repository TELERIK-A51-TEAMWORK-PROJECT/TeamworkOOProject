import unittest
from logistics_info.location import Locations
from logistics_info.customer_info import Customer 

class TestCustomerClass(unittest.TestCase):

    # правим базова проверка, с която да сравняваме
    def assertInvalidCustomer(self, location, first_name, last_name, telephone, email):
        with self.assertRaises(ValueError):
            Customer(location, first_name, last_name, telephone, email)

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


    def test_invalid_first_name(self):
        self.assertInvalidCustomer("Location", "123", "Bonev", "1234567890", "john.doe@abv.bg")
    
    def test_invalid_last_name(self):
        self.assertInvalidCustomer("Location", "Ivalo", "123", "1234567890", "john.doe@abv.bg")
    
    def test_invalid_telephone_characters(self):
        self.assertInvalidCustomer("Location", "Mario", "Stanoichev", "12a4567890", "john.doe@eabv.bg")
    
    def test_invalid_telephone_length(self):
        self.assertInvalidCustomer("Location", "Borislav", "Bonev", "1234567", "john.doe@abv.bg")
    
    def test_invalid_email_characters(self):
        self.assertInvalidCustomer("Location", "Ivailo", "Georgiev", "1234567890", "john.doe@abv!")
    