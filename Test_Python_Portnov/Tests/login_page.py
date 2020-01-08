import unittest
from selenium import webdriver
from time import sleep


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_name = self.driver.find_element_by_id('txtUsername')
        self.password = self.driver.find_element_by_id('txtPassword')
        self.button_login = self.driver.find_element_by_id('btnLogin')

    def enterName(self, name):
        self.user_name.send_keys(name)

    def enterPassword(self, name):
        self.password.send_keys(name)

    def pushButton(self):
        self.button_login.click()

    def hasError(self, errorText):
        try:
            errorElem = self.driver.find_element_by_id('spanMessage')

            if errorElem.text == errorText:
                return True
            else:
                return False
        except:
            return False


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_dashboard = self.driver.find_element_by_id('menu_dashboard_index')

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://hrm.seleniumminutes.com/symfony/web/index.php/auth/login")

        # test data:
        self.correct_admin_name = "admin"
        self.incorrect_admin_name = "min"
        self.correct_password = "Password"
        self.incorrect_password = "password"
        self.password_with_space = "Password "
        self.testError = "Invalid credentials"
        self.testErrorEmptyName = "Username cannot be empty"
        self.testErrorEmptyPassword = "Password cannot be empty"


    def test_page_opened(self):
        self.assertEqual("http://hrm.seleniumminutes.com/symfony/web/index.php/auth/login", self.driver.current_url)

    def test_valid_login(self):
        Page = LoginPage(self.driver)
        Page.enterName(self.correct_admin_name)
        Page.enterPassword(self.correct_password)
        Page.pushButton()
        sleep(2)
        welcome_admin = self.driver.find_element_by_id('welcome').text
        self.assertEqual('Welcome Admin', welcome_admin)
        self.driver.close()

    def test_invalid_username(self):
        Page = LoginPage(self.driver)
        Page.enterName(self.incorrect_admin_name)
        Page.enterPassword(self.correct_password)
        Page.pushButton()
        sleep(2)
        Page.hasError(self.testError)
        self.driver.close()

    def test_empty_username(self):
        Page = LoginPage(self.driver)
        Page.enterPassword(self.correct_password)
        Page.pushButton()
        sleep(2)
        Page.hasError(self.testErrorEmptyName)
        self.driver.close()

    def test_invalid_password(self):
        Page = LoginPage(self.driver)
        Page.enterName(self.correct_admin_name)
        Page.enterPassword(self.incorrect_password)
        Page.pushButton()
        sleep(2)
        Page.hasError(self.testError)
        self.driver.close()

    def test_empty_password(self):
        Page = LoginPage(self.driver)
        Page.enterName(self.correct_admin_name)
        Page.pushButton()
        sleep(2)
        Page.hasError(self.testErrorEmptyPassword)
        self.driver.close()

    def test_space_at_end_of_password(self):
        Page = LoginPage(self.driver)
        Page.enterName(self.correct_admin_name)
        Page.enterPassword(self.password_with_space)
        Page.pushButton()
        sleep(2)
        Page.hasError(self.testError)
        self.driver.close()








if __name__ == '__main__':
    unittest.main()

