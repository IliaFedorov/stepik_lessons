from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBasket(unittest.TestCase):
    def test_add_item_to_basket(self):
        try:
            # Arrange
            link = "http://selenium1py.pythonanywhere.com/ru"
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(link)
            every_item_button = browser.find_element_by_link_text("Все товары")
            every_item_button.click()

            # Act
            add_to_basket_button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".col-lg-3 form"))
                )
            add_to_basket_button.click()

            # Assert
            first_product = browser.find_element_by_xpath("//h3/a")
            first_product_name = first_product.text
            basket_add_notification = browser.find_element_by_css_selector(".alert-success .alertinner ")
            basket_add_notification_text = basket_add_notification.text
            self.assertIn(first_product_name, basket_add_notification_text, "Product wasn't added to the basket")

        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()
