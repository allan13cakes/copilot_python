import base64

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )

    def find_visible_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def find_visible_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located(locator)
        )

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        element.click()

    def enter_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        element.send_keys(text)

    def get_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        return element.text

    def get_all_text(self, locator):
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )
        return [element.text for element in elements]

    def get_all_visible_text(self, locator):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located(locator)
        )
        return [element.text for element in elements]

    def canvas_to_png(self, locator, filename):
        canvas = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        canvas.screenshot(filename)

    def get_canvas_data(self, locator):
        canvas = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        data_url = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
        image_data = base64.b64decode(data_url)
        return image_data

    def get_canvas_data_to_file(self, locator, filename):
        image_data = self.get_canvas_data(locator)
        with open(filename, "wb") as f:
            f.write(image_data)

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def drag_and_drop_by_offset(self, locator, x, y):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # self.driver.execute_script("window.scrollBy(0, -150);")
        action = ActionChains(self.driver)
        # action = self.driver.ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x, y).perform()

    def get_element_attribute(self, locator, attribute):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        return element.get_attribute(attribute)
    
    def wait_element_disappear(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator)
        )

    def get_table_data(self, locator):
        table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        rows = table.find_elements(By.TAG_NAME,"tr")
        data = []
        for row in rows:
            data.append(row.text.split())
        return data