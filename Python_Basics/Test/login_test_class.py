import unittest
from time import sleep
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('starting...')

    def setUp(self):
        browser = webdriver.Chrome()
        self.browser.maximize_window()
        browser.get('http://hrm.seleniumminutes.com')
        self.browser = browser

    def tearDown(self):
        self.browser.quit()

    @classmethod
    def tearDownClass(cls):
        print('finished...')


# Tests

    def test_invalid_password(self):
        browser = self.browser
        browser.find_element_by_id('txtUsername').send_keys('admin')
        browser.find_element_by_id('txtPassword').send_keys('password')
        browser.find_element_by_id('btnLogin').click()

        warning_text = browser.find_element_by_id('spanMessage').text

        # Expected value vs. Actual value
        self.assertEqual('Invalid credentials', warning_text)


    def test_empty_password(self):
        browser = self.browser
        browser.find_element_by_id('txtUsername').send_keys('admin')
        browser.find_element_by_id('btnLogin').click()

        sleep(2)

        warning_text = browser.find_element_by_id('spanMessage').text

        # Expected value vs. Actual value
        self.assertEqual('Password cannot be empty', warning_text)

    def test_empty_username(self):
        browser = self.browser
        browser.find_element_by_id('txtPassword').send_keys('Password')
        browser.find_element_by_id('btnLogin').click()

        sleep(2)

        warning_text = browser.find_element_by_id('spanMessage').text

        # Expected value vs. Actual value
        self.assertEqual('Username cannot be empty', warning_text)


if __name__ == '__main__':
    unittest.main()
