from random import randint
import pytest


@pytest.mark.smoke
def test_check_count_products_in_cart(open_index_page):
    index = open_index_page
    cart = index.click_to_product().select_options().add_to_cart().go_to_cart()
    assert cart.count() == 1


@pytest.mark.regression
def test_change_quantity_in_cart(open_index_page):
    index = open_index_page
    value = randint(0, 20)
    cart_count = index.click_to_product().select_options().add_to_cart().go_to_cart().change_quantity(
        value).quantity()
    assert cart_count == str(value)


@pytest.mark.regression
def test_change_quantity_in_cart_negative(open_index_page):
    index = open_index_page
    value = '-5'
    cart = index.click_to_product().select_options().add_to_cart().go_to_cart().change_quantity(value)
    assert cart.message_error() == 'This product is required in the quantity of 0'


@pytest.mark.smoke
def test_remove_product_from_cart(open_index_page):
    index = open_index_page
    cart = index.click_to_product().select_options().add_to_cart().go_to_cart().remove_product()
    assert 'empty' in cart


@pytest.mark.smoke
def test_checkout(open_index_page):
    index = open_index_page
    cart = index.click_to_product().select_options().add_to_cart().go_to_cart().continue_checkout().checkout_as_guest().fill_user_data().shipping_method().payment_method().payment_information().confirm_order()
    assert cart == 'Your order has been successfully processed!'
