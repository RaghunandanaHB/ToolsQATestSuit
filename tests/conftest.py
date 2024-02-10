import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(request):
    service_obj = Service("C:\\Users\\hraghuhb\\AmazonTestSuit\\ToolsQATestSuit\\ChromewebDriver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.toolsqa.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    #driver.quit()