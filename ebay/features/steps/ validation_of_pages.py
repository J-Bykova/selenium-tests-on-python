import time

from behave import step


@step("I see '{product}' on first '{num}' pages")
def items_on_first_3_pages(context, product, num):
    mismatches = []

    for _ in range(int(num)):
        next_arrow = context.driver.find_element_by_xpath("//a[@aria-label='Next page']")
        items_on_the_page = context.driver.find_element_by_xpath("//li[contains(@class, 's-item')]//h3")
        for item in items_on_the_page:
            if {product} not in item.text.lower():
                mismatches.append(item.text)

        next_arrow.click()

    if mismatches:
        raise ValueError(f"{len(mismatches)} item {mismatches} are not")


@step("I see '{product}' on first '{amount}' pages with while loop")
def items_on_first_3_pages(context, product, amount):
    mismatches = []
    current_page = context.driver.find_element_by_xpath("//a[@class='pagination__item' and @aria-current]").text
    while int(current_page) <= int(amount):
        items_on_the_page = context.driver.find_element_by_xpath("//li[contains(@class, 's-item')]//h3")
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
        raise ValueError(f"{len(mismatches)} item {mismatches} are not")


@step("I go to results page '{page}'")
def go_to_results_page(context, page):
    page_link = context.driver.find_element_by_xpath(f"//*[@class='pagination__items']//a[text() = '{page}']")
    page_link.click()


# TODO
# @step("I see the word 'Shoes' in each result heading")
# def check_results_in_page(context):


@step("I see the words '{words}' in each result heading from '{from_page_number}' to '{to_page_number}'")
def check_results_in_page_range(context, words, from_page_number, to_page_number):
    words = words.split(",")
    mismatches = []
    go_to_page(context, from_page_number)
    mismatches += check_words_in_results(context, words)

    while get_page_number(context) != to_page_number:
        if from_page_number < to_page_number:
            go_forward(context)
        else:
            go_backward(context)
        mismatches += check_words_in_results(context, words)

    if mismatches:
        raise AssertionError(mismatches)


def check_words_in_results(context, words):
    result_headings = context.driver.find_elements_by_xpath("//h3[@class = 's-item__title']")
    mismatches = []
    for heading in result_headings:
        if not is_one_of_words_in_string(heading.text, words):
            mismatches.append(heading.text)
    return mismatches


# Если одно из переданных слов есть в переданной строке то вернет True, иначе False
def is_one_of_words_in_string(source_string, words_to_find):
    for word in words_to_find:
        if word.lower() in source_string.lower():
            return True
    return False


def go_forward(context):
    try:
        forward_button = context.driver.find_element_by_xpath("//a[@class='pagination__next' and not(@aria-disabled = 'true')]")
        forward_button.click()
    except Exception:
        raise AssertionError('Forward button is unavailable')


def go_backward(context):
    try:
        backward_button = context.driver.find_element_by_xpath("//a[@class='pagination__previous' and not(@aria-disabled = 'true')]")
        backward_button.click()
    except Exception:
        raise AssertionError('Backward button is unavailable')


def go_to_page(context, to_page_number):
    ensure_page_exists(context, to_page_number)
    while get_page_number(context) != to_page_number:
        if get_page_number(context) < to_page_number:
            go_forward(context)
        else:
            go_backward(context)


def get_page_number(context):
    return context.driver.find_element_by_xpath("//a[@class='pagination__item' and @aria-current]").text


def ensure_page_exists(context, page_number):
    try:
        context.driver.find_element_by_xpath(f"//*[@class='pagination__items']//a[text()='{page_number}']")
    except Exception:
        raise AssertionError(f'Page does not exist: {page_number}')
