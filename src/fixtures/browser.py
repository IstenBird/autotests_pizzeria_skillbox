from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope="class")
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    # chrome_options.add_argument('--headless=new')
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()
