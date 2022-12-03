import pytest


@pytest.mark.smoke
def test_category_page_name(open_index_page):
    index_page = open_index_page
    category = index_page.click_to_category()
    assert category.category_name() == 'Notebooks'


@pytest.mark.smoke
def test_check_display_count(open_index_page):
    index_page = open_index_page
    category = index_page.click_to_category()
    assert category.actual_count_products_on_page() == category.expected_count_products_on_page()


@pytest.mark.regression
def test_change_viewmode(open_index_page):
    index_page = open_index_page
    assert index_page.click_to_category().select_list_view_mode().is_product_list()


@pytest.mark.regression
def test_sort_by_price_from_high_to_low(open_index_page):
    index_page = open_index_page
    price_list = index_page.click_to_category().change_sorting_high_to_low().prices()
    price_list_sort = sorted(price_list, reverse=True)
    assert price_list == price_list_sort


@pytest.mark.regression
def test_sort_by_price_from_low_to_high(open_index_page):
    index_page = open_index_page
    price_list = index_page.click_to_category().change_sorting_low_to_high().prices()
    price_list_sort = sorted(price_list)
    assert price_list == price_list_sort
