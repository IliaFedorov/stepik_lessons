from selenium import webdriver
import unittest


class TestAbs(unittest.TestCase):
    def test_add_to_basket(self):
        try:
            link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(link)

            first_product = browser.find_element_by_xpath("//h3/a")
            first_product_name = first_product.text
            add_basket_button = browser.find_element_by_css_selector(".col-lg-3 form")
            add_basket_button.click()

            basket_add_notification = browser.find_element_by_css_selector(".alert-success .alertinner ")
            basket_add_notification_text = basket_add_notification.text
            self.assertIn(first_product_name, basket_add_notification_text, "Product wasn't added to the basket")

        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()



