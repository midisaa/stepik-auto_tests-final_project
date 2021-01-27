import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # selecting a browser
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    # selecting a language
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, en etc.")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
