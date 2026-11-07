from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from config.config import Config


class LoginPage(BasePage):

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")
    REMEMBER_ME = (By.ID, "rememberMe")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot password?")

    def open_page(self):
        self.open(Config.LOGIN_URL)
        return self

    def login(self, email: str, password: str):
        self.log.info(f"Logging in as: {email}")
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def login_with_remember(self, email: str, password: str):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.REMEMBER_ME)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)

    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD_LINK)
