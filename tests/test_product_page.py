# tests/test_product_page.py
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    page = ProductPage(driver)
    page.add_to_cart()
    assert page.is_item_in_cart()

def test_remove_from_cart(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    page = ProductPage(driver)
    page.add_to_cart()
    page.remove_from_cart()
    
    # Extra wait if needed, to ensure cart updates
    WebDriverWait(driver, 5).until(lambda d: not page.is_item_in_cart())
    
    assert not page.is_item_in_cart()

def test_product_detail_navigation(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    page = ProductPage(driver)
    page.click_product_title()
    assert "inventory-item.html" in driver.current_url
