from utilities.waits import Waits

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waits = Waits(driver)

    def click(self, locator):
        self.waits.wait_for_clickable(locator).click()

    def type(self, locator, text):
        self.waits.wait_for_visibility(locator).send_keys(text)

    def get_text(self, locator):
        return self.waits.wait_for_visibility(locator).text

