# login page object
# https://www.imsilkroad.com/login
import time

import pandas as pd
from selenium.webdriver.common.by import By

from config import ROOT_DIR
from pages.base_page import BasePage


class ImsilkroadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username = (By.NAME, 'account')
        self.password = (By.NAME, 'password')
        self.login_btn = (By.ID, 'login')
        self.puzzle_lost_box = (By.XPATH, '//div[@class="puzzle-lost-box"]')
        self.slider_btn = (By.XPATH, '//div[@class="slider-btn"]')
        self.title = (By.XPATH, '//div[@class="title-text"]')
        self.global_index_list = (By.XPATH, "//span[contains(@class,'title-nav-item')]")
        self.statistical_period_dropdown = (By.XPATH, "//span[text()='统计周期:']/parent::*/div")
        self.statistical_period_dropdown_item = (By.XPATH, "//li[@class='el-select-dropdown__item']")
        self.date_range_selector = (
            By.XPATH, "//span[text()='时间范围:']/parent::*//i[contains(@class,'el-icon-date')]")
        self.date_range_options = (By.XPATH, "//button[@class='el-picker-panel__shortcut']")
        self.result_canvas = (By.XPATH, "//canvas")
        self.result_data_table = (By.XPATH, "//div[@class='search-container']//table")

    def login_validate(self):
        # position:absolute;width:260px;height:116px;top:0;left:-147px;z-index:111;
        puzzle_lost_box_style = self.get_element_attribute(self.puzzle_lost_box, 'style')
        offset_x = puzzle_lost_box_style.split(';')[4].split(':')[1].replace('px', '')
        abs_offset_x = abs(int(offset_x))
        self.drag_and_drop_by_offset(self.slider_btn, abs_offset_x, 0)

    def load(self, url):
        self.driver.get(url)

    def login(self, user, password):
        self.enter_text(self.username, user)
        self.enter_text(self.password, password)
        self.click_element(self.login_btn)
        self.login_validate()
        return self.wait_element_disappear(self.slider_btn)


    def navigate_to_menu(self, menu_name):
        menu = (By.XPATH, f"//span[text()='{menu_name}']")
        self.click_element(menu)

    def navigate_to_data(self):
        self.navigate_to_menu(self, '数据')

    def is_region_expanded(self, region):
        region_item = (By.XPATH, f"(//div[@role='treeitem' and .//span[text()='{region}']])[last()]")
        # check attribute aria-expanded is true
        return self.get_element_attribute(region_item, 'aria-expanded') == 'true'

    def expand_data_menu(self, region):
        if self.is_region_expanded(region):
            return
        #(//div[@role='treeitem' and .//span[text()='亚洲']])[last()]
        region_item = (By.XPATH, f"(//div[@role='treeitem' and .//span[text()='{region}']])[last()]")
        self.click_element(region_item)
        time.sleep(2)

    def select_data_menu(self, country):
        # //div[@role='treeitem' and .//span[text()='中国'] and @aria-checked]
        #(//div[@role='treeitem' and .//span[text()='中国']])[last()]//label
        country_item = (By.XPATH, f"//div[@role='treeitem' and .//span[text()='{country}'] and not(@aria-expanded)]//label")
        self.click_element(country_item)
        time.sleep(2)

    def select_tree_data_menus(self, menu_list):
        for menu in menu_list:
            self.expand_data_menu(menu)
        self.select_data_menu(menu_list[-1])

    def select_statistical_period(self, period):
        self.click_element(self.statistical_period_dropdown)
        period_items = self.find_elements(self.statistical_period_dropdown_item)
        for item in period_items:
            if item.text == period:
                item.click()
                break
        time.sleep(2)

    def select_date_range(self, date_range):
        self.click_element(self.date_range_selector)
        date_range_options = self.find_elements(self.date_range_options)
        for option in date_range_options:
            if option.text == date_range:
                option.click()
                break
        time.sleep(2)

    def get_result_canvas(self):
        timestamp = int(time.time())
        file_name = f'{ROOT_DIR}\\screenshots\\result_{timestamp}.png'
        self.get_canvas_data_to_file(self.result_canvas, filename=file_name)
        return file_name

    def get_result_table_data(self):
        table_data = []
        table_list = self.find_elements(self.result_data_table)
        if len(table_list) == 0:
            return None
        for table_item in table_list:
            if table_item.is_displayed():
                table_data.append(self.get_table_data(self.result_data_table))
        df = pd.DataFrame(data=table_data)
        return df
