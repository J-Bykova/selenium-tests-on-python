from behave import step


@step("I click the 'Sign in' link in the top header")
def click_top_header_sign_in_link(context):
    sign_in_link = context.driver.find_element_by_xpath("//*[@id='gh-ug']/a[text()='Sign in']")
    sign_in_link.click()


@step("I click the 'register' link in the top header")
def click_top_header_register_link(context):
    context.driver.find_element_by_xpath("//*[@id='gh-ug-flex']/a[text()='register']").click()


@step("I click the 'Daily Deals' link in the top header")
def click_top_header_daily_deals_link(context):
    context.driver.find_element_by_xpath("//*[@class='gh-t gh-divider-l']/a[text()=' Daily Deals']").click()


@step("I click the 'Brand Outlet' link in the top header")
def click_top_header_brand_outlet_link(context):
    context.driver.find_element_by_xpath("//*[@id='gh-p-4']/a[text()=' Brand Outlet']").click()


@step("I click the 'Help & Contact' link in the top header")
def click_top_header_daily_deals_link(context):
    context.driver.find_element_by_xpath("//*[@id='gh-p-3']/a[text()=' Help & Contact']").click()


@step("I click the 'Sell' link in the top header")
def click_top_header_daily_deals_link(context):
    context.driver.find_element_by_xpath("//*[@id='gh-p-2']/a[text()=' Sell']").click()
