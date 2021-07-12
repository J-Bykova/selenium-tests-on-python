import time

from behave import step


@step("I enter '{product}' into the search field")
def input_into_search_field(context, product):
    search_field = context.driver.find_element_by_xpath("//input[@class='gh-tb ui-autocomplete-input']")
    search_field.send_keys(product)


@step("I click the search button")
def click_search_button(context):
    search_button = context.driver.find_element_by_xpath("//input[@class='btn btn-prim gh-spr']")
    search_button.click()
    time.sleep(2)


@step("I click the 'Shop by category' button")
def click_category_button(context):
    category_button = context.driver.find_element_by_xpath("//*[@id='gh-shop']/button")
    category_button.click()


@step("I click the '{name}' link")
def click_product_category_link(context, name):
    product_category_link = context.driver.find_element_by_xpath(f"//a[text() = '{name}']")
    product_category_link.click()


@step("I click the 'All Categories' dropdown")
def click_categories_dropdown(context):
    categories_dropdown = context.driver.find_element_by_xpath(f"//option[text()='All Categories']")
    categories_dropdown.click()


@step("I push the '{category}' link")
def click_categories_dropdown(context, category):
    categories_dropdown = context.driver.find_element_by_xpath(f"//option[text()='{category}']")
    categories_dropdown.click()
