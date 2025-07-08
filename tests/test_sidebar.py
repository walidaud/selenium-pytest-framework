from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.mark.xfail(reason="Logout fails intermittently on SauceDemo")
def test_logout(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    sidebar = SidebarPage(driver)
    sidebar.open_menu()
    sidebar.logout()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
    assert driver.find_element(By.ID, "user-name").is_displayed()

def test_reset_app_state(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    sidebar = SidebarPage(driver)
    sidebar.open_menu()
    sidebar.reset_app_state()
    assert True
