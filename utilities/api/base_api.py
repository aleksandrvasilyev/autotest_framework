from my_framework.configurations.config_file import BASE_URL
import requests


class BaseAPI:
    def __init__(self):
        self.__base_url = BASE_URL
        self._headers = {'Content-Type': 'application/json'}
        self.__request = requests

    def get(self, url, headers=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.get(f'{self.__base_url}{url}', params=params, headers=headers)
        return response

    def post(self, url, headers=None, body=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.post(f'{self.__base_url}{url}', headers=headers, data=body, params=params)
        return response

    def delete(self, url, headers=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.delete(f'{self.__base_url}{url}', params=params, headers=headers)
        return response
