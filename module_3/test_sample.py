from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".product_price .price_color")
    x = input1.text

    print(x)

    input2 = browser.find_element_by_css_selector(".col-lg-3 form")
    input2.click()
    time.sleep(10)

    input3 = browser.find_element_by_css_selector(".hidden-xs")
    y = input3.text

    print(y)

    assert "Всего в корзине: "+x == y
    print("Всего в корзине: "+x)
    print(y)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()