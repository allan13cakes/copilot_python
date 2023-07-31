import allure

from config import ROOT_DIR
from pytests.conftest import take_screen_shot


@allure.step('open cifin page')
def open_cifin_page(cnfin_page):
    cnfin_page.load()

@allure.step('get cifin page title')
def get_cifin_page_title(cnfin_page):
    return cnfin_page.get_title()

@allure.step('get cifin page global index list')
def get_cifin_page_global_index_list(cnfin_page):
    return cnfin_page.get_global_index_list()

@allure.step('verify cifin page title')
def verify_cifin_page_title(cnfin_page,title, expected):
    take_screen_shot(cnfin_page)
    assert title == expected

@allure.step('verify cifin page global index list')
def verify_cifin_page_global_index_list(cnfin_page,stock_quotes, query):
    take_screen_shot(cnfin_page)
    assert query in stock_quotes