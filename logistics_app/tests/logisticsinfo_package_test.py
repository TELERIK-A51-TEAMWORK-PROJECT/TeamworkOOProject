import unittest
from logistics_info.package import Package
from logistics_info.location import Locations

class TestPackage(unittest.TestCase):
    
    # правим базова проверка, с която да сравняваме
    def assertInvalidPackage(self, package_id, package_name, package_kg, email, end_location):
        with self.assertRaises(ValueError):
            Package(package_id, package_name, package_kg, email, end_location)

    def test_valid_package_creation(self):
        package_id = 2
        package_name = "Televizor"
        package_kg = 50 
        email = "bobi@abv.bg" 
        end_location = Locations.ADL

        package = Package(package_id, package_name, package_kg, email, end_location)

        self.assertEqual(package.package_id, package_id)
        self.assertEqual(package.package_name, package_name)
        self.assertEqual(package.package_kg, package_kg)
        self.assertEqual(package.email, email)
        self.assertEqual(package.end_location, end_location)

    def test_invalid_package_id(self):
        self.assertInvalidPackage(-1, "Invalid ID Package", 15, "###&@abv.bg", "Wrong destination")

    def test_invalid_package_name(self):
        self.assertInvalidPackage(2, "A", 20, "john@abv.bg", "Wrong destination")
        self.assertInvalidPackage(3, "This package name is way too long and invalid", 25, "###&@abv.bg", "Wrong destination")

    def test_invalid_package_kg(self):
        self.assertInvalidPackage(4, "Heavy Package", -5, "john@abv.bg", "Wrong destination")
        self.assertInvalidPackage(5, "Too Heavy Package", 150, "john@abv.bg", "Wrong destination")

    def test_invalid_email(self):
        self.assertInvalidPackage(6, "Invalid Email Package", 30, "###&@abv.bg", "Destination G")
        self.assertInvalidPackage(7, "Another Invalid Email Package", 40, "john@abv.bg!", "Destination H")

    def test_invalid_email_length(self):
        self.assertInvalidPackage(8, "Email Length Package", 50, "a@b.c", "Destination I")
        self.assertInvalidPackage(9, "Long Email Length Package", 60, "###&@abv.bg", "Destination J")