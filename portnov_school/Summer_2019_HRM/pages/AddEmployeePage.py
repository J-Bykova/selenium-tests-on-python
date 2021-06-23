class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver

        # Elements
        self.first_name = self.driver.find_element_by_id('firstName')
        self.last_name = self.driver.find_element_by_id('lastName')
        self.employee_id = self.driver.find_element_by_id('employeeId')
        self.button_save = self.driver.find_element_by_id('btnSave')



    def enterFirstName(self, name):
        self.first_name.send.keys(name)

    def enterLastName(self, name):
        self.last_name.send.keys(name)

    def enterEmployeeId(self, id):
        self.employee_id.send.keys(id)

    def pushButtonSave(self):
        self.button_save.click()

