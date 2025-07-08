# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from utils.test_data import login_data

def test_valid_login(driver):
    page = LoginPage(driver)
    page.login(*login_data["valid"])
    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.login(*login_data["invalid"])
    error = page.get_error_message()
    assert "Username and password" in error

def test_locked_out_user(driver):
    page = LoginPage(driver)
    page.login(*login_data["locked_out"])
    error = page.get_error_message()
    assert "locked out" in error.lower()