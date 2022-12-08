from selenium.webdriver.common.by import By
from my_framework.utilities.web_ui.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(self.__driver)

    __count_products_in_cart = (By.XPATH, '//table[@class="cart"]//td[@class="product"]')
    __input_quantity = (By.XPATH, '//td[@class="quantity"]/input')
    __update_cart = (By.XPATH, '//button[@id="updatecart"]')
    __message_error = (By.XPATH, '//div[@class="message-error"]//li')
    __remove_link = (By.XPATH, '//button[@class="remove-btn"]')
    __empty_cart_message = (By.XPATH, '//div[@class="order-summary-content"]//div')
    __terms_accept = (By.XPATH, '//input[@id="termsofservice"]')
    __checkout_button = (By.XPATH, '//button[@id="checkout"]')
    __checkout_as_guest = (By.XPATH, '//button[@class="button-1 checkout-as-guest-button"]')
    __first_name = (By.XPATH, '//input[@id="BillingNewAddress_FirstName"]')
    __last_name = (By.XPATH, '//input[@id="BillingNewAddress_LastName"]')
    __email = (By.XPATH, '//input[@id="BillingNewAddress_Email"]')
    __country = (By.XPATH, '//select[@id="BillingNewAddress_CountryId"]/option[@value="231"]')
    __city = (By.XPATH, '//input[@id="BillingNewAddress_City"]')
    __address1 = (By.XPATH, '//input[@id="BillingNewAddress_Address1"]')
    __zip_code = (By.XPATH, '//input[@id="BillingNewAddress_ZipPostalCode"]')
    __phone = (By.XPATH, '//input[@id="BillingNewAddress_PhoneNumber"]')
    __button_continue = (
        By.XPATH, '//div[@id="billing-buttons-container"]//button[@class="button-1 new-address-next-step-button"]')
    __button_continue_1 = (By.XPATH, '//button[@class="button-1 shipping-method-next-step-button"]')
    __button_continue_2 = (By.XPATH, '//button[@class="button-1 payment-method-next-step-button"]')
    __button_continue_3 = (By.XPATH, '//button[@class="button-1 payment-info-next-step-button"]')
    __button_confirm = (By.XPATH, '//button[@class="button-1 confirm-order-next-step-button"]')
    __succes_message = (By.XPATH, '//div[@class="section order-completed"]//div[@class="title"]/strong')

    def count(self):
        return len(self._count_elements(self.__count_products_in_cart))

    def change_quantity(self, value):
        self._send_keys(self.__input_quantity, value)
        self._click(self.__update_cart)
        return self

    def quantity(self):
        return self._select_element(self.__input_quantity).get_attribute('value')

    def message_error(self):
        return self._select_element(self.__message_error).text

    def remove_product(self):
        self._click(self.__remove_link)
        return self._select_element(self.__empty_cart_message).text

    def continue_checkout(self):
        self._click(self.__terms_accept)
        self._click(self.__checkout_button)
        return self

    def checkout_as_guest(self):
        self._click(self.__checkout_as_guest)
        return self

    def fill_user_data(self, firstname, lastname, email, city, address, zipcode, phone):
        self._send_keys(self.__first_name, firstname)
        self._send_keys(self.__last_name, lastname)
        self._send_keys(self.__email, email)
        self._click(self.__country)
        self._send_keys(self.__city, city)
        self._send_keys(self.__address1, address)
        self._send_keys(self.__zip_code, zipcode)
        self._send_keys(self.__phone, phone)
        self._click(self.__button_continue)
        return self

    def shipping_method(self):
        self._click(self.__button_continue_1)
        return self

    def payment_method(self):
        self._click(self.__button_continue_2)
        return self

    def payment_information(self):
        self._click(self.__button_continue_3)
        return self

    def confirm_order(self):
        self._click(self.__button_confirm)
        return self._select_element(self.__succes_message).text
