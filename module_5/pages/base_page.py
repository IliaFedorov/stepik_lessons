from selenium.common.exceptions import NoSuchElementException
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    #def current_url(self):
    #    self.browser.current_url()

    def solve_quiz_and_get_code(self, data):
        return str(math.log(abs(12 * math.sin(int(data)))))


