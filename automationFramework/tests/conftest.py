import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    # if browser == 'firefox':
    #     baseUrl = "https://opensource-demo.orangehrmlive.com/"
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseURL)
    #     print("Running tests on FF")
    # else:
    #     #baseUrl = "https://opensource-demo.orangehrmlive.com/"
    #     driver = webdriver.Chrome()
    #     driver.get("https://opensource-demo.orangehrmlive.com/")
    #     print("Running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")