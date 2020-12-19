from .base_page import BasePage
from .locators import BasketPageLocators

basket_is_not_empty_notification = "В корзине есть товар"


class BasketPage(BasePage):

    def empty_basket_message_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_COST_LINK), basket_is_not_empty_notification

    def empty_basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT_LINK), basket_is_not_empty_notification
