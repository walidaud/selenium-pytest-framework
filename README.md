# README.md
# TestNest: Selenium + Pytest QA Automation Framework

# SauceDemo UI Test Automation Framework

This project is a complete UI automation test suite for [SauceDemo](https://www.saucedemo.com/), built with Selenium WebDriver, Pytest, and integrated with HTML reporting, test reruns, and GitHub Actions CI.

Note: SauceDemo includes intentional failures (e.g. broken cart and checkout), which are marked accordingly in the test suite using `@pytest.mark.xfail`.

---


---

## Features

 Selenium WebDriver with Chrome  
 Pytest framework with modular test files  
 Page Object Model (POM) structure  
 Custom Pytest fixtures (`conftest.py`)  
 HTML test reporting (`pytest-html`)  
 Automatic reruns for flaky tests (`pytest-rerunfailures`)  
 Marked `xfail` tests for SauceDemo's intentional failures  
 CI/CD pipeline via GitHub Actions  
 Version-controlled with Git & GitHub

---

## Running the Tests Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run all tests with HTML report and retries
```bash
pytest --html=reports/report.html --self-contained-html --reruns 2
```

### 3. Run specific test file
```bash
pytest tests/test_login.py
```

## Intentionally Broken Tests
test_cart_contents - Cart redirection fails intermittently
test_checkout_success - Checkout flow is unreliable
test_checkout_missing_info - Error message not always shown
test_logout - Logout doesn't redirect consistently


## CI/CD with GitHub Actions
All tests run automatically on every push or pull request via GitHub Actions.
.github/workflows/ci.yml handles:
Python setup
Dependency installation
Running the test suite
Generating HTML reports

## Tools
Python 3.13+
Selenium 4
Pytest 8+
pytest-html
pytest-rerunfailures
GitHub Actions for CI
ChromeDriver