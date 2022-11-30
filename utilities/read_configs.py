import configparser

from my_framework.CONSTANTS import ROOD_DIR

abs_path = f'{ROOD_DIR}/configurations/configuration.ini'
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
