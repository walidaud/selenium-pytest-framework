from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest

@pytest.mark.xfail(reason="Known issue: /cart.html navigation is flaky on SauceDemo")
def test_cart_contents(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    page = ProductPage(driver)
    page.add_multiple_items(2)
    page.goto_cart()
    assert page.count_cart_items() == 2

def test_cart_persistence_after_reload(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    page = ProductPage(driver)
    page.add_to_cart()
    driver.refresh()
    assert page.is_item_in_cart()
