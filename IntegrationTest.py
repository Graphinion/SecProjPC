import unittest
from selenium import webdriver
import sys
sys.path.insert(0, '/venv/src')
from ValidateSSH import validate_ssh_key
from ValidateCer import validate_certificate

class TestValidation(unittest.TestCase):
    def setUp(self):
        # Initialize WebDriver. Replace 'your_driver_path' with the path to your WebDriver executable
        # self.driver = webdriver.Chrome(executable_path='/Users/aqsa/bin/chromedriver')
        self.driver = webdriver.Chrome()

    def test_validate_ssh_key(self):
        # Call the function with the path to your SSH key
        result = validate_ssh_key('/Users/aqsa/IdeaProjects/SecProjPC/id_rsa')
        # Assert that the result is as expected
        self.assertEqual(result, "SSH key is valid.")

    def test_validate_certificate(self):
        # Call the function with the path to your certificate
        result = validate_certificate('/Users/aqsa/IdeaProjects/SecProjPC/certificate.crt')
        # Assert that the result is as expected
        self.assertEqual(result, "Certificate is valid.")

    def tearDown(self):
        # Close the WebDriver instance
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()