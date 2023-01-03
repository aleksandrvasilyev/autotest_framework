from selenium.webdriver.common.by import By

from my_framework.utilities.decorators import auto_step
from my_framework.utilities.web_ui.base_page import BasePage
from my_framework.utilities.read_configs import ReadConfig


@auto_step
class RegisterPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(self.__driver)

    day_of_birth = '25'  # need to get it from configuration.json
    month_of_birth = '3'  # need to get it from configuration.json
    year_of_birth = '1994'  # need to get it from configuration.json

    __gender_male = (By.XPATH, '//label[@for="gender-male"]')
    __first_name = (By.XPATH, '//input[@id="FirstName"]')
    __last_name = (By.XPATH, '//input[@id="LastName"]')
    __birthday_day = (By.XPATH, f'//select[@name="DateOfBirthDay"]/option[@value="{day_of_birth}"]')
    __birthday_month = (
        By.XPATH, f'//select[@name="DateOfBirthMonth"]/option[@value="{month_of_birth}"]')
    __birthday_year = (
        By.XPATH, f'//select[@name="DateOfBirthYear"]/option[@value="{year_of_birth}"]')
    __email = (By.XPATH, '//input[@id="Email"]')
    __password1 = (By.XPATH, '//input[@id="Password"]')
    __password2 = (By.XPATH, '//input[@id="ConfirmPassword"]')
    __register_button = (By.XPATH, '//button[@id="register-button"]')
    __result = (By.XPATH, '//div[@class="result"]')
    __logout_button = (By.XPATH, '//div[@class="header-links"]//a[@class="ico-logout"]')
    __error_message_firstname = (By.XPATH, '//span[@id="FirstName-error"]')
    __error_message_email = (By.XPATH, '//span[@id="Email-error"]')
    __error_message_password = (By.XPATH, '//span[@id="ConfirmPassword-error"]')

    def input_user_data(self, fname, lname, email, pwd1, pwd2):
        self._click(self.__gender_male)
        self._send_keys(self.__first_name, fname)
        self._send_keys(self.__last_name, lname)
        self._click(self.__birthday_day)
        self._click(self.__birthday_month)
        self._click(self.__birthday_year)
        self._send_keys(self.__email, email)
        self._send_keys(self.__password1, pwd1)
        self._send_keys(self.__password2, pwd2)
        self._click(self.__register_button)
        return self

    def user_logged_in(self):
        return self._is_visible(self.__result) and self._is_visible(self.__logout_button)

    def firstname_error(self):
        return self._is_visible(self.__error_message_firstname) and 'required' in self._select_element(
            self.__error_message_firstname).text

    def email_error(self):
        return self._is_visible(self.__error_message_email) and 'required' in self._select_element(
            self.__error_message_email).text

    def password_match(self):
        return self._is_visible(self.__error_message_password) and 'do not match' in self._select_element(
            self.__error_message_password).text

    def password(self):
        return self._is_visible(self.__error_message_password) and 'required' in self._select_element(
            self.__error_message_password).text
