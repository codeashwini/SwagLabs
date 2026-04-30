import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

import allure


@pytest.mark.regression
@pytest.mark.cart
@allure.feature("Cart")
@allure.story("Add Product to Cart")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Add product to cart")
@allure.description("Test adding a product to the shopping cart")
def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()
    inventory_page.click_cart_icon()

    assert cart_page.get_cart_title() == "Your Cart"
    assert cart_page.get_cart_item_name() == "Sauce Labs Backpack"
