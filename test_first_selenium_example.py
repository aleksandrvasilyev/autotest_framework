def test_02(open_login_page):
    login_page = open_login_page
    dash_board_page = login_page.login('admin@yourstore.com', 'admin')
    assert dash_board_page.is_logout_visible() is True, 'User was not logged-in'
