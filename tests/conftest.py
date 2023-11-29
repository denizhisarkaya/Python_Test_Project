import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdrivermanager import GeckoDriverManager
# from webdrivermanager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service as FirefoxService


# from webdrivermanager.firefox import GeckoDriverManager

# @pytest.fixture(params=["chrome", "firefox"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
    # my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )

# @pytest.fixture()
# def driver(request):
#     browser = request.config.getoption("--browser")
#     print(f"Creating {browser} driver")
#     if browser == "chrome":
#         my_driver = webdriver.Chrome()
#     elif browser == "firefox":
#         my_driver = webdriver.Firefox()
#     else:
#         raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
#     # my_driver.implicitly_wait(10)
#     yield my_driver
#     print(f"Closing {browser} driver")
#     my_driver.quit()
#     # fixture farklı tesler için aynı işlemi yapmamı sağlıyor.
#     # farklı testler için ortak olan test kurulumu yapmamızı sağlıyor.
#     # her selenium testi için önce bir browser oluşturmamız gerekiyor.
#     # bunu burda her test için fixture ile yapmış oluyoruz.
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
#     )
