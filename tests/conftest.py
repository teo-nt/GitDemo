import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# code to run tests using command line and giving the option to execute them in different browsers
# using the command py.test --browser_name <browser name>
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )



@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption('browser_name')  # pass the value of browser_name given in terminal to a
                                                             # variable called browser_name
    if browser_name == 'edge':
        options = webdriver.EdgeOptions()
        options.add_experimental_option('detach', True)
        ser_obj = Service(r"C:\Users\thod_\Desktop\msedgedriver.exe")
        driver = webdriver.Edge(service=ser_obj, options=options)
    elif browser_name == 'firefox':
        #  firefox invocation gecko driver
        pass
    elif browser_name == 'chrome':
        # chrome invocation driver
        pass
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    driver.implicitly_wait(4)

    request.cls.driver = driver
    yield
    driver.close()
