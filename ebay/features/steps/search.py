from behave import step


@step("I enter '{product}' into the search field")
def input_into_search_field(context, product):
    search_field = context.driver.find_element_by_xpath("//input[@class='gh-tb ui-autocomplete-input']")
    search_field.send_keys(product)


@step("I click the search button")
def click_search_button(context):
    search_button = context.driver.find_element_by_xpath("//input[@class='btn btn-prim gh-spr']")
    search_button.click()
