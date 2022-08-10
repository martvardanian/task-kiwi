import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    options = Options()
    # options.add_argument('--headless')

    s = Service(ChromeDriverManager().install())
    if browser == 'chrome':
        driver = webdriver.Chrome(service=s, options=options)
        # driver = webdriver.Chrome(executable_path=DriverPath.CHROME_EXECUTABLE_PATH)
        print("Launching Chrome browser..........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=s, options=options)
        print("Launching Firefox browser..........")
    else:
        driver = webdriver.Chrome(service=s, options=options)
        print("Launching Chrome browser..........")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")