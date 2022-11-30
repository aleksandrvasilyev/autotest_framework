
from selenium.webdriver.common.by import By

from my_framework.page_objects.page_cart import CartPage
from my_framework.utilities.web_ui.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(self.__driver)

    __product_name = (By.XPATH, '//h1')
    __select_processor = (By.XPATH, '//select[@id="product_attribute_1"]/option[@value="2"]')
    __select_ram = (By.XPATH, '//select[@id="product_attribute_2"]/option[@value="4"]')
    __select_hdd = (By.XPATH, '//label[@for="product_attribute_3_7"]')
    __add_to_cart_button = (By.XPATH, '//*[@id="add-to-cart-button-1"]')
    __notification_success_close_button = (By.XPATH, '//div[@class="bar-notification success"]//span[@class="close"]')
    __cart_link = (By.XPATH, '//*[@id="topcartlink"]/a')
    __notification_error_close_button = (By.XPATH, '//div[@class="bar-notification error"]//span[@class="close"]')
    __add_to_compare_button = (By.XPATH, '//div[@class="compare-products"]/button')
    __add_to_wishlist = (By.XPATH, '//div[@class="add-to-wishlist"]/button')
    __success_text = (By.XPATH, '//div[@class="bar-notification success"]/p/a')
    __input_quantity = (By.XPATH, '//div[@class="add-to-cart-panel"]/input[@class="qty-input"]')
    __error_text = (By.XPATH, '//div[@class="bar-notification error"]/p')

    def product_name(self):
        return self._select_element(self.__product_name).text

    def select_options(self):
        self._click(self.__select_processor)
        self._click(self.__select_ram)
        self._click(self.__select_hdd)
        return self

    def add_to_cart(self):
        self._click(self.__add_to_cart_button)
        return self

    def go_to_cart(self):
        self._click(self.__cart_link)
        return CartPage(self.__driver)

    @property
    def is_notification_error(self):
        return self._is_visible(self.__notification_error_close_button)

    @property
    def is_notification_success(self):
        return self._is_visible(self.__notification_success_close_button)

    @property
    def success_message(self):
        return self._select_element(self.__success_text).text

    @property
    def error_message(self):
        return self._select_element(self.__error_text).text

    def add_to_compare(self):
        self._click(self.__add_to_compare_button)
        return self

    def add_to_wishlist(self):
        self._click(self.__add_to_wishlist)
        return self

    def change_quantity(self, qty):
        self._send_keys(self.__input_quantity, qty)
        return self

    def check_for_error_message(self, message):
        return self.error_message == message and self.is_notification_error

    def check_for_success_message(self, message):
        return self.success_message == message and self.is_notification_success
