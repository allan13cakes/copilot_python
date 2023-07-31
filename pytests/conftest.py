import time

import allure
import pytest
from selenium import webdriver

from config import ROOT_DIR
from pages.cnfin_page import CnfinPage
from pages.imsilkload.imsilkroad_page import ImsilkroadPage


@pytest.fixture(scope="module", autouse=True)
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="module", autouse=True)
def cnfin_page(driver):
    page = CnfinPage(driver)
    page.load()
    return page


@pytest.fixture(scope="module", autouse=True)
def imsilkroad_page(driver):
    page = ImsilkroadPage(driver)
    return page


def take_screen_shot(base_page):
    # file name with unique timestamp
    timestamp = int(time.time())
    file_name = f"{ROOT_DIR}\\screenshots\\screenshot_{timestamp}.png"
    base_page.take_screenshot(file_name)
    with open(file_name, "rb") as f:
        allure.attach(f.read(), name=f"screenshot_{timestamp}", attachment_type=allure.attachment_type.PNG)
