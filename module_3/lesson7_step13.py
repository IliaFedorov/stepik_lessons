from selenium import webdriver
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(link)

            input_name = browser.find_element_by_css_selector(".first_block .first")
            input_name.send_keys("Ivan")
            input_lastname = browser.find_element_by_css_selector(".first_block .second")
            input_lastname.send_keys("Petrov")
            input_email = browser.find_element_by_css_selector(".first_block .third")
            input_email.send_keys("ogogo@yohoho.com")

            submit_button = browser.find_element_by_css_selector("button.btn")
            submit_button.click()

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "registration went wrong")

        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()

