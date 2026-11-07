import pytest

from config.config import Config
from pages.deals_page import DealsPage
from utilities.test_data_loader import get_deals


@pytest.mark.deals
def test_create_deal(logged_in_driver):
    page = DealsPage(logged_in_driver).open_page(Config.BASE_URL)
    deal = get_deals()[0]
    page.create_deal(deal)

    assert page.find_deal(deal["name"]), "Deal was not found on pipeline"


@pytest.mark.deals
def test_pipeline_has_columns(logged_in_driver):
    page = DealsPage(logged_in_driver).open_page(Config.BASE_URL)

    assert page.get_pipeline_columns() >= 4


@pytest.mark.deals
@pytest.mark.parametrize("deal", get_deals())
def test_deals_visible_on_pipeline(logged_in_driver, deal):
    page = DealsPage(logged_in_driver).open_page(Config.BASE_URL)

    assert page.get_deals_count() >= 1
