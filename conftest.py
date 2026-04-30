import pytest
from selenium import webdriver
from utilities.screenshot import ScreenshotUtil
import allure
import os

from utilities.driver_factory import get_driver
from utilities.config_reader import get_config

@pytest.fixture
def driver():
    driver = get_driver()
    # driver.get("https://www.saucedemo.com/")
    driver.get(get_config("base_url"))

    # driver.maximize_window()
    yield driver
    driver.quit()

def pytest_sessionstart(session):
    print("\n===============Test Execution Started======================")
    if not os.path.exists("allure-results"):
        os.makedirs("allure-results")
    
    with open("allure-results/environment.properties", "w") as f:
        f.write("Environment : QA\n")
        f.write("Browser = Chrome\n")
        f.write("URL: https://www.saucedemo.com\n")
        f.write("Framework : Pytest + Selenium")
        f.write("Tester : Ashwini")


def pytest_sessionfinish(session, exitstatus):
    print("\n===============Test Execution Finished======================")

def pytest_runtest_setup(item):
    print(f"\n Setup Starting item : {item.name}")

def pytest_runtest_teardown(item):
    print(f"\nTeardown Finished test : {item.name}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        if 'driver' in item.funcargs:
            driver = item.funcargs["driver"]

            path = ScreenshotUtil.capture(driver, item.name)
            print(f"\nScreenshot Captured : {path}")

            allure.attach.file(
                path,name=f"{item.name}_failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            print(f"\n Screenshot captured and attached to Allure: {path}")


