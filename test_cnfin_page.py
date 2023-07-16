import allure
import pytest
from selenium import webdriver

from config import ROOT_DIR
from pages.cnfin_page import CnfinPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def cnfin_page(driver):
    page = CnfinPage(driver)
    page.load()
    return page


@pytest.mark.parametrize("expected", ["全球指数"])
def test_login(cnfin_page, expected):
    cnfin_page.load()
    title = cnfin_page.get_title()
    print(title)
    cnfin_page.take_screenshot(f"{ROOT_DIR}\\screenshots\\screenshot.png")
    with open(f"{ROOT_DIR}\\screenshots\\screenshot.png", "rb") as f:
        allure.attach(f.read(), name="screenshot", attachment_type=allure.attachment_type.PNG)
    assert title == expected


@pytest.mark.parametrize("query", ["TSLA"])
@pytest.mark.description("Test searching for stock quotes")
def test_search_stock_quotes(cnfin_page, query):
    stock_quotes = cnfin_page.get_global_index_list()
    assert query in stock_quotes


@pytest.mark.parametrize("query", ["123"])
@pytest.mark.description("Test searching for invalid query")
def test_search_invalid_query(cnfin_page, query):
    error_message = cnfin_page.get_global_index_list()
    assert error_message == query
