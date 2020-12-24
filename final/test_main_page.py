from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

#Data
link = "http://selenium1py.pythonanywhere.com/"
search_text = "c0de"

class TestMainPage:
    @pytest.mark.guest
    class TestGuestFromMainPage:

        @pytest.mark.catalogue
        def test_guest_can_search_for_item(self, browser):
            # Arrange
            page = MainPage(browser, link)
            page.open()

            # Act
            page.paste_search_text(search_text)

            # Assert
            page.should_be_null_find_result()

        @pytest.mark.catalogue
        def test_guest_can_open_catalogue(self,browser):
            # Arrange
            page = MainPage(browser, link)
            page.open()

            # Act
            page.open_catalogue()

            # Assert
            page.should_be_not_null_find_result()

        @pytest.mark.login
        def test_guest_should_see_login_link(self, browser):
            # Arrange
            page = MainPage(browser, link)

            # Act
            page.open()

            # Assert
            page.should_be_login_link()

        @pytest.mark.basket
        def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
            # Arrange
            page = MainPage(browser, link)
            page.open()

            # Act
            page.go_to_basket()

            # Assert
            basket_page = BasketPage(browser, browser.current_url)
            basket_page.empty_basket_message_should_be_empty()
            basket_page.empty_basket_should_be_empty()

    @pytest.mark.user
    class TestUserFromMainPage:

        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
            self.page = LoginPage(browser, link)
            self.page.open()
            self.page.go_to_login_page()
            self.page.register_new_user()
            self.page.should_be_authorized_user()

        @pytest.mark.catalogue
        def test_user_can_search_for_item(self, browser):
            # Arrange
            page = MainPage(browser, link)
            page.open()

            # Act
            page.paste_search_text(search_text)

            # Assert
            page.should_be_null_find_result()

        @pytest.mark.catalogue
        def test_user_can_open_catalogue(self, browser):
            # Arrange
            page = MainPage(browser, link)
            page.open()

            # Act
            page.open_catalogue()

            # Assert
            page.should_be_not_null_find_result()


