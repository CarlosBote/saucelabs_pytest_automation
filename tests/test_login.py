from pages.login_page import LoginPage


def test_login(browser):
    login_page = LoginPage(browser)
    browser.get('https://www.saucedemo.com')

    login_page.login('standard_user', 'secret_sauce')

    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', ("Login failed - URL does not match "
                                                                               "expected value")