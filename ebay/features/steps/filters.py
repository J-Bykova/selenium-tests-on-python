from selenium import webdriver
from behave import step
from selenium.common.exceptions import NoSuchElementException


@step("Click on checkbox '{option}' in '{filter}'")
def click_checkbox(context, option, name_filter):
    checkbox = context.driver.find_element_by_xpath(
        f"//*[@class='x-refine__main__list '][.//h3[text()='{name_filter}']]"
        f"//*[@class='x-refine__main__list--value']//*[text()='{option}']")
    checkbox.click()


@step("I see selected '{option}'")
def verify_checkbox_result(context, option):
    label = context.driver.find_element_by_xpath(f"//*[@class='carousel__list']//*[text()='{option}']")
    try:
        label
    except NoSuchElementException:
        return False
    return True
