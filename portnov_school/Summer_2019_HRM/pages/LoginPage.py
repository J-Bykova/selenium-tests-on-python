

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Elements
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