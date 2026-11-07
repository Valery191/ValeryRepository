from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DealsPage(BasePage):

    ADD_DEAL = (By.CSS_SELECTOR, "button[data-action='add-deal']")
    DEAL_NAME = (By.NAME, "dealName")
    DEAL_AMOUNT = (By.NAME, "amount")
    DEAL_STAGE = (By.NAME, "stage")
    DEAL_CLOSE_DATE = (By.NAME, "closeDate")
    SAVE = (By.CSS_SELECTOR, "button[data-action='save']")
    PIPELINE_COLUMNS = (By.CSS_SELECTOR, ".pipeline-column")
    DEAL_CARDS = (By.CSS_SELECTOR, ".deal-card")

    def open_page(self, base_url: str):
        self.open(f"{base_url}/deals")
        self.wait_for_loader()
        return self

    def create_deal(self, deal: dict):
        self.click(self.ADD_DEAL)
        self.type(self.DEAL_NAME, deal["name"])
        self.type(self.DEAL_AMOUNT, deal["amount"])
        self.type(self.DEAL_CLOSE_DATE, deal["close_date"])
        self.click(self.SAVE)
        self.wait_for_loader()

    def get_pipeline_columns(self) -> int:
        return len(self.driver.find_elements(*self.PIPELINE_COLUMNS))

    def get_deals_count(self) -> int:
        return len(self.driver.find_elements(*self.DEAL_CARDS))

    def find_deal(self, name: str) -> bool:
        return any(name in card.text for card in self.driver.find_elements(*self.DEAL_CARDS))
