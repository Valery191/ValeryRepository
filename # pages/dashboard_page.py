from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):

    USER_MENU = (By.CSS_SELECTOR, ".user-menu")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".user-menu .logout")
    SIDEBAR_CUSTOMERS = (By.CSS_SELECTOR, "a[href*='/customers']")
    SIDEBAR_DEALS = (By.CSS_SELECTOR, "a[href*='/deals']")
    WELCOME_TITLE = (By.CSS_SELECTOR, ".dashboard-header h1")
    STAT_CARDS = (By.CSS_SELECTOR, ".stat-card")

    def is_opened(self) -> bool:
        return self.is_visible(self.WELCOME_TITLE)

    def get_welcome_text(self) -> str:
        return self.get_text(self.WELCOME_TITLE)

    def get_stat_cards_count(self) -> int:
        return len(self.driver.find_elements(*self.STAT_CARDS))

    def go_to_customers(self):
        self.click(self.SIDEBAR_CUSTOMERS)

    def go_to_deals(self):
        self.click(self.SIDEBAR_DEALS)

    def logout(self):
        self.click(self.USER_MENU)
        self.click(self.LOGOUT_BUTTON)
