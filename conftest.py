import pytest
from selenium.webdriver.support.wait import WebDriverWait

from my_framework.page_objects.index_page import IndexPage
from my_framework.page_objects.login_page import LoginPage
from my_framework.page_objects.page_cart import CartPage
from my_framework.page_objects.page_product import ProductPage
from my_framework.page_objects.page_register import RegisterPage
from my_framework.utilities.driver_factory import DriverFactory
from my_framework.utilities.read_configs import ReadConfig


@pytest.fixture(scope='session')
def create_driver():
    chrome_driver = DriverFactory.create_driver(ReadConfig.get_browser_id())
    chrome_driver.maximize_window()
    chrome_driver.get(ReadConfig.get_base_url())
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def open_index_page(create_driver):
    return IndexPage(create_driver)


@pytest.fixture()
def open_product_page(create_driver):
    return ProductPage(create_driver)


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def open_cart_page(create_driver):
    return CartPage(create_driver)


@pytest.fixture()
def open_register_page(create_driver):
    return RegisterPage(create_driver)
