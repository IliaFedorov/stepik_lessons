from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_button = browser.find_element_by_css_selector("button.btn")
    first_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    required_value = browser.find_element_by_id("input_value").text
    calculated_result = calc(required_value)

    result_paste = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", result_paste)
    result_paste.send_keys(calculated_result)

#    robot_check_box = browser.find_element_by_id("robotCheckbox")
#    robot_check_box.click()

#    robot_radio_button = browser.find_element_by_id("robotsRule")
#    robot_radio_button.click()

    result_button = browser.find_element_by_css_selector("button.btn")
    result_button.click()



finally:
    time.sleep(5)
    browser.quit()
