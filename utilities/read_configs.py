import configparser

from my_framework.CONSTANTS import ROOT_DIR

abs_path = f'{ROOT_DIR}/configurations/configuration.ini'
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_user_name():
        return config.get('user_data', 'user_name')

    @staticmethod
    def get_browser_id():
        return config.get('browser_data', 'browser_id')

    @staticmethod
    def get_user_phone():
        return config.get('user_data', 'phone')

    @staticmethod
    def get_user_zipcode():
        return config.get('user_data', 'zipcode')

    @staticmethod
    def get_user_address():
        return config.get('user_data', 'address')

    @staticmethod
    def get_user_city():
        return config.get('user_data', 'city')

    @staticmethod
    def get_user_email():
        return config.get('user_data', 'email')

    @staticmethod
    def get_user_lastname():
        return config.get('user_data', 'lastname')

    @staticmethod
    def get_user_firstname():
        return config.get('user_data', 'firstname')

    @staticmethod
    def get_user_day_of_birth():
        return config.get('user_data', 'day_of_birth')

    @staticmethod
    def get_user_month_of_birth():
        return config.get('user_data', 'month_of_birth')

    @staticmethod
    def get_user_year_of_birth():
        return config.get('user_data', 'year_of_birth')
