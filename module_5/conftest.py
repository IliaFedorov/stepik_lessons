import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: ru, en-gb, es, fr")

@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    request.config.getoption('language')
    esoptions = webdriver.ChromeOptions()
    esoptions.add_argument('language')

    yield browser
    print("\nquit browser..")
    browser.quit()

