import pytest
from pages.login_page import LoginPage

import allure


@allure.feature("Login")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("User should get logged in")
@allure.description("Entering valid username and password to check user login")
@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


@allure.feature("Login")
@allure.story("Invalid Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("User should not get logged in")
@allure.description("Entering invalid username and password to check user login")
@pytest.mark.regression
@pytest.mark.login
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("wrong_user", "secret_sauce")
    
    assert "Epic Sadface" in login_page.get_error_message()