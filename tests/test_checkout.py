from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.xfail(reason="Known issue: cart navigation randomly fails")
def test_checkout_success(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    page = ProductPage(driver)
    page.add_to_cart()
    page.goto_cart()
    checkout = CheckoutPage(driver)
    checkout.start_checkout()
    checkout.fill_info("John", "Doe", "12345")
    checkout.finish_checkout()
    assert "thank you for your order" in checkout.get_confirmation_text().lower()

@pytest.mark.xfail(reason="Known issue: error message sometimes not shown")
def test_checkout_missing_info(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    page = ProductPage(driver)
    page.add_to_cart()
    page.goto_cart()

    checkout = CheckoutPage(driver)
    checkout.start_checkout()
    checkout.fill_info("", "Doe", "12345")  # Missing first name

    error_container = driver.find_element(By.CLASS_NAME, "error-message-container")
    error_text = error_container.text
    if "Error" not in error_text:
        driver.save_screenshot("checkout_missing_error.png")
    assert "Error" in error_text


def test_product_images_and_prices_visible(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    page = ProductPage(driver)
    images = driver.find_elements(By.CLASS_NAME, "inventory_item_img")
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    assert all(img.is_displayed() for img in images)
    assert all(price.is_displayed() for price in prices)
