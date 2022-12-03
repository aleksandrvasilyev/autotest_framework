from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 5)

    def __wait_until_element_located(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def __wait_until_element_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def __wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def __wait_until_elements_located(self, locator):
        return self.__wait.until(EC.presence_of_all_elements_located(locator))

    def _send_keys(self, locator, value):
        element = self.__wait_until_element_clickable(locator)
        element.clear()
        element.send_keys(value)

    def _click(self, locator):
        element = self.__wait_until_element_clickable(locator)
        element.click()

    def _is_visible(self, locator):
        try:
            self.__wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False

    def _wait(self, locator):
        return self.__wait_until_element_located(locator)
        # return webdriver.wait().until(ExpectedConditions.presenceOfElementLocated(
        #     By.xpath("//*[@id='some_input'][contains(@style, 'display: block')]")));

    def _hover(self, locator):
        element = self.__wait_until_element_located(locator)
        hover = ActionChains(self._driver).move_to_element(element)
        hover.perform()

    def _count_elements(self, locator):
        return self.__wait.until(EC.presence_of_all_elements_located(locator))

    def _select_element(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def _select_elements(self, locator):
        return self.__wait.until(EC.presence_of_all_elements_located(locator))

    def _go_to_element(self, locator):
        return self._driver.execute_script("arguments[0].scrollIntoView();", locator)
