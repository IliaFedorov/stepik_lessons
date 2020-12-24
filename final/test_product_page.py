from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
class TestProductPage:
    @pytest.mark.user
    class TestUserAddToBasketFromProductPage:

        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
            self.page = LoginPage(browser, link)
            self.page.open()
            self.page.go_to_login_page()
            self.page.register_new_user()
            time.sleep(5)
            self.page.should_be_authorized_user()

        @pytest.mark.parametrize('link',
                                 ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", \
                                          marks=pytest.mark.xfail), \
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/", \
                                          marks=pytest.mark.xfail)])
        @pytest.mark.basket
        def test_user_can_add_product_to_basket(self, browser, link):
            # Arrange
            page = ProductPage(browser, link)
            page.open()
            page.add_item_to_basket()

            # Act
            page.solve_quiz_and_get_code()

            # Assert
            page.should_be_same_name()
            page.should_be_same_cost()
