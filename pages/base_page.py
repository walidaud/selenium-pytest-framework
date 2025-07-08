from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=10):  # 🔧 ADD THIS
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def select_dropdown_by_text(self, locator, text):
        from selenium.webdriver.support.ui import Select
        select = Select(self.find(locator))
        select.select_by_visible_text(text)

    def is_element_present(self, locator):  # 🔧 ADD THIS TOO
        try:
            self.find(locator)
            return True
        except:
            return False
