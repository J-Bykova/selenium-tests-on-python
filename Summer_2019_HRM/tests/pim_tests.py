import unittest
from random import randint
from time import sleep
from selenium import webdriver
from browsers.browsers_runner import BrowserRunner
from pages.AddEmployeePage import AddEmployeePage
from pages.LoginPage import LoginPage
from pages.MainMenuElements import MainMenuElements
from test_data.employee_date import correct_first_name, correct_last_name, correct_id
from test_data.login_data import correct_admin_name, correct_password
from test_data.pim_data import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = BrowserRunner().run()
        page = LoginPage(self.driver)
        page.enterName(correct_admin_name)
        page.enterPassword(correct_password)
        page.pushButton()
        sleep(2)

        page_pim = MainMenuElements(self.driver)
        page_pim.pushPimMenu()
        self.driver.find_element_by_id('menu_pim_addEmployee').click()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_create_valid_employee(self):
        driver = self.driver
        page_employee = AddEmployeePage(self)
        page_employee.enterFirstName(correct_first_name)
        page_employee.enterLastName(correct_last_name)
        page_employee.employee_id(correct_id)
        page_employee.button_save()



        


    # # TODO  EY:
    # def test_something(self):
    #     # Login
    #     browser = self.browser
    #
    #
    #     # click Pim
    #     browser.find_element_by_xpath('//*[@id="menu_pim_viewPimModule"]').click()
    #     # search for Ellie
    #     # browser.find_element_by_id('empsearch_employee_name_empName').clear()
    #     browser.find_element_by_id('empsearch_employee_name_empName').send_keys('Ellie Yampolskaya')
    #     browser.find_element_by_id('searchBtn').click()
    #     # wait for the search to complete
    #     sleep(8)
    #     # verify that the search returned correct value
    #     actual_search_result = browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[4]/a').text
    #
    #
    #     self.assertEqual('Ellie', actual_search_result)
    #
    # # TODO  EY:
    # def test_emp_search_by_id(self):
    #     empId = randint(100000, 999999)
    #
    #     browser = self.browser
    #
    #     # click Pim
    #     browser.find_element_by_xpath('//*[@id="menu_pim_viewPimModule"]').click()
    #     # Click add
    #     browser.find_element_by_id('btnAdd').click()
    #     # Enter first and last name
    #     browser.find_element_by_id('firstName').send_keys('Fred')
    #     browser.find_element_by_id('lastName').send_keys('Flintstone')
    #     browser.find_element_by_id('employeeId').clear()
    #     browser.find_element_by_id('employeeId').send_keys(empId)
    #     browser.find_element_by_id('btnSave').click()
    #     browser.find_element_by_id('menu_pim_viewPimModule').click()
    #     browser.find_element_by_id('resetBtn').click()
    #     browser.find_element_by_id('empsearch_id').click()
    #
    #     actual_search_result = browser.find_element_by_xpath('').text
    #
    #     self.assertEqual(empId, int(actual_search_result))
    #
    #
    #     # Enter unique id (8 )
    #
    #
    # def test_something(self):
    #     empId = randint(100000, 999999)
    #
    #     browser = self.browser
    #
    #
    #     # Click the Add button
    #     browser.find_element_by_id("btnAdd").click()
    #     # TODO  EY: may need to come back and do 'something'
    #
    #     # Enter First and Last name
    #     browser.find_element_by_id("firstName").send_keys("James")
    #     browser.find_element_by_id("lastName").send_keys("Bond")
    #
    #     # Enter and remember the empId
    #     browser.find_element_by_id("employeeId").clear()
    #     browser.find_element_by_id("employeeId").send_keys(empId)
    #
    #     # Save the Employee
    #     browser.find_element_by_id("btnSave").click()
    #
    #     # Go to PIM page
    #     browser.find_element_by_id("menu_pim_viewPimModule").click()
    #     # TODO  EY: may need to come back and do 'something' here as well :P
    #
    #     # Search by EmpId
    #     browser.find_element_by_id("empsearch_id").send_keys(empId)
    #     browser.find_element_by_id("searchBtn").click()
    #
    #     # Expected: 1 record back
    #     self.assertTrue(len(browser.find_elements_by_xpath("//td[3]/a")) == 1)
    #
    #
    #     # Expected Correct Full Name
    #     firstName = browser.find_element_by_xpath("//td[3]/a").text
    #     lastName = browser.find_element_by_xpath("//td[4]/a").text
    #
    #
    #     self.assertEqual("James", firstName)
    #     self.assertEqual("Bond", lastName)



if __name__ == '__main__':
    unittest.main()
