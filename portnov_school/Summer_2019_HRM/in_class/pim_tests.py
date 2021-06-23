import unittest
from random import randrange
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select


class MyTestCase(unittest.TestCase):

    def setUp(self):
        browser = webdriver.Firefox()
        browser.get("http://hrm.seleniumminutes.com")

        # login
        browser.find_element_by_id('txtUsername').send_keys('admin')
        browser.find_element_by_id('txtPassword').send_keys('Password')
        browser.find_element_by_id('btnLogin').click()

        self.browser = browser

    def tearDown(self):
        self.browser.quit()

    def test_emp_search_by_name(self):
        browser = self.browser
        # click PIM
        browser.find_element_by_id('menu_pim_viewPimModule').click()
        # search for 'Ellie'
        browser.find_element_by_id('empsearch_employee_name_empName').clear()
        browser.find_element_by_id('empsearch_employee_name_empName').send_keys('Ellie')
        # wait for the search to complete
        browser.find_element_by_id('searchBtn').click()
        sleep(2)
        # verify that the search returned correct value
        actual_search_result = browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[3]/a').text
        self.assertEqual('Ellie', actual_search_result)

    def test_emp_search_by_id(self):
        emp_id = randrange(10000000, 99999999)
        browser = self.browser
        # click PIM
        browser.find_element_by_id('menu_pim_viewPimModule').click()
        # click Add
        browser.find_element_by_id('btnAdd').click()
        # enter First and Last name
        browser.find_element_by_id('firstName').send_keys('Wilma')
        browser.find_element_by_id('lastName').send_keys('Flintstone')
        # enter unique id (8 digit or more)
        browser.find_element_by_id('employeeId').clear()
        browser.find_element_by_id('employeeId').send_keys(emp_id)
        # click Save
        browser.find_element_by_id('btnSave').click()
        # go back to PIM
        browser.find_element_by_id('menu_pim_viewPimModule').click()
        # search for the unique id (8 digit from above)
        browser.find_element_by_id('empsearch_id').click()
        browser.find_element_by_id('empsearch_id').send_keys(emp_id)
        browser.find_element_by_id('searchBtn').click()
        sleep(2)
        # verify that the search returned correct value and person (first and last name)
        actual_search_result = browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[2]/a').text
        self.assertEqual(str(emp_id), actual_search_result)

    # 24.07.19
    def test_emp_search_by_job_title(self):
        browser = self.browser
        # click PIM
        browser.find_element_by_id('menu_pim_viewPimModule').click()
        # # select QA Engineer job Title
        browser.find_element_by_id('empsearch_job_title').click()
        browser.find_element_by_id('empsearch_job_title').find_element_by_xpath('.//option[5]').click()
        # click search
        browser.find_element_by_id('searchBtn').click()

        sleep(3)

        all_rows = browser.find_elements_by_xpath('//tbody/tr')
        for i, single_row in enumerate(all_rows, 1):
            # check result contains QA Engineer
            actual_result = single_row.find_element_by_xpath(".//td[5]").text
            self.assertEqual("QA Engineer", actual_result)
            print("Done checking row " + str(i))

    def test_emp_search_by_job_title2(self):
        browser = self.browser
        # click PIM
        browser.find_element_by_id('menu_pim_viewPimModule').click()
        # # select QA Engineer job Title
        # browser.find_element_by_id('empsearch_job_title').click()
        # browser.find_element_by_id('empsearch_job_title').find_element_by_xpath('.//option[5]').click()
        # click search

        Select(browser.find_element_by_id('empsearch_job_title')).select_by_visible_text("QA Engineer")
        browser.find_element_by_id('searchBtn').click()

        sleep(3)

        all_rows = browser.find_elements_by_xpath('//tbody/tr')
        for i, single_row in enumerate(all_rows, 1):
            actual_result = single_row.find_element_by_xpath(".//td[5]").text
            self.assertEqual("QA Engineer", actual_result)
            print("Done checking row " + str(i))

    def test_check_name(self):
        browser = self.browser
        # click PIM
        browser.find_element_by_id('menu_pim_viewPimModule').click()
        browser.find_element_by_id('empsearch_employee_name_empName').clear()
        browser.find_element_by_id('empsearch_employee_name_empName').send_keys('Jane')
        sleep(2)

        all_items = browser.find_elements_by_xpath("//strong")
        for i, item in enumerate(all_items, 1):
            self.assertEqual("Jane", item.text)
            print("Done checking item " + str(i))



    def test_verify_names_in_alpha_order(self):
        browser = self.browser
        browser.find_element_by_id('menu_pim_viewPimModule').click()
        browser.find_element_by_link_text("First (& Middle) Name").click()
        sleep(3)

        elems = browser.find_elements_by_xpath('//td[3]/a')
        def getText(elem):
            return elem.text



        self.assertTrue()


        


if __name__ == '__main__':
    unittest.main()
