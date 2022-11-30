from my_framework.utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __logout_button = (By.XPATH, "//div[@id='navbarText']//a[@href='/logout']")

    def is_logout_visible(self):
        return self._is_visible(self.__logout_button)
