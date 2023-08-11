import unittest
from logistics_info.package import Package
from logistics_info.location import Locations

class Package_should(unittest.TestCase):

    def test_validpackage_creation(self):
        package_id = 2
        package_name = "Televizor"
        package_kg = 50 
        email = "bobi@abv.bg" 
        end_location = Locations.ADL

        package = Package(package_id, package_name, package_kg,email,end_location)
            
        self.assertEqual(package.package_id, package_id)
        self.assertEqual(package.package_name, package_name)
        self.assertEqual(package.package_kg, package_kg)
        self.assertEqual(package.email, email)
        self.assertEqual(package.end_location, end_location)