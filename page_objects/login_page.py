from selenium.webdriver.common.by import By

from my_framework.page_objects.dashboard_page import DashboardPage
from my_framework.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(self.__driver)

    __email_input = (By.XPATH, '//input[@id="Email"]')
    __password_input = (By.CSS_SELECTOR, '#Password')
    __login_button = (By.XPATH, '//*[@type="submit"]')

    def set_email(self, email):
        self._send_keys(self.__email_input, email)
        return self

    def set_password(self, password):
        self._send_keys(self.__password_input, password)
        return self

    def click_login(self):
        self._click(self.__login_button)

    def login(self, email, password):
        self.set_email(email).set_password(password).click_login()
        return DashboardPage(self.__driver)
