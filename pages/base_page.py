from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_for_element(self, timeout, locator):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))




