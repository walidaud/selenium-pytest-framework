from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CONFIRMATION_TEXT = (By.CLASS_NAME, "complete-header")
    CHECKOUT_BTN = (By.ID, "checkout")

    def start_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()

    def fill_info(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BTN)

    def finish_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.FINISH_BTN)).click()

    def get_confirmation_text(self):
        return self.get_text(self.CONFIRMATION_TEXT)
