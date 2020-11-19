from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    x = int(num1)
    y = int(num2)
    z = x + y
    num3 = str(z)


    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(num3)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
