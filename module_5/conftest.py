import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language: ru, en-gb, es, fr")

@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    language = request.config.getoption("language")
    link_language = None

    if language == "ru":

        print("\nopening russian language web page..")
        link_language = language

    elif language == "es":
        print("\nopening spanish language web page..")
        link_language = language

    elif language == "fr":
        print("\nopening spanish language web page..")
        link_language = language
    else:
        print("\nno language parameter was given, opening english language web page..")
        link_language = language

    yield browser
    print("\nquit browser..")
    browser.quit()

