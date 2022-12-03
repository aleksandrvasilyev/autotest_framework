import pytest


@pytest.mark.smoke
def test_check_welcome_text(open_index_page):
    index_page = open_index_page
    assert index_page.welcome_text() == 'Welcome to our store'


@pytest.mark.regression
def test_subscribe_positive(open_index_page):
    index_page = open_index_page
    assert 'Thank you' in index_page.subscribe('test@gmail.com').subscribe_message()


@pytest.mark.regression
def test_subscribe_negative(open_index_page):
    index_page = open_index_page
    assert 'Enter valid email' in index_page.subscribe('test').subscribe_message()


@pytest.mark.smoke
def test_change_currency(open_index_page):
    index_page = open_index_page
    assert index_page.set_currency_euro().current_currency() == '€'


@pytest.mark.regression
def test_add_to_compare(open_index_page):
    index_page = open_index_page
    assert index_page.add_to_compare().added_to_compare()
