import pytest
from random import randint


@pytest.mark.smoke
def test_register_new_user(open_index_page, env):
    index = open_index_page
    register = index.go_to_register_page()
    assert register.input_user_data(env.firstname, env.lastname, f'example{randint(0, 9999)}@gmail.com',
                                    env.password_user, env.password_user).user_logged_in()


@pytest.mark.regression
def test_register_new_user_without_firstname(open_index_page, env):
    index = open_index_page
    register = index.go_to_register_page()
    assert register.input_user_data('', env.lastname, f'example{randint(0, 9999)}@gmail.com', env.password_user,
                                    env.password_user).firstname_error()


@pytest.mark.regression
def test_register_new_user_without_email(open_index_page, env):
    index = open_index_page
    register = index.go_to_register_page()
    assert register.input_user_data(env.firstname, env.lastname, '', env.password_user, env.password_user).email_error()


@pytest.mark.regression
def test_register_new_user_passwords_not_match(open_index_page, env):
    index = open_index_page
    register = index.go_to_register_page()
    assert register.input_user_data(env.firstname, env.lastname, f'example{randint(0, 9999)}@gmail.com', env.password_user + '1',
                                    env.password_user).password_match()


@pytest.mark.regression
def test_register_new_user_without_password(open_index_page, env):
    index = open_index_page
    register = index.go_to_register_page()
    assert register.input_user_data(env.firstname, env.lastname, f'example{randint(0, 9999)}@gmail.com', env.password_user,
                                    '').password()
