import pytest

from pytests.test_steps.cifin_steps import *


@allure.feature("Test cnfin page")
@allure.story("Test cnfin page")
@allure.title("Login page title should be '全球指数'")
@allure.description("Verify login page element contains '全球指数'")
@allure.severity(allure.severity_level.CRITICAL)
@allure.issue("JIRA-001")
@allure.epic("Test cnfin page")
@pytest.mark.parametrize("expected", ["全球指数"])
def test_login(cnfin_page, expected):
    # cnfin_page.load()
    open_cifin_page(cnfin_page)
    # title = cnfin_page.get_title()
    # print(title)
    title = get_cifin_page_title(cnfin_page)
    # assert title == expected
    verify_cifin_page_title(cnfin_page, title, expected)

@allure.feature("Test cnfin page")
@allure.story("Test cnfin page")
@allure.title("Login page title should be 'TSLA'")
@allure.description("Verify login page element contains TSLA")
@allure.severity(allure.severity_level.CRITICAL)
@allure.issue("JIRA-002")
@pytest.mark.parametrize("query", ["TSLA"])
def test_search_stock_quotes(cnfin_page, query):
    # stock_quotes = cnfin_page.get_global_index_list()
    # assert query in stock_quotes
    stock_quotes = get_cifin_page_global_index_list(cnfin_page)
    verify_cifin_page_global_index_list(cnfin_page, stock_quotes, query)


