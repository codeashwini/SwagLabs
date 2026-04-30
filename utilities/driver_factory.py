from selenium import webdriver
from utilities.config_reader import get_config

def get_driver():
    browser = get_config("browser")

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "edge":
        driver = webdriver.Edge()

    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    return driver

