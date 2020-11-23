from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_one_item_to_basket():
    #Data
    every_item_button_locator = "Все товары"
    test_main_page_link = "http://selenium1py.pythonanywhere.com/ru"
    basket_add_button_locator = ".col-lg-3 form"
    first_product_name_locator = "//h3/a"
    basket_add_notification_locator = ".alert-success .alertinner "
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(test_main_page_link)
        every_item_list_button = browser.find_element_by_link_text(every_item_button_locator)
        every_item_list_button.click()
        basket_add_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, basket_add_button_locator))
        )

        # Act
        basket_add_button.click()

        # Assert
        first_product_name = browser.find_element_by_xpath(first_product_name_locator).text
        basket_add_notification = browser.find_element_by_css_selector(basket_add_notification_locator).text
        assert first_product_name in basket_add_notification, "Product wasn't added to the basket"

    finally:
        browser.quit()

test_add_one_item_to_basket()
