from behave import given, when, then
from selenium import webdriver
from hamcrest import assert_that, equal_to


@given("Browser is open")
def open_browser(context):
    context.driver = webdriver.Chrome(
        executable_path="/Users/jenny/Code/studying/selenium/Selenium-tests-on-python/ebay/drivers/chromedriver"
    )


@when("I go to '{url}'")
def go_to(context, url):
    context.driver.get(url)


@then("I see the title is '{title}'")
def title_is(context, title):
    assert_that(context.driver.title, equal_to(title))
