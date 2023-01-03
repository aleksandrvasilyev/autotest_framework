import requests
from http import HTTPStatus

from my_framework.hw.config_file import BASE_URL


def test_get_pet():
    response = requests.get(f'{BASE_URL}people/1')
    assert response.status_code == HTTPStatus.OK, f'Status code is not as expected ' \
                                                  f'\nActual : {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_response_body():
    response = requests.get('https://swapi.dev/api/people/1')
