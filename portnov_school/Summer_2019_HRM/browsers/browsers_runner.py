from selenium import webdriver


class BrowserRunner:
    def run(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http://hrm.seleniumminutes.com")
        return driver

