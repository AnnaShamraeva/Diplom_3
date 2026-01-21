import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if 'chrome' in request.param:
        driver = webdriver.Chrome()
    elif 'firefox' in request.param:
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
