import unittest
from selenium import webdriver
from time import sleep
from browsers.browsers_runner import BrowserRunner
from pages.LoginPage import LoginPage
from test_data.login_data import *



class LoginTestSuit(unittest.TestCase):

    def setUp(self):
        self.driver = BrowserRunner().run()

    def tearDown(self):
        self.driver.close()

    def test_page_opened(self):
        self.assertEqual("http://hrm.seleniumminutes.com/symfony/web/index.php/auth/login", self.driver.current_url)

    def test_valid_login(self):
        page = LoginPage(self.driver)
        page.enterName(correct_admin_name)
        page.enterPassword(correct_password)
        page.pushButton()
        sleep(2)
        welcome_admin = self.driver.find_element_by_id('welcome').text
        self.assertEqual('Welcome Admin', welcome_admin)

    def test_invalid_username(self):
        page = LoginPage(self.driver)
        page.enterName(incorrect_admin_name)
        page.enterPassword(correct_password)
        page.pushButton()
        sleep(2)
        page.hasError(testError)

    def test_empty_username(self):
        page = LoginPage(self.driver)
        page.enterPassword(correct_password)
        page.pushButton()
        sleep(2)
        page.hasError(testErrorEmptyName)

    def test_invalid_password(self):
        page = LoginPage(self.driver)
        page.enterName(correct_admin_name)
        page.enterPassword(incorrect_password)
        page.pushButton()
        sleep(2)
        page.hasError(testError)

    def test_empty_password(self):
        page = LoginPage(self.driver)
        page.enterName(correct_admin_name)
        page.pushButton()
        sleep(2)
        page.hasError(testErrorEmptyPassword)

    def test_space_at_end_of_password(self):
        page = LoginPage(self.driver)
        page.enterName(correct_admin_name)
        page.enterPassword(password_with_space)
        page.pushButton()
        sleep(2)
        page.hasError(testError)
        
    def test_check_page_header(self):
        Page = LoginPage(self.driver)
        Page.enterName(correct_admin_name)
        Page.enterPassword(correct_password)
        Page.pushButton()
        sleep(2)
        dashboard = self.driver.find_element_by_id('menu_dashboard_index').text
        self.assertEqual('Dashboard', dashboard)

    def test_check_header_form(self):
        Page = LoginPage(self.driver)
        Page.enterName(incorrect_admin_name)
        Page.enterPassword(correct_password)
        Page.pushButton()
        sleep(2)
        form_header = self.driver.find_element_by_id('logInPanelHeading').text
        self.assertEqual('LOGIN Panel', form_header)

if __name__ == '__main__':
    unittest.main()
