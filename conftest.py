import json

import pytest

from my_framework.page_objects.index_page.index_page import IndexPage
from my_framework.utilities.configuration import Configuration
from my_framework.utilities.driver_factory import DriverFactory
from my_framework.utilities.read_configs import ReadConfig
from my_framework.CONSTANTS import ROOT_DIR


@pytest.fixture(scope="session")
def env():
    with open(f'{ROOT_DIR}/configurations/configuration.json') as f:
        data = f.read()
        json_to_dict = json.loads(data)
    config = Configuration(**json_to_dict)
    return config


@pytest.fixture()
def create_driver(env):
    """
    Fixture creates webdriver
    :return: opened base page in webdriver
    """
    chrome_driver = DriverFactory.create_driver(env.browser_id)
    chrome_driver.maximize_window()
    chrome_driver.get(env.base_url)
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
