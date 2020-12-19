from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
class TestProductPage:
    @pytest.mark.registered_user
    class TestUserAddToBasketFromProductPage:

        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
            self.page = LoginPage(browser, link)
            self.page.open()
            self.page.go_to_login_page()
            self.page.register_new_user()
            time.sleep(5)
            self.page.should_be_authorized_user()


        def test_user_cant_see_success_message(self, browser):
            # Arrange
            page = ProductPage(browser, link)

            # Act
            page.open()

            # Assert
            page.should_not_be_success_message()

        def test_user_can_add_product_to_basket(self, browser):
            # Arrange
            page = ProductPage(browser, link)
            page.open()
            page.add_item_to_basket()

            # Act
            page.solve_quiz_and_get_code()
            # time.sleep(150)

            # Assert
            page.should_be_same_name()
            page.should_be_same_cost()

    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", \
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        #Arrange
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_basket()

        #Act
        page.solve_quiz_and_get_code()
        #time.sleep(150)

        #Assert
        page.should_be_same_name()
        page.should_be_same_cost()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser)
        page.open()
        page.add_item_to_basket()

        # Act
        page.solve_quiz_and_get_code()

        # Assert
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link)

        # Act
        page.open()

        # Assert
        page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_basket()

        # Act
        page.solve_quiz_and_get_code()

        # Assert
        page.success_message_should_disappear()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link)

        # Act
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()

        # Assert
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        #Act
        page.go_to_basket()

        #Assert
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.empty_basket_message_should_be_empty()
        basket_page.empty_basket_should_be_empty()




