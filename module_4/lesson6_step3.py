from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math

#data
answer = str(math.log(int(time.time())))
paste_result_locator = "#ember91"
submit_button_locator = ".submit-submission"

#arrange
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

#act   #, "896", "897", "898", "899","903","904","905"])
@pytest.mark.parametrize('site_link', ["895"])
def test_get_correct_answer(browser, site_link):
    link = f"https://stepik.org/lesson/236{site_link}/step/1"
    browser.get(link)
    paste_result = browser.find_element_by_css_selector(paste_result_locator)
    paste_result.send_keys(answer)

    submit_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS, submit_button_locator))
    )
    submit_button.click
    time.sleep(33)
