from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from config.config import Config


class Waits:

    def __init__(self, driver, timeout: int = None):
        self.driver = driver
        self.timeout = timeout or Config.EXPLICIT_WAIT

    def visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def presence(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def invisible(self, locator) -> bool:
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    def text_present(self, locator, text: str) -> bool:
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
        except TimeoutException:
            return False
