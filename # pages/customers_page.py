from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CustomersPage(BasePage):

    ADD_BUTTON = (By.CSS_SELECTOR, "button[data-action='add-customer']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Search customers']")
    TABLE_ROWS = (By.CSS_SELECTOR, "table.customers-table tbody tr")
    EMPTY_STATE = (By.CSS_SELECTOR, ".empty-state")

    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    EMAIL_INPUT = (By.NAME, "email")
    PHONE_INPUT = (By.NAME, "phone")
    COMPANY_INPUT = (By.NAME, "company")
    STATUS_SELECT = (By.NAME, "status")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-action='save']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "button[data-action='cancel']")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".toast-success")

    def open_page(self, base_url: str):
        self.open(f"{base_url}/customers")
        self.wait_for_loader()
        return self

    def click_add_customer(self):
        self.click(self.ADD_BUTTON)

    def create_customer(self, customer: dict):
        self.log.info(f"Creating customer: {customer['email']}")
        self.click_add_customer()
        self.type(self.FIRST_NAME_INPUT, customer["first_name"])
        self.type(self.LAST_NAME_INPUT, customer["last_name"])
        self.type(self.EMAIL_INPUT, customer["email"])
        self.type(self.PHONE_INPUT, customer["phone"])
        self.type(self.COMPANY_INPUT, customer["company"])
        self.click(self.SAVE_BUTTON)
        self.wait_for_loader()

    def search(self, query: str):
        self.type(self.SEARCH_INPUT, query)
        self.wait_for_loader()

    def get_rows_count(self) -> int:
        return len(self.driver.find_elements(*self.TABLE_ROWS))

    def is_customer_present(self, email: str) -> bool:
        self.search(email)
        return any(email in row.text for row in self.driver.find_elements(*self.TABLE_ROWS))

    def is_empty_state_visible(self) -> bool:
        return self.is_visible(self.EMPTY_STATE)

    def is_success_toast_visible(self) -> bool:
        return self.is_visible(self.SUCCESS_TOAST)
