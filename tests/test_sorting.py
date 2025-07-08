# tests/test_sorting.py
from pages.login_page import LoginPage
from pages.product_page import ProductPage

def test_sort_by_price_desc(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    page = ProductPage(driver)
    prices = page.get_prices()
    page.sort_items("Price (high to low)")
    sorted_prices = page.get_prices()
    assert sorted_prices == sorted(prices, reverse=True)