import time

from behave import step


@step("I see '{product}' on first '{amount}' pages")
def items_on_first_3_pages(context, product, amount):
    mismatches = []

    for _ in range(int(amount)):
        next_arrow = context.driver.find_element_by_xpath("//a[@aria-label=''Next page]")
        items_on_the_page = context.driver.find_element_by_xpath("//li[contains(@class, ''s-item     )]//h3")
        for item in items_on_the_page:
            if {product} not in item.text.lower():
                mismatches.append(item.text)

        next_arrow.click()

    if mismatches:
        raise ValueError(f"{len(mismatches)} item {mismatches} are not ")


@step("I see '{product}' on first '{amount}' pages with while loop")
def items_on_first_3_pages(context, product, amount):
    mismatches = []
    current_page = context.driver.find_element_by_xpath("//a[@class='pagination__item' and @aria-current]").text
    while int(current_page) <= int(amount):
        items_on_the_page = context.driver.find_element_by_xpath("//li[contains(@class, ''s-item     )]//h3")
        for item in items_on_the_page:
            if product not in item.text.lower():
                mismatches.append(item.text)

        next_arrow = context.driver.find_elements_by_xpath(
            "//a[@aria-label=''Next page and not(@aria-disabled = 'true')]"
        )

        if next_arrow:
            next_arrow[0].click()
        else:
            break

    current_page = context.driver.find_element_by_xpath("//a[@class='pagination__item' and @aria-current]").text

    if mismatches:
        raise ValueError(f"{len(mismatches)} item {mismatches} are not ")


@step("I go to results page '{page}'")
def go_to_results_page(context, page):
    toggle_page = context.driver.find_element_by_xpath(f"//*[@class='pagination__items']//a[text() = '{page}']")
    toggle_page.click()


@step("I see the word '{word}' in each result heading")
def check_word_in_results(context, word):
    result_headings = context.driver.find_elements_by_xpath("//h3[@class = 's-item__title']")
    for heading in result_headings:
        if word.lower() not in heading.text.lower():
            raise ValueError(f"Heading {heading.text} does not contain the word {word}")
