from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    USER_NAME_FIELD = (By.CSS_SELECTOR, "#")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#")