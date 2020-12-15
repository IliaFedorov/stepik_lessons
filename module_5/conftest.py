import pytest
from selenium import webdriver
#import time
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language: ru, en-gb, es, fr")

@pytest.fixture(scope="function")
def browser(request):

    language = request.config.getoption('language')

    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nopening browser..")

    browser = webdriver.Chrome(options=options)
    #browser.maximize_window()

    yield browser
    print("\nquit browser..")
    #time.sleep(15)
    browser.quit()

