from selenium import webdriver
from behave import step
from time import sleep


@step("Main page is open")
def open_main_page(context):
    context.driver = webdriver.Chrome(
        executable_path="/Users/jenny/Code/studying/selenium/Selenium-tests-on-python/ebay/drivers/chromedriver"
    )
    context.driver.get("http://www.ebay.com")


@step("I enter 'Shoes' into the search field")
def input_into_search_field(context):
    search_field = context.driver.find_element_by_xpath("//input[@class='gh-tb ui-autocomplete-input']")
    search_field.send_keys("Shoes")


@step("I click the search button")
def click_search_button(context):
    search_button = context.driver.find_element_by_xpath("//input[@class='btn btn-prim gh-spr']")
    search_button.click()
    sleep(5)

