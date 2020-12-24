from selenium.webdriver.common.by import By

class BasketPageLocators():
    BASKET_COST_LINK = (By.CSS_SELECTOR, "#messages > div > div > p:nth-child(1) > strong")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    BASKET_CONTENT_LINK = (By.CSS_SELECTOR, ".content .row")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    SEARCH_BOX = (By.CSS_SELECTOR, "[name = 'q']")
    SEARCH_START_BUTTON = (By.CSS_SELECTOR, ".primary-collapse [type = 'submit']")
    SEARCH_RESULT = (By.CSS_SELECTOR, ".form-horizontal > strong")
    ALL_PRODUCTS_DROP_DOWN = (By.CSS_SELECTOR, "#browse .dropdown-toggle")
    ALL_PRODUCT_LINK = (By.CSS_SELECTOR, "[href='/en-gb/catalogue/']")




class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_USER_NAME_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, '[name = "registration-password1"]')
    REGISTRATION_PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, '[name = "registration-password2"]')
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CARD_ITEM_NAME = (By.XPATH, "//div/h1")
    CARD_ITEM_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_ITEM_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    MESSAGE_ITEM_COST = (By.CSS_SELECTOR, "#messages .alert-info")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")

