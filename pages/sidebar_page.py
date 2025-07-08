from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class SidebarPage(BasePage):
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_LINK = (By.ID, "reset_sidebar_link")

    def open_menu(self):
        self.click(self.MENU_BTN)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGOUT_LINK))

    def logout(self):
        self.click(self.LOGOUT_LINK)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))

    def reset_app_state(self):
        self.click(self.RESET_LINK)
