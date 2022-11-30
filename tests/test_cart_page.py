from random import randint

import pytest


@pytest.mark.smoke
def test_check_count_products_in_cart(open_index_page):
    index = open_index_page
    cart = index.click_to_product().select_options().add_to_cart().go_to_cart()
    assert cart.check_count() == 1


@pytest.mark.regression
def test_change_quantity_in_cart(open_index_page):
    index = open_index_page
    value = randint(0, 100)
    cart_count = index.click_to_product().select_options().add_to_cart().go_to_cart().change_quantity(
        value).check_quantity()
    assert cart_count == str(value)


@pytest.mark.regression
def test_change_quantity_in_cart_negative(open_index_page):
    index = open_index_page
    value = '-5'
    cart = index.click_to_product().select_options().add_to_cart().go_to_cart().change_quantity(value)
    assert cart.check_message_error() == 'This product is required in the quantity of 0'


@pytest.mark.smoke
def test_remove_product_from_cart(open_index_page):
    index = open_index_page
    cart = index.click_to_product().select_options().add_to_cart().go_to_cart().remove_product()
    assert 'empty' in cart


@pytest.mark.smoke
def test_checkout(open_index_page):
    index = open_index_page
    cart = index.click_to_product().select_options().add_to_cart().go_to_cart().checkout()
    assert cart == 'Your order has been successfully processed!'
