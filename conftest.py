# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()