import pytest


@pytest.mark.smoke
def test_product_page_check_name(open_index_page):
    index_page = open_index_page
    product = index_page.click_to_product()
    assert product.product_name() == 'Build your own computer'


@pytest.mark.smoke
def test_add_to_cart(open_index_page):
    index = open_index_page
    assert index.click_to_product().select_options().add_to_cart().check_for_success_message('shopping cart')


@pytest.mark.regression
def test_add_to_cart_without_options(open_index_page):
    index = open_index_page
    assert index.click_to_product().add_to_cart().is_notification_error


@pytest.mark.smoke
def test_add_to_compare(open_index_page):
    index = open_index_page
    assert index.click_to_product().add_to_compare().check_for_success_message('product comparison')


@pytest.mark.smoke
def test_add_to_wishlist(open_index_page):
    index = open_index_page
    assert index.click_to_product().select_options().add_to_wishlist().check_for_success_message('wishlist')


@pytest.mark.regression
def test_add_to_wishlist_without_options(open_index_page):
    index = open_index_page
    assert index.click_to_product().add_to_wishlist().is_notification_error


@pytest.mark.regression
def test_add_to_cart_negative_quantity(open_index_page):
    index = open_index_page
    assert index.click_to_product().select_options().change_quantity('-1').add_to_cart().check_for_error_message(
        'Quantity should be positive')
