from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CnfinPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.title = (By.XPATH, '//div[@class="title-text"]')
        self.global_index_list = (By.XPATH, "//span[contains(@class,'title-nav-item')]")

    def load(self):
        super().load("https://www.cnfin.com/quote/index.html")

    def get_title(self):
        return self.get_text(self.title)

    def get_global_index_list(self):
        return self.get_all_visible_text(self.global_index_list)



