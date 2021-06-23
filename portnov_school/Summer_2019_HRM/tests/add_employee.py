import unittest
from time import sleep

from pages.LoginPage import LoginPage
from pages.MainMenuElements import *
from test_data.login_data import correct_password, correct_admin_name
from browsers.browsers_runner import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = BrowserRunner().run()
        page = LoginPage(self.driver)
        page.enterName(correct_admin_name)
        page.enterPassword(correct_password)
        page.pushButton()
        sleep(2)

        page_pim = MainMenuElements(self.driver)
        page_pim.pushPimMenu()

    def tearDown(self):
        self.driver.quit()


    def test_something(self):


       self.driver.find_element_by_xpath('//*[@id="empsearch_employee_name_empName"]').send_keys('j')

        # Login
        # Click the add button
        # Enter first and last name
        # Enter and remember the InpId
        # Save the Employee
        # Go to PIM page
        # Search by InpId

        # Expected: 1 record back
        # Expected: correct name and InpId

        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
