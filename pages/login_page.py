from locators.login_locators import LoginLocators
from utilities.waits import Waits
from utilities.logger import get_logger
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)


    # def enter_username(self, username):
    #     self.waits.wait_for_visibility(LoginLocators.USERNAME).send_keys(username)
    
    # def enter_password(self, password):
    #     self.waits.wait_for_visibility(LoginLocators.PASSWORD).send_keys(password)
    
    # def click_login(self):
    #     self.waits.wait_for_clickable(LoginLocators.LOGIN_BUTTON).click()

    def login(self, username, password):

        self.logger.info("Entering username")
        self.type(LoginLocators.USERNAME, username)

        self.logger.info("Entering password")
        self.type(LoginLocators.PASSWORD, password)

        self.logger.info("Clicking login button")
        self.click(LoginLocators.LOGIN_BUTTON)

        # self.enter_username(username)
        # self.enter_password(password)
        # self.click_login()

    def get_error_message(self):
        # return self.waits.wait_for_visibility(LoginLocators.ERROR_MESSAGE).text
        return self.get_text(LoginLocators.ERROR_MESSAGE)

  


