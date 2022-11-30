import time

from selenium.webdriver.common.by import By

from my_framework.page_objects.category_page import CategoryPage
from my_framework.page_objects.page_product import ProductPage
from my_framework.page_objects.page_register import RegisterPage
from my_framework.utilities.web_ui.base_page import BasePage


class IndexPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(self.__driver)

    __welcome_text = (By.XPATH, '//div[@class="topic-block-title"]/h2')
    __link_to_product = (By.XPATH,
                         '//*[@class="product-grid home-page-product-grid"]//*[@class="item-box"][1]//*[@class="details"]//a')
    __category_link = (By.XPATH, '//ul[@class="top-menu notmobile"]/li[1]//li[2]/a')
    __category_main_link = (By.XPATH, '//ul[@class="top-menu notmobile"]/li[1]/a')
    __register_link = (By.XPATH, '//div[@class="header-links"]//a[@class="ico-register"]')
    __subscribe_input = (By.XPATH, '//input[@id="newsletter-email"]')
    __subscribe_button = (By.XPATH, '//button[@id="newsletter-subscribe-button"]')
    __subscribe_result = (By.XPATH, '//div[@id="newsletter-result-block"]')
    __currency_euro = (By.XPATH, '//*[@id="customerCurrency"]/option[2]')
    __price_with_currency_in_product = (By.XPATH,
                                        '//*[@class="product-grid home-page-product-grid"]//*[@class="item-box"][1]//*[@class="details"]//div[@class="prices"]')
    __button_to_compare = (By.XPATH,
                           '//*[@class="product-grid home-page-product-grid"]//*[@class="item-box"][1]//*[@class="details"]//button[2]')
    __success_close_button = (By.XPATH, '//div[@class="bar-notification success"]/span[@class="close"]')

    def welcome_text(self):
        return self._select_element(self.__welcome_text).text

    def click_to_product(self):
        self._click(self.__link_to_product)
        return ProductPage(self.__driver)

    def click_to_category(self):
        self._hover(self.__category_main_link)
        self._click(self.__category_link)
        return CategoryPage(self.__driver)

    def go_to_register_page(self):
        self._click(self.__register_link)
        return RegisterPage(self.__driver)

    def subscribe(self, email):
        self._send_keys(self.__subscribe_input, email)
        self._click(self.__subscribe_button)
        return self

    def check_subscribe_message(self):
        time.sleep(1)
        return self._select_element(self.__subscribe_result).text

    def set_currency_euro(self):
        self._click(self.__currency_euro)
        return self

    def check_current_currency(self):
        return self._select_element(self.__price_with_currency_in_product).text[0]

    def add_to_compare(self):
        self._click(self.__button_to_compare)
        return self

    def check_added_to_compare(self):
        return self._is_visible(self.__success_close_button)
