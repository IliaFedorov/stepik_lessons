from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element_by_id("book")
    button.click()

    required_value = browser.find_element_by_id("input_value").text
    calculated_result = calc(required_value)

    result_paste = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", result_paste)
    result_paste.send_keys(calculated_result)

    result_button = browser.find_element_by_id("solve")
    result_button.click()




finally:
    time.sleep(5)
    browser.quit()
