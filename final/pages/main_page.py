from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasePageLocators
from selenium.webdriver.support.ui import Select
#Data
login_assert_fail = "No link for login page"

class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), login_assert_fail

    def paste_search_text(self, text):
        paste = self.browser.find_element(*BasePageLocators.SEARCH_BOX)
        paste.send_keys(text)
        button = self.browser.find_element(*BasePageLocators.SEARCH_START_BUTTON)
        button.click()

    def open_catalogue(self):
        product_button = self.browser.find_element(*BasePageLocators.ALL_PRODUCT_LINK)
        product_button.click()




