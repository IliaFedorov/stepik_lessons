from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math

#data
final_result_text=[]
paste_result_locator = ".textarea"
submit_button_locator = ".submit-submission"
text_check_locator = ".smart-hints__hint"

#arrange
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

#act   #
@pytest.mark.parametrize('site_link', ["896", "896", "897", "898", "899","903","904","905"])
def test_get_correct_answer(browser, site_link):
    #data
    answer = str(math.log(int(time.time())))
    link = f"https://stepik.org/lesson/236{site_link}/step/1"
    browser.get(link)
    paste_result = browser.find_element_by_css_selector(paste_result_locator)
    paste_result.send_keys(answer)
    submit_button = browser.find_element_by_css_selector(submit_button_locator)
    submit_button.click()
    result = browser.find_element_by_css_selector(text_check_locator)
    result_text = result.text
    final_result_text.append(result_text)
    assert "correct!" in result_text, print(final_result_text)
