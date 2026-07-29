import pytest
from utilities.driver import Driver


@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and quit the driver"""
    driver_instance = Driver.get_driver()
    yield driver_instance
    Driver.quit_driver()
