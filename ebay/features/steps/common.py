from selenium import webdriver
from behave import step
from utils.asserts import assert_equal


@step("Main page is open")
def open_main_page(context):
    context.driver = webdriver.Chrome(
        executable_path="/Users/jenny/Code/studying/selenium/Selenium-tests-on-python/ebay/drivers/chromedriver"
    )
    context.driver.get("http://www.ebay.com")


@step("I see the '{expected_title}' page")
def check_page_title(context, expected_title):
    actual_title = context.driver.title
    assert_equal(expected_title, actual_title)
