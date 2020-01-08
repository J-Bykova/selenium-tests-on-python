import unittest
from selenium import webdriver
from time import sleep


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome(executable_path = '/Users/evgeniiabykova/PycharmProjects/Selenium/Test_Python_Portnov/browser_drivers/chromedriver')
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://hrm.seleniumminutes.com")

        # id elements
        self.user_name = self.driver.find_element_by_id('txtUsername')
        self.password = self.driver.find_element_by_id('txtPassword')
        self.button_Login = self.driver.find_element_by_id('btnLogin')
        self.logIn_Panel_Heading = self.driver.find_element_by_id('logInPanelHeading')

    # def verifying_page_header(self):
    #     page_header = 'LOGIN Panel'
    #     self.assertEqual('LOGIN Panel', page_header.text)

    def login_check(self):
        self.user_name.send_keys('admin')
        self.password.send_keys('Password')
        self.button_Login.click()
        sleep(2)





if __name__ == '__main__':
    unittest.main()
