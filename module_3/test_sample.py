from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_one_item_to_basket():
    try:
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/ru"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        every_item_list_button = browser.find_element_by_link_text("Все товары")
        every_item_list_button.click()
        add_to_basket_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".col-lg-3 form"))
        )

        # Act
        add_to_basket_button.click()

        # Assert
        first_product_name = browser.find_element_by_xpath("//h3/a").text
        basket_add_notification = browser.find_element_by_css_selector(".alert-success .alertinner ").text
        assert first_product_name in basket_add_notification, "Product wasn't added to the basket"

    finally:
        browser.quit()

test_add_one_item_to_basket()
