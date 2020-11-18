from selenium import webdriver
import time
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//h3/a")
    x = input1.text

    input2 = browser.find_element_by_css_selector(".col-lg-3 form")
    input2.click()
    time.sleep(5)

    input3 = browser.find_element_by_css_selector(".alert-success .alertinner ")
    y = input3.text

    assert x+" был добавлен в вашу корзину." == y

finally:
    browser.quit()