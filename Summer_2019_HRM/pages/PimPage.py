class PimPage:
    def __init__(self, driver):
        self.driver = driver

        # Elements
        self.employee_name = self.driver.find_element_by_id('empsearch_employee_name_empName')
        self.supervisor_name = self.driver.find_element_by_id('empsearch_supervisor_name')
        self.id = self.driver.find_element_by_id('empsearch_id')
        self.button_search = self.driver.find_element_by_id('searchBtn')
        self.button_reset = self.driver.find_element_by_id('resetBtn')


    def enterEmployeeName(self, name):
        self.employee_name.send_keys(name)

    def enterSupervisorName(self, name):
        self.supervisor_name.send.keys(name)

    def enterId(self, id):
        self.id.send.keys(id)

    def pushButtonSearch(self):
        self.button_search.click()

    def pushButtonReset(self):
        self.button_reset.click()
