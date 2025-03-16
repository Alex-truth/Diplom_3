import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(Urls.MAIN_PAGE)

    yield driver
    driver.quit()

