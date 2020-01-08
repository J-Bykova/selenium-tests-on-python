import unittest
from selenium import webdriver
from LoginPage import pim_page



class PimPage:
    def __init__(self, driver):
        self.driver = driver

class EmployeeInformation:
    def __init__(self, driver):
        self.driver = driver

        # elements
        self.field_employee_name = self.driver.find_element_by_xpath('//*[@id="empsearch_employee_name_empName"]')
        self.field_supervisor_name = self.driver.find_element_by_xpath('//*[@id="empsearch_supervisor_name"]')
        self.field_id = self.driver.find_element_by_xpath('//*[@id="empsearch_id"]')
        self.field_job_title = self.driver.find_element_by_xpath('//*[@id="empsearch_job_title"]')
        self.field_employment_status = self.driver.find_element_by_xpath('//*[@id="empsearch_employee_status"]')
        self.field_sub_unit = self.driver.find_element_by_xpath('//*[@id="empsearch_sub_unit"]')
        self.field_include = self.driver.find_element_by_xpath('//*[@id="empsearch_termination"]')
        self.button_search = self.driver.find_element_by_xpath('//*[@id="searchBtn"]')
        self.button_reset = self.driver.find_element_by_xpath('//*[@id="resetBtn"]')


    def enterEmployeeName(self, name):
        self.field_employee_name.send_keys(name)

    def enterSupervisorName(self, name):
        self.field_supervisor_name.send_keys(name)

    def enterId(self, name):
        self.field_id.send_keys(name)



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

