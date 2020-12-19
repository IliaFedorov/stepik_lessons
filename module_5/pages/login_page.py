from .base_page import BasePage
from .locators import LoginPageLocators
import time



#Data


password = "QWERTYasdfghZXC321"

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

    def register_new_user(self):

        username_paste = self.browser.find_element(*LoginPageLocators.REGISTRATION_USER_NAME_FIELD)
        username_paste.send_keys(self.generate_mail())
        password_paste = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        password_paste.send_keys(password)
        confirm_password_paste = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_FIELD)
        confirm_password_paste.send_keys(password)
        register_action_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_action_button.click()


