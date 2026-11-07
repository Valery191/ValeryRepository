import pytest

from config.config import Config
from pages.customers_page import CustomersPage
from utilities.test_data_loader import get_customers


@pytest.mark.customers
def test_create_customer(logged_in_driver):
    page = CustomersPage(logged_in_driver).open_page(Config.BASE_URL)
    customer = get_customers()[0]
    page.create_customer(customer)

    assert page.is_customer_present(customer["email"]), "Customer was not created"


@pytest.mark.customers
@pytest.mark.parametrize("customer", get_customers())
def test_search_customer_by_email(logged_in_driver, customer):
    page = CustomersPage(logged_in_driver).open_page(Config.BASE_URL)
    page.search(customer["email"])

    assert page.get_rows_count() >= 1


@pytest.mark.customers
def test_search_unknown_customer_shows_empty_state(logged_in_driver):
    page = CustomersPage(logged_in_driver).open_page(Config.BASE_URL)
    page.search("no-such-user-9999@example.com")

    assert page.is_empty_state_visible(), "Empty state was not shown"


@pytest.mark.customers
def test_success_toast_after_creation(logged_in_driver):
    page = CustomersPage(logged_in_driver).open_page(Config.BASE_URL)
    page.create_customer(get_customers()[1])

    assert page.is_success_toast_visible()
