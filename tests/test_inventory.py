import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

import allure


@pytest.mark.smoke
@pytest.mark.inventory
@allure.feature("Inventory")
@allure.story("Page Title")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Inventory page title")
@allure.description("Verify the inventory page displays correct title")
def test_inventory_title(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.get_page_title() == "Products"


