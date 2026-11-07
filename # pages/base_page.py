from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utilities.waits import Waits
from utilities.logger import get_logger


class BasePage:

    LOADER = (By.CSS_SELECTOR, ".loading-overlay, .spinner")

    def __init__(self, driver):
        self.driver = driver
        self.wait = Waits(driver)
        self.log = get_logger(self.__class__.__name__)

    def open(self, url: str):
        self.log.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find(self, locator):
        return self.wait.presence(locator)

    def click(self, locator):
        element = self.wait.clickable(locator)
        element.click()

    def type(self, locator, text: str, clear: bool = True):
        element = self.wait.visible(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        return self.wait.visible(locator).text.strip()

    def is_visible(self, locator) -> bool:
        try:
            return self.wait.visible(locator).is_displayed()
        except Exception:
            return False

    def wait_for_loader(self):
        self.wait.invisible(self.LOADER)

    def current_url(self) -> str:
        return self.driver.current_url

    def press_enter(self, locator):
        self.wait.visible(locator).send_keys(Keys.ENTER)
