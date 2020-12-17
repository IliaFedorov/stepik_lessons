from .base_page import BasePage
from .locators import LoginPageLocators
import time



#Data
url_check_text = "login"
login_url_fail_notification = "Ссылка не ведёт на страницу логина"
login_form_fail_notification = "Нет формы для логина"
register_form_fail_notification = "нет формы для регистрации"

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert url_check_text in self.url, login_url_fail_notification

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), login_form_fail_notification

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), register_form_fail_notification

    def register_new_user(self, username, password):
        email = str(time.time()) + "@fakemail.org"
