import unittest
from selenium import webdriver


class AddEmployee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get()

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()