import pytest

from my_framework.page_objects.index_page import IndexPage
from my_framework.utilities.driver_factory import DriverFactory
from my_framework.utilities.read_configs import ReadConfig


@pytest.fixture(scope='session')
def create_driver():
    """
    Fixture creates webdriver
    :return: opened base page in webdriver
    """
    chrome_driver = DriverFactory.create_driver(ReadConfig.get_browser_id())
    chrome_driver.maximize_window()
    chrome_driver.get(ReadConfig.get_base_url())
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def open_index_page(create_driver):
    """
    Fixture opens index page
    :param create_driver: function
    :return: opened index_page in webdriver
    """
    return IndexPage(create_driver)
