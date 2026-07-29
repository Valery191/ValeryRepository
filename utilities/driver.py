from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    _driver = None
    
    @classmethod
    def get_driver(cls, browser="chrome", headless=False):
        """Get driver instance (Singleton pattern)"""
        if cls._driver is None:
            if browser.lower() == "chrome":
                options = Options()
                if headless:
                    options.add_argument("--headless")
                options.add_argument("--start-maximized")
                options.add_argument("--disable-notifications")
                cls._driver = webdriver.Chrome(
                    service=Service(ChromeDriverManager().install()),
                    options=options
                )
        return cls._driver
    
    @classmethod
    def quit_driver(cls):
        """Close the driver"""
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
