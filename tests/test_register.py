import pytest


@pytest.mark.smoke
def test_register_new_user(open_index_page):
    index = open_index_page
    register = index.go_to_register_page()
    assert register.input_user_data('alex', 'vas', 'example2@gmail.com', 'zxcasd', 'zxcasd').user_logged_in()


@pytest.mark.regression
def test_register_new_user_without_firstname(open_index_page):
    index = open_index_page
    register = index.go_to_register_page()
    assert register.input_user_data('', 'vas', 'example2@gmail.com', 'zxcasd', 'zxcasd').firstname_error()


@pytest.mark.regression
def test_register_new_user_without_email(open_index_page):
    index = open_index_page
    register = index.go_to_register_page()
    assert register.input_user_data('alex', 'vas', '', 'zxcasd', 'zxcasd').email_error()


@pytest.mark.regression
def test_register_new_user_passwords_not_match(open_index_page):
    index = open_index_page
    register = index.go_to_register_page()
    assert register.input_user_data('alex', 'vas', 'testik@gmail.com', 'zxcasd1', 'zxcasd').password_match()


@pytest.mark.regression
def test_register_new_user_without_password(open_index_page):
    index = open_index_page
    register = index.go_to_register_page()
    assert register.input_user_data('alex', 'vas', 'testik123@gmail.com', 'password', '').password()
