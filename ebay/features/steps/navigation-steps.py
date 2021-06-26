from behave import step


@step("I click the 'Sign in' link in the top header")
def click_top_header_sign_in_link(context):
    sign_in_link = context.driver.find_element_by_xpath("//*[@id='gh-ug']/a[text()='Sign in']")
    sign_in_link.click()

