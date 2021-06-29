from behave import step
import time
from selenium.webdriver.common.action_chains import ActionChains


@step("I click the 'Sign in' link in the top header")
def click_top_header_sign_in_link(context):
    context.driver.find_element_by_xpath("//*[@id='gh-ug']/a[text()='Sign in']").click()


@step("I click the 'register' link in the top header")
def click_top_header_register_link(context):
    context.driver.find_element_by_xpath("//*[@id='gh-ug-flex']/a[text()='register']").click()


@step("I click the '{name_link}' link in the top header")
def click_top_header_link(context, name_link):
    context.driver.find_element_by_xpath(f"//div[@id='gh-top']//a[text()= '{name_link}']").click()
    time.sleep(1)


@step("I see the '{expected_title}' dropdown")
# //TODO rename method
def click_top_header_daily_deals_link(context, expected_title):
    actual_title = context.driver.find_element_by_xpath("//*[@class='rvi__title']")
    assert expected_title == actual_title.text


@step("I click the 'Sign in' link in the Watchlist dropdown")
def click_sign_in_link_into_watchlist_dropdown(context):
    context.driver.find_element_by_xpath("//*[@class='rvi__title']/a").click()


@step("I cursor at 'My eBay' in the top header")
def cursor_at_my_ebay_link(context):
    my_ebay_button = context.driver.find_element_by_xpath("//*[@class='gh-menu']/a[@title='My eBay']")
    action = ActionChains(context.driver)
    action.move_to_element(my_ebay_button).perform()
    time.sleep(1)
