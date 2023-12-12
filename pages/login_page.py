from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    username_input = (By.CSS_SELECTOR, '#user-name')
    password_input = (By.XPATH, '//input[@id="password"]')
    submit_btn = (By.ID, 'login-button')

    def enter_username(self, username):
        self.find_element(self.username_input).send_keys('standard_user')

    def enter_password(self, password):
        self.find_element(self.password_input).send_keys('secret_sauce')

    def click_submit(self):
        self.find_element(self.submit_btn).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()



