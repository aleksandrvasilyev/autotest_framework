from http import HTTPStatus
from my_framework.api_collections.users_api import UsersAPI
from my_framework.data_classes.user import User


def test_get_user():
    response = UsersAPI().get_user_by_id(1)
    assert response.status_code == HTTPStatus.OK


def test_response_body(create_user):
    expected_user = create_user
    response = UsersAPI().get_user_by_id(1)
    user_data = response.json()['data']
    actual_user = User.from_json(**user_data)
    assert actual_user == expected_user


def test_nonexistent_user():
    response = UsersAPI().get_user_by_id(0)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_create_user(create_user):
    expected_user = create_user
    response = UsersAPI().create_user()
    actual_user = response.json()
    del actual_user['createdAt']
    assert response.status_code == HTTPStatus.CREATED
    assert actual_user == expected_user.get_dict()


def test_delete_user_by_id():
    response = UsersAPI().delete_user_by_id(2)
    assert response.status_code == HTTPStatus.NO_CONTENT
    assert response.text == ''

