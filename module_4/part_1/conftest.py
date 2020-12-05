import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en-gb, es, fr")


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    language = request.config.getoption("language")

    if language == "ru":

        print("\nopening russian language web page..")
        link_language = language

    elif language == "en-gb":
        print("\nopening english language web page..")
        link_language = language

    elif language == "es":
        print("\nopening spanish language web page..")
        link_language = language

    elif language == "fr":
        print("\nopening spanish language web page..")
        link_language = language
    else:
        print("\nno language parameter was given, opening russian language web page..")
        link_language = 'ru'

    page_link = f"http://selenium1py.pythonanywhere.com/{link_language}/catalogue/coders-at-work_207/"
    browser.get(page_link)
    #time.sleep(150)
    yield browser
    print("\nquit browser..")

    browser.quit()
