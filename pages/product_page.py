from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class ProductPage(BasePage):
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_TITLE = (By.CLASS_NAME, "inventory_item_name")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    REMOVE_BUTTONS = (By.XPATH, "//button[contains(text(),'Remove')]")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def remove_from_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.REMOVE_BTN))
        self.driver.find_element(*self.REMOVE_BTN).click()


    def is_item_in_cart(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(self.REMOVE_BTN))
            return True
        except:
            return False

    def goto_cart(self):
        print("🔍 Navigating to cart page...")
        self.click(self.CART_ICON)
        try:
            WebDriverWait(self.driver, 15).until(EC.url_contains("/cart.html"))
            print("Cart page loaded.")
        except:
            self.driver.save_screenshot("cart_navigation_failed.png")
            print("Failed to reach cart page. Screenshot saved.")
            raise


    def click_product_title(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PRODUCT_TITLE)).click()


    def add_multiple_items(self, count):
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        for btn in buttons[:count]:
            btn.click()
            time.sleep(0.2)  # slight buffer to ensure cart updates

    def remove_all_items(self):
        buttons = self.find_elements(self.REMOVE_BUTTONS)
        for btn in buttons:
            btn.click()

    def count_cart_items(self):
        return len(self.find_elements(self.CART_ITEMS))

    def get_prices(self):
        return [float(e.text.replace("$", "")) for e in self.find_elements(self.PRODUCT_PRICES)]

    def sort_items(self, option_text):
        self.select_dropdown_by_text(self.SORT_SELECT, option_text)
