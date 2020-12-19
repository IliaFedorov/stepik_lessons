from .base_page import BasePage
from .locators import ProductPageLocators

#Data
wrong_item_cost_notification = "цена не совпадает"
wrong_item_name_notification = "Название товара не совпадает"
success_message_presented = "Success message is presented, but should not be"
success_message_still_presented = "Success message haven't disappeared, but should"



class ProductPage(BasePage):

    def add_item_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link.click()

    def should_be_same_name(self):
        assert self.browser.find_element(*ProductPageLocators.CARD_ITEM_NAME). \
                   text == self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_NAME).text, wrong_item_name_notification

    def should_be_same_cost(self):
        assert self.browser.find_element(*ProductPageLocators.CARD_ITEM_COST). \
                   text in self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_COST).text, wrong_item_cost_notification

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            success_message_presented

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE) == True, success_message_still_presented





