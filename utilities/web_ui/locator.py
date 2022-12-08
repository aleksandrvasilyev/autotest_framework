class Locator:
    def __init__(self, method, locator):
        self.__method = method
        self.__locator = locator

    def get_locator(self):
        return self.__method, self.__locator
