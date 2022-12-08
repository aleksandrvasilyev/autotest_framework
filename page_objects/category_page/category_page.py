from selenium.webdriver.common.by import By

from my_framework.utilities.waits import wait_until
from my_framework.utilities.web_ui.base_page import BasePage
import time


class CategoryPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(self.__driver)

    __category_name = (By.XPATH, '//h1')
    __expected_products_on_page = (By.XPATH, '//select[@id="products-pagesize"]/*[boolean(@selected)]')
    __count_of_products = (By.XPATH, '//div[@class="product-item"]')
    __viewmode_list_link = (By.XPATH, '//a[@data-viewmode="list"]')
    __product_list = (By.XPATH, '//div[@class="product-list"]')
    __from_high_to_low_sorting = (By.XPATH, '//*[@id="products-orderby"]/option[@value="11"]')
    __prices_of_products = (By.XPATH, '//span[@class="price actual-price"]')
    __from_low_to_high_sorting = (By.XPATH, '//*[@id="products-orderby"]/option[@value="10"]')
    __ajax_products_loading = (By.XPATH, "//*[@class='ajax-products-busy'][contains(@style, 'display: none')]")

    def category_name(self):
        return self._select_element(self.__category_name).text

    def actual_count_products_on_page(self):
        return str(len(self._count_elements(self.__count_of_products)))

    def expected_count_products_on_page(self):
        return self._select_element(self.__expected_products_on_page).text

    def select_list_view_mode(self):
        self._click(self.__viewmode_list_link)
        return self

    def is_product_list(self):
        return self._is_visible(self.__product_list)

    def change_sorting_high_to_low(self):
        self._click(self.__from_high_to_low_sorting)
        self._wait(self.__ajax_products_loading)
        return self

    def change_sorting_low_to_high(self):
        self._click(self.__from_low_to_high_sorting)
        self._wait(self.__ajax_products_loading)
        return self

    def prices(self):
        return [float(i.text.replace('$', '').replace('.00', '').replace(',', '.')) for i in
                self._select_elements(self.__prices_of_products)]
